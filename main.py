# Ian Zhou
def encode(password):
    return ''.join(str(int(i) + 3) if int(i) < 7 else str(int(i) - 7) for i in password)


def decode(password):
    return ''.join(str(int(i) - 3) if int(i) > 2 else str(int(i) + 7) for i in password)


def main():
    while True:
        option = int(input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored!\n')
        if option == 2:
            print(f'The encoded password is {encoded}, and the original password is {password}.\n')
        if option == 3:
            break


if __name__ == '__main__':
    main()
