import sys

Morse_Code_list={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def morse_code_conversion(text):
    morse_code = ''
    for letter in text:
        if letter != ' ':
            morse_code += Morse_Code_list[letter] + ' '
        else:
            morse_code += ' '
    return morse_code
def morse_code_to_text(text):
    text = text.split(' ')
    morse_code = ''
    for letter in text:
        if letter != '':
            morse_code += list(Morse_Code_list.keys())[list(Morse_Code_list.values()).index(letter)]
        else:
            morse_code += ' '
    return morse_code

def main():
    print("-----Welcome to Morse Code Converter-----")
    print("1. Text to Morse Code\n2. Morse Code to Text\n3. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                text = input("Enter the text to convert to Morse Code: ")
                print("Morse Code: ", morse_code_conversion(text.upper()))
            except Exception:
                print("Invalid input")
                main()
        elif choice == 2:
            try:
                text = input("Enter the Morse Code to convert to Text: ")
                print("Text: ", morse_code_to_text(text))
            except Exception:
                print("Invalid input")
                main()
        elif choice == 3:
            sys.exit()
        else:
            print("Invalid choice")
            main()
    except Exception:
        print("Invalid input")
        main()
main()