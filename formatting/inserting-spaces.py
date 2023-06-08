filepath_and_name = "testing.txt"
filepath_output_and_name = "output_testing.txt"

f = open (filepath_and_name, mode="r", encoding="utf-8")
output_txt = open(filepath_output_and_name, mode="w", encoding="utf-8")

list1 = []

for line in f:
    print(line)
    if line == line.capitalize():
        list1.extend(line[:line])
    
print(list1)
    