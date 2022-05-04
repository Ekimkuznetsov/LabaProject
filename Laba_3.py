#Task3

import string
import random

alphabet_small = list(string.ascii_lowercase)
alphabet_big = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)

print(alphabet_small)
print(alphabet_big)
print(digits_list)
print(punctuation_list)

#Length of the password
#Format definition
print("Chouse tokens in the next format A,a,d,p,-,@ with number of their repetitions")

tokens_row = input("Enter your tokens in format A4%d3%-%a2%: ") #Нужно перевести в список
def token_creation(tokens_row):
    tokens_list = tokens_row.split("%")

    print(tokens_list)
    new_tokens = ""
    for simbol in newtokens_list:
        if simbol == "A":
            repetition = simbol
            print(repetition)
            for index in repetition:
                if new_tokens == None:
                    new_tokens = index
                else:
                    new_tokens = new_tokens + index

    print(new_tokens)
token_creation(tokens_row)


tokens = ["p", "d", "d", "d", "A", "A", "A", "a"]
def token(tokens):
    pas = ''
    for index in tokens:
        if index == "a":
            pas += random.choice(alphabet_small)
        elif index == "A":
            pas += random.choice(alphabet_big)
        elif index == "d":
            pas += random.choice(digits_list)
        elif index == "p":
            pas += random.choice(punctuation_list)
        elif index == "-":
            pas += "-"
        elif index == "@":
            pas += "@"
        else: print("Wrong token")
    print(pas)
token(tokens)
'''
a = [a-z]
A = [A-Z]
d = [0-9]
p = punctuation
- = -
@ = @
[ ] set type of token

#A4%d3%-%a2% => DHRF345-st
#A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd
import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)

python -c "from random import choice "
print(''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for i in range(10)]))"


import random as r
c = 'abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)'
print(''.join([c[r.randint(0,len(c)-1)] for i in range(10)]))




import random
num = input('login ')
pas = ''
for x in range(16): #Количество символов (16)
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
print('Hello, ', num, 'your password is: ', pas)

'''