import random

# Globals
GIFT_LIST = "gift-list.txt"
COUNTER = 0
NUMBER_OF_RUNS = 0
FINISHED_RUNS = 4

# Additonal Lists
size = ["Big",'Normal','Small','Tiny','Biggest','Smallest','Micro']
quantity = ['All','Half','Two','Dozen','-1','Three',"Four"]
quality = ['Cheap','Expensive','Dollar',"Live"]

alist = []
dup_list =[]
new_list = []

# random selector
def random_selector(selected_txt_list):
    with open (selected_txt_list, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        random_line = random_line.replace('\n','')

    # counter
    global COUNTER
    COUNTER = COUNTER + 1

    # random selection and formatting
    random_number_selector = random.randint(0,5)

    if (random_number_selector == 0) or (random_number_selector == 5):
        alist.append(f"{COUNTER}. {random_line.title()}")
    elif random_number_selector == 1:
        alist.append(f"{COUNTER}. [random_attribute] of {random_line.title()}")
    elif random_number_selector == 2:
        alist.append(f"{COUNTER}. {random.choice(size)} {random_line.title()}")
    elif random_number_selector == 3:
        alist.append(f"{COUNTER}. {random.choice(quantity)} {random_line.title()}")
    elif random_number_selector == 4:
        alist.append(f"{COUNTER}. {random.choice(quality)} {random_line.title()}")
    # return random_line

def finished_program(selected_list):
    # check for repitition

    for i in selected_list:
            if i not in new_list:
                new_list.append(i)
            else:
                dup_list.append(i)

def print_list(selected_list):
    # merging everything into one string and list
    
    if COUNTER < 4:
        astring = ', '.join(selected_list)
        # astring.replace('\n','')
        print(astring)
    else:
        astring = ',\n'.join(selected_list)
        print(astring)

# main loop
while True:
    random_selector(GIFT_LIST)
    NUMBER_OF_RUNS += 1
    # print(alist)

    # Ending the program
    if NUMBER_OF_RUNS == FINISHED_RUNS:
        finished_program(alist)

        if range(len(new_list)) != FINISHED_RUNS:
            NUMBER_OF_RUNS = NUMBER_OF_RUNS - int(len(dup_list))
        else:
            pass

        print_list(new_list)
        break
print(".end.")