# Chi Mai

def encode(num_string):
    original_password = ""
    for num in num_string:
        num = int(num)
        num += 3
        num = str(num)
        original_password += num
    return original_password

def decode(num_string):

    # written by Abigail Hennessey

    new_password = ""
    for num in num_string:
        num = int(num)
        num -= 3
        num = str(num)
        new_password -= num
    return new_password

def main():
    menu = '''Menu
    
-------------
1. Encode
2. Decode
3. Quit'''

    while True:
        print(menu)
        option = int(input("\nPlease enter an option: "))

        if option == 1:
            user_password = input("Please enter your password to encode: ")
            encode(user_password)
            print("Your password has been encoded and stored!\n")

        if option == 2:
            user_password = input("Please enter your password to decode: ")
            decode(user_password)
            print("Your password has been decoded and stored!\n")

        elif option == 3:
            break


if __name__ == '__main__':
    main()
