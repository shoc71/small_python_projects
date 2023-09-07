str_morse = ""
string = ""
count = 1

user_input = input(f"{count}. Short or Long? [q to quit] / [c to clear] / [cc to convert]: ")

# function converting morse code into a letter
def morse_decoder(morse_code_text, display):

    # keeping it in a string, redundant yes, can be removed and replaced
    morse_code = str(morse_code_text)

    # morse code dictionary
    morse_dict = {
        'short_long_': 'A', 'long_short_short_short_': 'B', 'long_short_long_short_': 'C', 'long_short_short_': 'D', 'short_': 'E',
        'short_short_long_short_': 'F', 'long_long_short_': 'G', 'short_short_short_short_': 'H', 'short_short_': 'I', 'short_long_long_long_': 'J',
        'long_short_long_': 'K', 'short_long_short_short_': 'L', 'long_long_': 'M', 'long_short_': 'N', 'long_long_long_': 'O',
        'short_long_long_short_': 'P', 'long_long_short_long_': 'Q', 'short_long_short_': 'R', 'short_short_short_': 'S', 'long_': 'T',
        'short_short_long_': 'U', 'short_short_short_long_': 'V', 'short_long_long_': 'W', 'long_short_short_long_': 'X', 'long_short_long_long_': 'Y',
        'long_long_short_short_': 'Z', 'long_long_long_long_long_': '0', 'short_long_long_long_long_': '1', 'short_short_long_long_long_': '2', 'short_short_short_long_long_': '3',
        'short_short_short_short_long_': '4', 'short_short_short_short_short_': '5', 'long_short_short_short_short_': '6', 'long_long_short_short_short_': '7', 'long_long_long_short_short_': '8',
        'long_long_long_long_short_': '9'
    }

    # checking if morse code exists or not
    if morse_code_text in morse_dict:
        display = morse_code.replace(morse_code, morse_dict[morse_code])
    else:
        print("No morse_code like that exists. Please refer to the 'Internationl Morse Code'")
        display = ""
    
    # return
    return display

while user_input != "quit":
    # user enters short in text
    if user_input == "1" or user_input =="s" or user_input == "short":
        str_morse += "short_"
        print(str_morse)
    
    # user enters long in text
    elif user_input == "2" or user_input =="l" or user_input == "long":
        str_morse += "long_"
        print(str_morse)
    
    # user converting morse code to string
    elif user_input == "convert" or user_input == "cc":
        # morse_decoder(str_morse, str_ing)
        # morse_decoder(str_morse, string)
        string += morse_decoder(str_morse, string) # I can't believe this works
        print(string)
        print("morse_code_text reset!")
        str_morse = ""
    
    # user quitting code
    elif user_input == "clear" or user_input == "c":
        print("morse_code_text reset!")
        str_morse = ""
    
    # user quitting code
    elif user_input == "q" or user_input == "quit":
        print("program has been quit")
        if len(str_morse) == 0:
            print("no input")
        else:
            print(f"the new word is {str_morse}")
        break
    else:
        print("invalid input, try again")

    # counter
    count += 1
    user_input = input(f"{count}. Short or Long? [q to quit] / [c to clear] / [cc to convert]: ")

# final word for the code
print(f"{(count + 1)}. The final word is {string}")
