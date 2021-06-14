import re
ENCRYPTION_CODE = {
                    'a':'.-', 
                    'b':'-...', 
                    'c':'-.-.', 
                    'd':'-..', 
                    'e':'.', 
                    'f':'..-.', 
                    'g':'--.',
                    'h':'....', 
                    'i':'..', 
                    'j':'.---', 
                    'k':'-.-', 
                    'l':'.-..', 
                    'm':'--', 
                    'n':'-.',
                    'o':'---', 
                    'p':'.--.', 
                    'q':'--.-', 
                    'r':'.-.', 
                    's':'...', 
                    't':'-', 
                    'u':'..-',
                    'v':'...-', 
                    'w':'.--', 
                    'x':'-..-', 
                    'y':'-.--', 
                    'z':'--..', 
                    ' ':'/'
                    }

#prints the menu
def display_menu():
    num_of_asterix = 30
    print()
    print(f"*" * num_of_asterix)
    print(f"{'Translate text (Press t):': ^30s}\n{'Translate morse (Press m):': ^30s} \n{'Exit (Press x):': ^30s} \n")
    print(f"*" * num_of_asterix)
    return input()


#cleans the input text string, calls the encrypter and prints result
def handle_txt_to_morse(user_input_translated):
    user_str = input("Please enter the text to translate: \n ")
    if user_str == "":
        print("\nInvalid input! Please enter letters or spaces only.")
        return user_input_translated

    invalid_input = False
    for char in user_str:
        if char.lower() not in ENCRYPTION_CODE.keys():
            invalid_input = True
            break
                
    if invalid_input == True:
        print("\nInvalid input! Please enter letters or spaces only.")
        
    else:
        user_input_translated = True
        result = morse_code_encrypter(user_str.lower())
        result_str = f"\n{'Text:': <15s}{user_str}\n\n{'Morse Code:': <15s}{result}\n"
        display_result(result_str)
        
    return user_input_translated


#translates input text to morse code
def morse_code_encrypter(user_str):
    txt_to_morse = ''
    for letter in user_str:
        txt_to_morse += (ENCRYPTION_CODE[letter]) + ' '
       
    txt_to_morse = txt_to_morse.rstrip()
    return txt_to_morse



#cleans the input morse code string, calls the decrypter and prints result
def handle_morse_to_txt(user_input_translated):
    user_str = input("Please enter the morse code to translate: \n")
    if re.search("[^\.\-\/\s]",user_str) or user_str == "":
        print("\nInvalid input! Please enter .  -  / or spaces only.")
           
    else:
        user_input_translated = True
        result = morse_code_decrypter(user_str)
        result_str = f"\n{'Morse Code:': <15s}{user_str}\n\n{'Text:': <15s}{result}\n"
        display_result(result_str)

    return user_input_translated



#translates input morse code to text
def morse_code_decrypter(user_morse_str):
    morse_to_txt = ''
    morse_arr = user_morse_str.split(' ')
    for morse in morse_arr:
        valid_morse = False
        for key,val in ENCRYPTION_CODE.items():
            if morse == val:
                morse_to_txt += key
                valid_morse = True
                break
        
        if valid_morse == False and morse != "":
            print(f"Invalid morse code: {morse}")
            morse_to_txt +=  morse
            
    return morse_to_txt


#prints the result
def display_result(result_str):
    num_of_asterix = 75
    print()
    print(f"*" * num_of_asterix)
    print(f"{result_str}")
    print(f"*" * num_of_asterix)
    print()


#main
def main():
    user_input_translated = False
    while not (user_input_translated):
        translate_txt_or_morse = display_menu()

        if translate_txt_or_morse.lower() == "t":
            user_input_translated = handle_txt_to_morse(user_input_translated)
        
            
        elif translate_txt_or_morse.lower() == "m":
            user_input_translated = handle_morse_to_txt(user_input_translated)

    
        elif translate_txt_or_morse.lower() == "x":
            print("Until next time, goodbye\n")
            break

        else:
            print("\nIncorrect input: Please enter only from the following: t, m or x")


main()
        


