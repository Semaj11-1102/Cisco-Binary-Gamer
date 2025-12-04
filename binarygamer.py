from splinter import Browser
import time
browser = Browser()

# Clicks play
def click_play():
    button = browser.find_by_xpath('/html/body/div/div/div[3]/div/div/button')[0]
    button.click()

# This takes the denary and calculates the binary. It shouldn't be called tests but I don't want to change it
def tests():
    element = browser.find_by_css('.digits')[0]
    value = element.text
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

# This sets the buttons to their correct state, completing the question. Can probably be done in the previous function.
def click_buttons():
    #128
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[1]')
    except Exception:
        print (error)
        pass
    if binary_nums[0] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[0] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[0] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[0] != 0 and 'on' not in button ['class']:
        button.click()

    #64
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[2]')
    except Exception:
        print (error)
    if binary_nums[1] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[1] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[1] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[1] != 0 and 'on' not in button ['class']:
        button.click()

    #32
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[3]')
    except Exception:
        print (error)
    if binary_nums[2] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[2] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[2] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[2] != 0 and 'on' not in button ['class']:
        button.click()

    #16
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[4]')
    except Exception:
        print(error)
    if binary_nums[3] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[3] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[3] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[3] != 0 and 'on' not in button ['class']:
        button.click()

    #8
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[5]')
    except Exception:
        print(error)
    if binary_nums[4] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[4] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[4] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[4] != 0 and 'on' not in button ['class']:
        button.click()

    #4
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[6]')
    except Exception:
        print(error)
    if binary_nums[5] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[5] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[5] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[5] != 0 and 'on' not in button ['class']:
        button.click()

    #2
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[7]')
    except Exception:
        print(error)
    if binary_nums[6] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[6] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[6] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[6] != 0 and 'on' not in button ['class']:
        button.click()

    #1
    try:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[8]')
    except Exception:
        print(error)
    if binary_nums[7] == 0 and 'on' not in button ['class']:
        pass
    elif binary_nums[7] == 0 and 'on' in button['class']:
        button.click()

    if binary_nums[7] != 0 and 'on' in button ['class']:
        pass
    elif binary_nums[7] != 0 and 'on' not in button ['class']:
        button.click()

def orange_question():
    global binary_nums
    binary_nums = tests()
    tests()
    #get_button_states()
    click_buttons()

# Works out the total from the binary digits for green question
def green_question_logic():
    global green_value
    green_value = 0
    #128
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[1]')
    if 'on' in button['class']:
        green_value = int(green_value) + 128
    else:
        pass
    #64
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[2]')
    if 'on' in button['class']:
        green_value = int(green_value) + 64
    else:
        pass
    #32
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[3]')
    if 'on' in button['class']:
        green_value = int(green_value) + 32
    else:
        pass
    #16
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[4]')
    if 'on' in button['class']:
        green_value = int(green_value) + 16
    else:
        pass
    #8
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[5]')
    if 'on' in button['class']:
        green_value = int(green_value) + 8
    else:
        pass
    #4
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[6]')
    if 'on' in button['class']:
        green_value = int(green_value) + 4
    else:
        pass
    #2
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[7]')
    if 'on' in button['class']:
        green_value = int(green_value) + 2
    else:
        pass
    #1
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/button[8]')
    if 'on' in button['class']:
        green_value = int(green_value) + 1
    else:
        pass
    return (str(green_value))

# Clicks the button to enter the inputs
def green_question_input():
    button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]')
    button.click()

#enters the first digit
def green_clicking(green_value):
    if (str(green_value)[0:1]) == '1':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[4]')
        button.click()
    elif (str(green_value)[0:1]) == '2':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[5]')
        button.click()
    elif (str(green_value)[0:1]) == '3':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[6]')
        button.click()
    elif (str(green_value)[0:1]) == '4':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[7]')
        button.click()
    elif (str(green_value)[0:1]) == '5':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[8]')
        button.click()
    elif (str(green_value)[0:1]) == '6':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[9]')
        button.click()
    elif (str(green_value)[0:1]) == '7':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[10]')
        button.click()
    elif (str(green_value)[0:1]) == '8':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[11]')
        button.click()
    elif (str(green_value)[0:1]) == '9':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[12]')
        button.click()
    elif (str(green_value)[0:1]) == '0':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]')
        button.click()
    if len(str(green_value)) == 1:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        green_clicking_second_digit(green_value)

#Enters the final digit in 2 digit numbers and the middle digit for 3 digit numbers
def green_clicking_second_digit(green_value):
    if (str(green_value)[1:2]) == '1':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[4]')
        button.click()
    elif (str(green_value)[1:2]) == '2':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[5]')
        button.click()
    elif (str(green_value)[1:2]) == '3':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[6]')
        button.click()
    elif (str(green_value)[1:2]) == '4':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[7]')
        button.click()
    elif (str(green_value)[1:2]) == '5':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[8]')
        button.click()
    elif (str(green_value)[1:2]) == '6':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[9]')
        button.click()
    elif (str(green_value)[1:2]) == '7':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[10]')
        button.click()
    elif (str(green_value)[1:2]) == '8':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[11]')
        button.click()
    elif (str(green_value)[1:2]) == '9':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[12]')
        button.click()
    elif (str(green_value)[1:2]) == '0':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]')
        button.click()
    if len(str(green_value)) == 2:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        green_clicking_third_digit(green_value)

#Enters the final digit in 3 digit numbers
def green_clicking_third_digit(green_value):
    if (str(green_value)[2:3]) == '1':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[4]')
        button.click()
    elif (str(green_value)[2:3]) == '2':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[5]')
        button.click()
    elif (str(green_value)[2:3]) == '3':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[6]')
        button.click()
    elif (str(green_value)[2:3]) == '4':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[7]')
        button.click()
    elif (str(green_value)[2:3]) == '5':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[8]')
        button.click()
    elif (str(green_value)[2:3]) == '6':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[9]')
        button.click()
    elif (str(green_value)[2:3]) == '7':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[10]')
        button.click()
    elif (str(green_value)[2:3]) == '8':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[11]')
        button.click()
    elif (str(green_value)[2:3]) == '9':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[12]')
        button.click()
    elif (str(green_value)[2:3]) == '0':
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]')
        button.click()
    if len(str(green_value)) == 3:
        button = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/button[3]')
        button.click()
    else:
        exit(7)

# Runs all functions for green question
def green_question():
    green_question_logic()
    green_question_input()
    green_clicking(green_value)
    time.sleep(0.5)

def next_level():
    try:
        element_next = browser.find_by_xpath('/html/body/div/div/div[3]/div/div/button')
        element_next.click()
        print("Next level clicked")
    except Exception as error:
        print (error)
        exit(8)


# Starts the program
browser.visit('https://learningcontent.cisco.com/games/binary/index.html')
click_play()
binary_nums = tests()

element_box =  browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]')

#Loops the program
while True:
    try:
        element_box = browser.find_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]')
        if "?" in element_box.text:
            green_question()
            #next_level()
            time.sleep(1)
        else:
            orange_question()
            #next_level()
            time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(5)

