import random

# Globals
GIFT_LIST = "gift-list.txt"

NUMBER_OF_RUNS = 0
FINISHED_RUNS = 5

# Additonal Lists
size = ["Big",'Normal','Small','Tiny','Biggest','Smallest']
alist = []
dup_list =[]
new_list = []

# random selector
def random_selector(selected_txt_list):
    with open (selected_txt_list, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        random_line = random_line.replace('\n','')
    # return random_line

    random_number_selector = random.randint(0,2)

    if random_number_selector == 0:
        # print(random_line.capitalize())
        alist.append(random_line.capitalize())
    elif random_number_selector == 1:
        # print(f"{random_line.capitalize()} .[random_attribute]")
        alist.append(f"[random_attribute] of {random_line.capitalize()}")
    elif random_number_selector == 2:
        # print(f"{random_line.capitalize()} .{random.choice(size)}")
        alist.append(f"{random.choice(size)} {random_line.capitalize()}")
    # return random_line



# main loop
while True:
    random_selector(GIFT_LIST)
    NUMBER_OF_RUNS += 1
    # print(alist)
    if NUMBER_OF_RUNS == FINISHED_RUNS:
        astring = ', '.join(alist)
        # astring.replace('\n','')
        print(astring)
        break
print(".end.")
