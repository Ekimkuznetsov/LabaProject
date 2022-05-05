# Task3
import string
import random

#Constants. Tokens groups
alphabet_small = list(string.ascii_lowercase)
alphabet_big = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)
# 1 Default password generation
#Function to make raw_tokens list from input
def tokens_l(raw_tokens = "A4%d3%-%a2"):

    try:
        if raw_tokens.endswith("%"):
            raw_tokens = raw_tokens[:-1]
    except:
        pass

    try:
        "[" in raw_tokens
        a = int(raw_tokens.index("["))
        b = int(raw_tokens.index("]"))
        c = raw_tokens[a + 1 : b]
        d = c.replace("%", "")
        raw_tokens = raw_tokens.replace(raw_tokens[a:b+1], d)
    except:
        pass
    raw_tokens = raw_tokens.split("%")
    #print("Raw_tokens: ", raw_tokens)
    list_of_tokens(raw_tokens)

# Function to create list of tokens from prepared raw_tokens list
def list_of_tokens(raw_tokens):
    tokens = ["d", "A", "a", "p", "-", "@"]
    tokens_list = []
    for token in raw_tokens:
        type_token = ''
        i = 0
        block = ""

        try:
            while token[i] in tokens: type_token += token[i]; i +=1
        except:
            if type_token == '': print('Wrong template key : ', token); break

        try: count = int(token[i:])
        except:
            if type_token in tokens:
                count = 1
            else: print('Wrong template key : ', token); break

        if len(type_token) > 1:
            for i in range(count):
                block = block + random.choice(type_token)
        else:
            block = count * type_token
        tokens_list += block
    #print("There is your tokens list: ", tokens_list)
    password_gen(tokens_list)

#Function to generate password from the list
def password_gen(tokens_list):
    pas = ''
    for token in tokens_list:
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
    print("Your password is: ", pas)

tokens_l("A2%[d%a%]3%-%a2%")


# 2 Password generation of the set length
# 3 Set template for generate passwords
# 4 From file
# 5 Number of passwords
# 6 Verbose mode
# 7 Help


#A4%d3%-%a2% => DHRF345-st
#A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd