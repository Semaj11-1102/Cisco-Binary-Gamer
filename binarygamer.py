
from splinter import Browser
import time

browser = Browser('firefox')


# Dictionaries
global_dictionary = {0: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[1]", 1: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[2]", 2:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[3]", 3:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[4]",4:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[5]",5:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[6]",6:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[7]",7:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[8]"}
binary_number_dictionary = {0:128, 1:64, 2:32, 3:16, 4:8, 5:4, 6:2, 7:1}
button_dictionary = {0:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]" ,1:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[4]", 2: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[5]", 3: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[6]", 4: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[7]", 5: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[8]", 6: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[9]", 7: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[10]", 8: "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[11]", 9:"/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[12]"}
bit_words = {0: "one_twenty_eight", 1: "sixty_four", 2: "thirty_two", 3: "sixteen", 4: "eight", 5: "four", 6: "two", 7: "one"}
bit_values = {  }

# Clicks play
def click_play():
    button = browser.find_by_xpath('/html/body/div/div/div[3]/div/div/button')[0]
    button.click()

# This takes the denary and calculates the binary. It shouldn't be called tests but I don't want to change it
def tests():
    try:
        value = browser.find_by_css('.digits').first.text
        one_twenty_eight = int(value) // 128
        if one_twenty_eight >= 1:
            one_twenty_eight = 1
            value = int(value) - 128
        if one_twenty_eight == 0:
            one_twenty_eight = 0

        sixty_four = int(value) // 64
        if sixty_four >= 1:
            sixty_four = 1
            value = int(value) - 64
        if sixty_four == 0:
            sixty_four = 0

        thirty_two = int(value) // 32
        if thirty_two >= 1:
            thirty_two = 1
            value = int(value) - 32
        if thirty_two == 0:
            thirty_two = 0

        sixteen = int(value) // 16
        if sixteen >= 1:
            sixteen = 1
            value = int(value) - 16
        if sixteen == 0:
            sixteen = 0

        eight = int(value) // 8
        if eight >= 1:
            eight = 1
            value = int(value) - 8
        if eight == 0:
            eight = 0

        four = int(value) // 4
        if four >= 1:
            four = 1
            value = int(value) - 4
        if four == 0:
            four = 0

        two = int(value) // 2
        if two >= 1:
            two = 1
            value = int(value) - 2
        if two == 0:
            two = 0

        one = int(value) // 1
        if one >= 1:
            one = 1
        if one == 0:
            one = 0

        return [one_twenty_eight, sixty_four, thirty_two, sixteen, eight, four, two, one]

    except ValueError:
        time.sleep(0.05)
        return [0,0,0,0,0,0,0,0]

# This sets the buttons to their correct state, completing the question. Can probably be done in the previous function.
def click_buttons():
    try:
        for i in range (0,8):
            button = browser.find_by_xpath(global_dictionary[i]).first

            if binary_nums[i] == 0 and 'on' not in button ['class']:
                pass
            elif binary_nums[i] == 0 and 'on' in button['class']:
                try:
                    button.click()
                except:
                    pass

            if binary_nums[i] != 0 and 'on' in button ['class']:
                pass
            elif binary_nums[i] != 0 and 'on' not in button ['class']:
                try:
                    button.click()
                except:
                    pass

    except TypeError:
        time.sleep(0.05)


def orange_question():
    global binary_nums
    binary_nums = tests()
    click_buttons()

# Works out the total from the binary digits for green question
def green_question_logic():
    global green_value
    green_value = 0

    for i in range (0,8):
        button = browser.find_by_xpath(global_dictionary[i])
        if 'on' in button['class']:
            green_value = int(green_value) + binary_number_dictionary[i]
        else:
            pass
    return (str(green_value))


# Clicks the button to enter the inputs
def green_question_input():
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]')
    button.click()

#enters the first digit
def green_clicking(green_value):

    for i in range (0,10):
        if (str(green_value)[0:1]) == str(i):
            button = browser.find_by_xpath(button_dictionary[i])
            button.click()
    if len(str(green_value)) == 1:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        green_clicking_second_digit(green_value)

#Enters the final digit in 2 digit numbers and the middle digit for 3 digit numbers
def green_clicking_second_digit(green_value):
    for i in range (0,10):
        if (str(green_value)[1:2]) == str(i):
            button = browser.find_by_xpath(button_dictionary[i])
            button.click()
    if len(str(green_value)) == 2:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        green_clicking_third_digit(green_value)

#Enters the final digit in 3 digit numbers
def green_clicking_third_digit(green_value):

    for i in range (0,10):
        if (str(green_value)[2:3]) == str(i):
            button = browser.find_by_xpath(button_dictionary[i])
            button.click()
    if len(str(green_value)) == 3:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        exit("Error reading string")

# Runs all functions for green question
def green_question():
    green_question_logic()
    green_question_input()
    green_clicking(green_value)


def next_level():
    time.sleep(0.05)

    if browser.is_element_present_by_xpath('/html/body/div/div/div[3]/div/div/button',):
        try:
            browser.find_by_xpath('/html/body/div/div/div[3]/div/div/button').first.click()
        except:
            pass

# Starts the program
browser.visit("https://learningcontent.cisco.com/games/binary/index.html")
click_play()
binary_nums = tests()


#Loops the program
while True:
    time.sleep(0.05)
    if browser.is_element_present_by_xpath("/html/body/div/div/div[3]/div/div/button", wait_time=0.1):
        next_level()
        time.sleep(0.1)
        continue
    try:
        box_text = browser.find_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]").first.text
    except:
        box_text = ""

    if "?" in box_text:
        green_question()
    else:
        orange_question()

