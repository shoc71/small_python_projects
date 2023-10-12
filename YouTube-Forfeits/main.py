# imports
import random

#  globals
OPTIONS = ['1. Easy', '2. Meduim', '3. Hard', '0. Random', '4. Agony', 'Q. Quit']
EASY_PUNISHMENTS = "easy-fft.txt"
MEDIUM_PUNISHMENTS = "medium-fft.txt"
HARD_PUNISHMENTS = "hard-fft.txt"
user_input = ''
counter = 0

# display options
def display_options(count):
    global user_input
    if count == 0:
        print("This is a Youtube Forfeit/Punishment Selector. These are your options")
    
    print(f"{OPTIONS} - remhaq")
    user_input = input("Enter your selection : ")


# random choice selection
def random_choice(user_input):
    # creating randomness
    random_number = random.randint(0,100)

    # 50% chance of easy punishment
    if random_number >= 0 and random_number <= 50:
        print("\nselected from easy list")
        random_choice_from_txt(EASY_PUNISHMENTS)
    
    # 40% chance of medium punishment
    elif random_number >= 51 and random_number <= 90:
        print("\nselected from medium list")
        random_choice_from_txt(MEDIUM_PUNISHMENTS)

    # 10% chance of hard punishment
    elif random_number >= 91 and random_number <= 100:
        print("\nselected from hard list")
        random_choice_from_txt(HARD_PUNISHMENTS)
    
    # agony has not been coded for


# making a random choice from the selected txt file
def random_choice_from_txt(selected_txt):
    with open (selected_txt, 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
        random_line = random.choice(lines).replace('\n','')
        print('\n')
        print(f"{counter + 1}. {random_line.title()}")
        print('\n')
        # return random_line


# main loop
while True:

    display_options(counter)

    # options
    if (user_input == '0') or (user_input == 'random') or (user_input == 'r'):
        random_choice(user_input)
    elif (user_input == '1') or (user_input == 'easy') or (user_input == 'e'):
        random_choice_from_txt(EASY_PUNISHMENTS)
    elif (user_input == '2') or (user_input == 'medium') or (user_input == 'm'):
        random_choice_from_txt(MEDIUM_PUNISHMENTS)
    elif (user_input == '3') or (user_input == 'hard') or (user_input == 'h'):
        random_choice_from_txt(HARD_PUNISHMENTS)
    elif (user_input == '4') or (user_input == 'agony') or (user_input == 'a'):
        print("No...")

    # quit
    elif (user_input == 'q') or (user_input == 'quit'):
        print("-----------\n\nThis program has been ended\n-----------")
        break

    # invalid input
    else:
        print("-----------\nInvalid Input. Try Again.\n-----------")

    counter += 1

    if counter >= 10:
        counter = 0
