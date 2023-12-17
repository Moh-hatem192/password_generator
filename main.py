import random
import string
characters = string.ascii_letters +  string.digits
special_letters = string.punctuation

def take_length():
    while True:
        try:
            length = int(input('Enter the password length (min is 6): '))
        except ValueError:
            print('Length must be an integer')
            continue 
        if length >= 6:
                return length
        else:
            print('length must be 6 min')            

def create_password(length):
    password = []
    num_special_characters = int(length/2 + length%2)
    for i in range(num_special_characters):
        password.append(random.choice(special_letters))
    for i in range(length - num_special_characters):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ''.join(password) 
    return password

def main():
    length = take_length()
    password = create_password(length)
    print(f'Your generated password is {password}')

if __name__ == '__main__':
    main()
