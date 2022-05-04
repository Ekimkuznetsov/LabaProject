# Task3
import string
import random
import re

alphabet_small = list(string.ascii_lowercase)
alphabet_big = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)

#print(alphabet_small)
#print(alphabet_big)
#print(digits_list)
#print(punctuation_list)
# 1 Default password generation
def raw_gen(format = "A4%d3%-%a2"):
    tokens = ["d", "A", "a", "p", "-", "@"]
    tokens_list = []

    try:
        "[" in format
        a = int(format.index("["))
        b = int(format.index("]"))
        print(a, b)
        c = format[a + 1 : b]
        print(c)

        d = c.replace("%", "")
        print(d)
         =
    except:
        pass


    try:
        if format.endswith("%"):
            format = format[:-1]

    finally:
        raw_tokens = format.split("%")
        print("Raw_tokens: ", raw_tokens)

    for item in raw_tokens:
        try:
            count = int(item[1:])
        except:
            if item[1:] == "":
                count = 1
        try:
            item[0] in tokens
            type_token = item[0]
        except:
            type_token = None
            count = None

        block = type_token * count
        tokens_list += block
        #print("There is a block: ", block)
    print("There is your tokens list: ", tokens_list)
    return(tokens_list)

def password_gen(raw_gen):
    pas = ''
    for token in raw_gen:
        if token == "a":
            pas += random.choice(alphabet_small)
        elif token == "A":
            pas += random.choice(alphabet_big)
        elif token == "d":
            pas += random.choice(digits_list)
        elif token == "p":
            pas += random.choice(punctuation_list)
        elif token == "-":
            pas += "-"
        elif token == "@":
            pas += "@"
        #else: print("Wrong token")
    print("Your password is: ", pas)
password_gen(raw_gen("A4%[d%a%]3%-%a2%"))


# 2 Password generation of the set length
# 3 Set template for generate passwords
# 4 From file
# 5 Number of passwords
# 6 Verbose mode
# 7 Help


#A4%d3%-%a2% => DHRF345-st
#A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd
