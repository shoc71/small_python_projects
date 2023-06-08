filepath_and_name = "edit-list.txt"
filepath_and_name_output = "output-edit.txt"

f = open(filepath_and_name, mode='r', encoding="utf-8")
output_txt = open(filepath_and_name_output, mode='w', encoding="utf-8")

list1 = []
remove_list = [" ", "  ", "   ", "    ", "     ", "      ","(", "\t","\n"]
#               0     1     2       3       4         5        6        7 

# f = "This is a sentences \t hihi"

for line in f:
    line = line.rstrip().strip()
    line = line.replace("\t",":")#YAYAYSAYSYAYYAYSAAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSS
    if remove_list[0] in line:
        num = line.index(remove_list[0])
        new_line = line[:num]
    elif remove_list[1] in line:
        num = line.index(remove_list[1])
        new_line = line[:num]
    elif remove_list[2] in line:
        num = line.index(remove_list[2])
        new_line = line[:num]
    elif remove_list[3] in line:
        num = line.index(remove_list[3])
        new_line = line[:num]
    elif remove_list[4] in line:
        num = line.index(remove_list[4])
        new_line = line[:num]
    elif remove_list[5] in line:
        num = line.index(remove_list[5])
        new_line = line[:num]
    elif remove_list[6] in line:
        num = line.index(remove_list[6])
        new_line = line[:num]
    elif remove_list[7] in line:
        num = line.index(remove_list[7])
        new_line = line[:num]
    elif remove_list[8] in line:
        num = line.index(remove_list[8])
        new_line = line[:num]
    else:
        new_line = line

    if ":" in new_line:
        num = new_line.index(':')
        new_line = line[:num]
    else:
        new_line = new_line

    if ',' in line:
        line = new_line.split(', ')
    else:
        line = new_line.split()
    # if '    ' in new_line:
    #     num = line.index(' ')
    #     new_line = line[:num]
    # else:
    #     new_line = new_line
    
    # print(new_line)

    list1.append(new_line)
    # list1.extend(line)

print(list1)

new_string = '\n'.join(list1)
# new_string = new_string.replace
# new_string_2 = new_string.split()
# for line in new_string:
#     if "\n" in line:
#         new_string.replace("\n","")
#     if "\t" in line:
#         new_string = new_string
# print(new_string)
# print(new_string)
output_txt.write(new_string)