import random
import os

DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
GIFT_FILE = DIRECTORY_PATH + '/gift-list.txt'
GIFT_FILE_AI = DIRECTORY_PATH + '/gift-list-AI.txt'
all_condition = False

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

def display_options(combined_list, index):
    clear_terminal()
    save_list = []
    select_list = combined_list[0:index]
    random.shuffle(select_list)
    for item in range(len(select_list)):
        save_list.append(f"{item + 1}. {select_list[item]}")
    return print('\n'.join(save_list))

clear_terminal()
user_input = input("Would you like 1.Human Recommendtions, 2.AI Recommendations, 3.None, 4.Both : ").capitalize()

u_human_gl = unique_check(read_txtfile(GIFT_FILE))
u_ai_gl = unique_check(read_txtfile(GIFT_FILE_AI))

user_input_options = ["0", "Setting", "Set" , "Zero"] + ["3", "No", "Quit", "None", "Three"]
user_input_options += ["1", "Human", "One"] + ["2", "AI", "Two"] + ["4", "Both", "Four"]

while True:
    if user_input in user_input_options:
        break
    if user_input not in user_input_options:
        clear_terminal()
        print("\nPlease input a valid option!\n")
        user_input = input("Would you like 1.Human Recommendtions, 2.AI Recommendations, 3.None, 4.Both : ").capitalize()

if user_input in ["0", "Setting", "Set" , "Zero"]:
    print(f"\nHuman List BEFORE Unique check; {len(read_txtfile(GIFT_FILE))}" + "\n"
          f"Human List AFTER Unique check; {len(unique_check(read_txtfile(GIFT_FILE)))}")
    print(f"AI List BEFORE Unique check; {len(read_txtfile(GIFT_FILE_AI))}" + "\n"
          f"AI List AFTER Unique check; {len(unique_check(read_txtfile(GIFT_FILE_AI)))}")
    print(f"Total unique count with both lists combined; {len(unique_check(read_txtfile(GIFT_FILE_AI))) + len(unique_check(read_txtfile(GIFT_FILE)))}\n")
    
elif user_input in ["3", "No", "Quit", "None", "Three"]:
    print(f"\nUser has selected option -[None]-\n"
          "Program terminated immediately.\n")
    
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
            index = len(u_human_gl)
        elif index >= len(u_human_gl):
            print(f"\nUser Number {index} is greater than {len(u_human_gl)}."
                "Default Number is now {len(u_human_gl)}\n")
            index = len(u_human_gl)
        
        display_options(u_human_gl, index)
        print(f"\nYou have selected HUMAN options with {index} items displayed above!\n")


    elif user_input in ["2", "AI", "Two"]:
        if index >= len(u_ai_gl):
            print(f"\nUser Number {index} is greater than {len(u_ai_gl)}."
                "Default Number is now {len(u_ai_gl)}\n")
            index = len(u_ai_gl)
        elif all_condition == True:
            index = len(u_ai_gl)

        display_options(u_ai_gl, index)
        print(f"\nYou have selected AI options with {index} items displayed above!\n")

    elif user_input in ["4", "Both", "Four"]:
        if index >= (len(u_ai_gl) + len(u_human_gl)):
            print(f"\nUser Number {index} is greater than {len(u_ai_gl) + len(u_human_gl)}."
                "Default Number is now {len(u_ai_gl)}\n")
            index = (len(u_ai_gl) + len(u_human_gl))
        elif all_condition == True:
            index = (len(u_ai_gl) + len(u_human_gl))

        display_options(u_ai_gl + u_human_gl, index) # wanted to make function that could accept something like this without display error
        print(f"\nYou have selected HUMAN & AI options with {index} items displayed above!\n")