# imports
import random
import os

def clear_terminal():
    """
    Clears the terminal screen.
    """
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix-like systems (Linux, macOS)

def read_txtfile(FILE):
    """
    Argument:
        must be path, format as string

    Returns:
        list of contents in txtfile
    """
    with open(FILE, 'r',encoding='utf-8',errors='ignore') as file:
        return file.readlines()

def unique_check(g_list):
    """
    Argument:
        must be list

    Returns:
        a list of unique strings
    """
    return list(set([str(line).replace("\n","").title().strip() for line in g_list]))

def exit_protocal():
    exit_option = input("\n" + "Would you like re-run this program? (Y/N) : ").lower()
    if exit_option in ["n", "q"]:
        return True
    elif exit_option in ["r", "y"]:
        return False
    else:
        print("Select a valid option!")
        exit_protocal()

def display_options(combined_list, index):
    """
    Arguments:
        - list
        - randomized and the indexed to a certain position
        - numbered order of each random item from list
    Returns:
        - ordered strings inside of list
    """
    clear_terminal()
    save_list = []
    select_list = combined_list[0:index]
    random.shuffle(select_list)
    for item in range(len(select_list)):
        save_list.append(f"{item + 1}. {select_list[item]}")
    return print('\n'.join(save_list))

# Globals
DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
GIFT_FILE = DIRECTORY_PATH + '/lists/gift-list.txt'
GIFT_FILE_AI = DIRECTORY_PATH + '/lists/gift-list-AI.txt'

UNIQUE_HUMAN_GIFTLIST = unique_check(read_txtfile(GIFT_FILE))
UNIQUE_AI_GIFTLIST = unique_check(read_txtfile(GIFT_FILE_AI))

USER_INPUT_OPTIONS = ["0", "Setting", "Set" , "Zero"] + ["3", "No", "Quit", "None", "Three"]
USER_INPUT_OPTIONS += ["1", "Human", "One"] + ["2", "AI", "Two"] + ["4", "Both", "Four"]

def listing_options(user_input):
    all_condition = False
    while True:
        if user_input in USER_INPUT_OPTIONS:
            break
        if user_input not in USER_INPUT_OPTIONS:
            clear_terminal()
            print("\nPlease input a valid option!\n")
            user_input = input("Would you like 1.Human Recommendtions, 2.AI Recommendations, 3.None, 4.Both : ").capitalize()

    if user_input in ["0", "Setting", "Set" , "Zero"]:
        print(f"\nHuman List BEFORE Unique check; {len(read_txtfile(GIFT_FILE))}" + "\n"
            f"Human List AFTER Unique check; {len(unique_check(read_txtfile(GIFT_FILE)))}")
        print(f"AI List BEFORE Unique check; {len(read_txtfile(GIFT_FILE_AI))}" + "\n"
            f"AI List AFTER Unique check; {len(unique_check(read_txtfile(GIFT_FILE_AI)))}")
        print(f"\nTotal unique count with both lists combined; {len(unique_check(read_txtfile(GIFT_FILE_AI))) + len(unique_check(read_txtfile(GIFT_FILE)))}\n")
        
    elif user_input in ["3", "No", "Quit", "None", "Three"]:
        print(f"\nUser has selected option -[None]-\n")
        
    else:
        clear_terminal()
        user_index_input = input("How many gift-ideas / options would like to know of? 1.Zero, 2.(Custom number, just type it), All : ")

        while True:
            try:
                if user_index_input in ["all", "All", 3]:
                        print("\nYou have selected the [ALL] option count!\n")
                        all_condition = True
                        break
                else:
                    index = int(round(float(user_index_input), 0))
                    break

            except:
                print("\nThe following prompt about the number of options requires a number input.\n"
                    "Please Enter A Valid Number.\n")
                user_index_input = input("How many gift-ideas / options would like to know of? 1.Zero, 2.(Custom number, just type it), 3.All : ")
                clear_terminal()

        if user_input in ["1", "Human", "One"]:
            if all_condition == True:
                index = len(UNIQUE_HUMAN_GIFTLIST)
            elif index >= len(UNIQUE_HUMAN_GIFTLIST):
                print(f"\nUser Number {index} is greater than {len(UNIQUE_HUMAN_GIFTLIST)}."
                    "Default Number is now {len(u_human_gl)}\n")
                index = len(UNIQUE_HUMAN_GIFTLIST)
            
            display_options(UNIQUE_HUMAN_GIFTLIST, index)
            print(f"\nYou have selected HUMAN options with {index} items displayed above!\n")


        elif user_input in ["2", "AI", "Two"]:
            if index >= len(UNIQUE_AI_GIFTLIST):
                print(f"\nUser Number {index} is greater than {len(UNIQUE_AI_GIFTLIST)}."
                    "Default Number is now {len(u_ai_gl)}\n")
                index = len(UNIQUE_AI_GIFTLIST)
            elif all_condition == True:
                index = len(UNIQUE_AI_GIFTLIST)

            display_options(UNIQUE_AI_GIFTLIST, index)
            print(f"\nYou have selected AI options with {index} items displayed above!\n")

        elif user_input in ["4", "Both", "Four"]:
            if index >= (len(UNIQUE_AI_GIFTLIST) + len(UNIQUE_HUMAN_GIFTLIST)):
                print(f"\nUser Number {index} is greater than {len(UNIQUE_AI_GIFTLIST) + len(UNIQUE_HUMAN_GIFTLIST)}."
                    "Default Number is now {len(u_ai_gl)}\n")
                index = (len(UNIQUE_AI_GIFTLIST) + len(UNIQUE_HUMAN_GIFTLIST))
            elif all_condition == True:
                index = (len(UNIQUE_AI_GIFTLIST) + len(UNIQUE_HUMAN_GIFTLIST))

            display_options(UNIQUE_AI_GIFTLIST + UNIQUE_HUMAN_GIFTLIST, index) # wanted to make function that could accept something like this without display error
            print(f"\nYou have selected HUMAN & AI options with {index} items displayed above!\n")

def main():
    while True:
        clear_terminal()
        user_choice_n_options = input("Would you like 1.Human Recommendtions, 2.AI Recommendations, 3.None, 4.Both : ").capitalize()
        listing_options(user_input=user_choice_n_options)

        # Exiting infinite loop condition
        leave = exit_protocal()
        if leave == True:
            clear_terminal()
            break

if __name__ =="__main__":
    main()