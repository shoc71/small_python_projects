import secrets, random
# import string
from tkinter import *

window = Tk()
window.title('Random Password Generator')
window.geometry('400x400')


i = IntVar()
i2 = IntVar()
i3 = IntVar()

pass_string = "qwertyuioplkjhgfdsazxcvbnm"

nums = "1234567890"
symbols = "!@#$%^&*()_+-=}{][\|;:\'\"<>?,./"
upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"

def click_me():
    if i.get() == 0:
        print("No Upper Case Letters")
    elif i.get() == 1:
        print("Upper Case Letters")

    if i2.get() == 0:
        print("No Numbers included")
    elif i2.get() == 1:
        print("Numbers included")

    if i3.get() == 0:
        print("No symbols included")

    elif i3.get() == 1:
        print("Symbols included")

    for j in range(1):
        random_pass = ''.join(secrets.choice(pass_string) for x in range(40))

    l2 = Label(window, bg="white", text=random_pass)
    l2.pack()

l1 = Label(window, bg='white', width=25, text='Select the options below')
l1.pack()

c1 = Checkbutton(window, text = "Upper Case Letters",variable=i)
c1.pack()

c2 = Checkbutton(window, text = "Include Numbers",variable=i2)
c2.pack()

c3 = Checkbutton(window, text = "Include Symbols",variable=i3)
c3.pack()

b = Button(window,text="Click here",command=click_me)
b.pack()

t = Text(window, width=15, height= 1)
t.pack(pady=3)

window.mainloop()