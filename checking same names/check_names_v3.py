import random, time, datetime

start_time = time.time()

filepath = r"C:\Users\shoc71\Desktop\all_names.txt"

print(f"\nThis program has started on {datetime.datetime.now()}\n")

list1 = []
new_list = []
dup_list = []

with open (filepath, mode='r', encoding='utf-8') as f:
    line = f.readlines()
    list1.append(line)
    
for i in line:
    if i not in new_list:
        new_list.append(i)
    else:
        dup_list.append(i)

# new_list = random.shuffle(new_list)
new_list = random.sample(new_list, len(new_list))
new_list = ''.join(new_list).title()

seconds = (time.time() - start_time)
minutes = seconds / 60
calc_percent = len(dup_list)/len(line)
seconds = round(seconds, 3)
minutes = round(minutes, 2)

calc_percent = round((calc_percent*100),2)

# print(f"Unique characters list : {new_list}")
print(f"List of duplicates : {dup_list} \n")
print(f"List before program is <{len(line)}> and new list count now <{len(line)-len(dup_list)}>")
print(f"This is the number of duplicates you have : {len(dup_list)}\
 - {calc_percent}% list reduction \n")
print("This code took --- %s seconds --- to run" % (seconds))
print(f"This code took --- {minutes} minutes --- to finish \n")
print(f"Program has been finished on {datetime.datetime.now()}")

with open (filepath, mode='w', encoding='utf-8') as f:
    f.write(new_list)
f.close()
