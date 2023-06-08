list1 = []

filepath = r"C:\Users\Sonu.Singh\Desktop\temp-file-jap-names.txt"
filepath_dis = r"C:\Users\Sonu.Singh\Desktop\output_file_jap.txt"

f = open (filepath, encoding="utf-8")
output_txt = open(filepath_dis, mode='w',encoding="utf-8")

for line in f:
    line = line.rstrip()
    if ':' in line:
        num = line.index(':')
        new_line = line[:num]
    else:
        new_line = line
    if ',' in new_line:
        new_line = new_line.split(', ')
    else:
        new_line = new_line.split()
    # if 'or' in new_line:
    #     new_line.remove('or')
    #     list1.extend(new_line)
    # else:
    list1.extend(new_line)

new_string = ' '.join(list1)
new_string = new_string.replace(' or ',' ')
list2 = new_string.split()
# print(list2)
new_string = '\n'.join(list2)

# print(list1)
# print(new_string)

'''filepath('file2.txt','w').write( filepath('file.txt').read().encode('utf-8') )

data = filepath('file.txt').read()
data = data.encode('utf-8')
file('file2.txt','w').write( data )
'''
output_txt.write(new_string)
