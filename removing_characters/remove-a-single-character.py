list1 = []
filepath_txt_2 = r"C:\Users\shoc71\Desktop\temptemp.txt" #insert filepath here, if the file is not in the same folder as the file
output_file = open('output.txt', 'w')

# int_check2 = '012345678910'
# space_check = ' '

# opeing the og file
with open(filepath_txt_2, mode = 'r', encoding='utf-8') as f:
    line = f.readlines()
    list1.append(line)

new_list = ''.join(line)


remove_char = "\n"
replace_char = " "

new_string = new_list.replace(remove_char,replace_char)

print(new_string)
