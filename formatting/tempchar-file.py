list1 = []
filepath_txt_2 = r"C:\Users\Sonu.Singh\Desktop\temptemp.txt" #insert filepath here
output_file = open('output.txt', 'w')

user_input = input("formating or custom? : ")

int_check2 = '012345678910'
# opeing the og file
with open('temptemp.txt', encoding="utf-8") as f:
    line = f.readline().rstrip().split()

print(line)

for ch in line:
    if user_input == 'formating':
        if ch[-1] == '.' and line[-2] not in int_check2:
            ch = ch[:] + '\n\n\t'
        else:
            ch = ch[:] + ' '
    output_file.write(ch)
#new_list = ''.join(line)

# if user_input == "custom":
#     user_input_1 = input("What character would you like removed? : ")
#     remove_char = str(user_input_1)
#     user_input_2 = input("What would you like to replace it with? :")
#     replace_char = str(user_input_2)
#     new_string = new_list.replace(remove_char,replace_char)
# else:
#     print("fuk off")


# try:
#     with open (filepath_txt_2, 'w') as f:
#         f.write(new_string)
#         print("done")
# except:
#     with open (filepath_txt_2, 'x') as f:
#         f.write(new_string)
#         print("what have u done")

# f.close()
