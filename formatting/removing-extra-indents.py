list1 = []
output_txt = open('output_file.txt', mode='w',encoding="utf-8")

with open ('indented.txt', mode='r',encoding='utf-8') as f:
    line = f.readlines()

new_string_1 = ''.join(line)
print(new_string_1)
new_string_2 = new_string_1.replace("\n"," ")
# print(new_string_2) -- it works bruh
output_txt.write(new_string_2)