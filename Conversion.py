# function: error handling for invalid input
def get_input(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

# function: string converter
def convert_string(string):
    return [ord(char) for char in string]
# string menu
def string_menu():
    print("\n")
    print("=================== String to ASCII ====================")
    string = input("Enter a string: ")
    print("ASCII code:", convert_string(string))
    print("========================================================")
    repeat = input("Would you like to convert another string? (y/n): ") 
    if repeat.lower() == "y":
        string_menu()
    elif repeat.lower() == "n":
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# function: decimal converter
def convert_decimal(num, select):
    if select == 1:
        return bin(num)[2:]
    elif select == 2:
        return oct(num)[2:]
    elif select == 3:
        return hex(num)[2:]
    else:
        return None
# decimal menu
def decimal_menu():
    print("\n")
    print("================== Decimal Converter ===================")
    num = get_input("Enter a decimal number: ")
    print("Convert to?")
    print("1. Binary")
    print("2. Octal")
    print("3. Hexadecimal")
    select = get_input("Input your choice: ")
    print("Answer:", convert_decimal(num, select))
    print("========================================================")
    repeat = input("Would you like to convert another decimal? (y/n): ") 
    if repeat.lower() == "y":
        decimal_menu()
    elif repeat.lower() == "n":
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# function: binary converter
def convert_binary(num, select):
    # convert number to string
    num_str = str(num)
    if select == 1:
        return int(num_str, 2)
    elif select == 2:
        return oct(int(num_str, 2))[2:]
    elif select == 3:
        return hex(int(num_str, 2))[2:]
    else:
        return None
# binary menu
def binary_menu():
    print("\n")
    print("=================== Binary Converter ===================")
    num = get_input("Enter a binary number: ")
    print("Convert to?")
    print("1. Decimal")
    print("2. Octal")
    print("3. Hexadecimal")
    select = get_input("Input your choice: ")
    print("Answer:", convert_binary(num, select))
    print("========================================================")
    repeat = input("Would you like to convert another binary? (y/n): ") 
    if repeat.lower() == "y":
        binary_menu()
    elif repeat.lower() == "n":
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# function: octal converter
def convert_octal(num, select):
    num_str = str(num)
    if select == 1:
        return int(num_str, 8)
    elif select == 2:
        return bin(int(num_str, 8))[2:]
    elif select == 3:
        return hex(int(num_str, 8))[2:]
    else:
        return None
# octal menu
def octal_menu():
    print("\n")
    print("=================== Octal Converter ====================")
    num = get_input("Enter an octal number: ")
    print("Convert to?")
    print("1. Decimal")
    print("2. Binary")
    print("3. Hexadecimal")
    select = get_input("Input your choice: ")
    print("Answer:", convert_octal(num, select))
    print("========================================================")
    repeat = input("Would you like to convert another string? (y/n): ") 
    if repeat.lower() == "y":
        octal_menu()
    elif repeat.lower() == "n":
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# function: hexadecimal converter 
def convert_hexadecimal(num, select):
    num_str = str(num)
    if select == 1:
        return int(num_str, 16)
    elif select == 2:
        return bin(int(num_str, 16))[2:]
    elif select == 3:
        return oct(int(num_str, 16))[2:]
    else:
        return None
# hexadecimal menu
def hex_menu():
    print("\n")
    print("================ Hexadecimal Converter =================")
    num = input("Enter a hexadecimal number: ")
    print("Convert to?")
    print("1. Decimal")
    print("2. Binary")
    print("3. Octal")
    select = get_input("Input your choice: ")
    print("Answer:", convert_hexadecimal(num, select))
    print("========================================================")
    repeat = input("Would you like to convert another string? (y/n): ") 
    if repeat.lower() == "y":
        hex_menu()
    elif repeat.lower() == "n":
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# function: show main menu 
def main ():
    while True: 
        print("\n")
        print("=========== Welcome to My Conversion Program ===========")
        print("1. Conversion String to ASCII")
        print("2. Conversion Decimal")
        print("3. Conversion Binary")
        print("4. Conversion Octal")
        print("5. Conversion Hexadecimal")
        print("6. Exit")
        print("========================================================")

        # input choice
        choice = get_input("Input your choice: ")
            
        # conversion string to ascii
        if choice == 1:
            string_menu()
                        
        # conversion decimal
        elif choice == 2:
            decimal_menu()
                
        # conversion binary
        elif choice == 3:
            binary_menu()
                
        # conversion octal
        elif choice == 4:
            octal_menu()           
                
        # conversion hexadecimal
        elif choice == 5:
            hex_menu()
            
        elif choice == 6:
            break

        else:
            print("Invalid Input")

main()
