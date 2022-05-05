# Task3
import string
import random

#Constants. Tokens groups
alphabet_small = list(string.ascii_lowercase)
alphabet_big = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)

#print(alphabet_small)
#print(alphabet_big)
#print(digits_list)
#print(punctuation_list)

# 1 Default password generation
#Function to make tokens_list from raw_tokens
def tokens_l(raw_tokens = "A4%d3%-%a2"):
    tokens = ["d", "A", "a", "p", "-", "@"]
    tokens_list = []

    try:
        if raw_tokens.endswith("%"):
            raw_tokens = raw_tokens[:-1]
    except:
        pass

    try:
        "[" in raw_tokens
        a = int(raw_tokens.index("["))
        b = int(raw_tokens.index("]"))
        print(a, b)
        c = raw_tokens[a + 1 : b]
        print(c)
        d = c.replace("%", "")
        print(d)
        raw_tokens = raw_tokens.replace(raw_tokens[a:b+1], d)
    except:
        pass
    raw_tokens = raw_tokens.split("%")
    print("Raw_tokens: ", raw_tokens)
    for token in raw_tokens:

        type_token = ''
        i = 0
        try:
            while token[i] in tokens: type_token += token[i]; i +=1
        except:
            if type_token == '': print('Wrong template key : ', token); break

        try: count = int(token[i:])
        except:
            if type_token in tokens:
                count = 1
            else: print('Wrong template key : ', token); break
        print('num is : ', count)
#-----------------------------------------------------------------------------
        block = ""
        if len(type_token) > 1:
            for i in range(count):
                if
                block += random.choice(list)
        else:
            block = count * type_token
        tokens_list += block
        print("There is a block: ", block)
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
password_gen(tokens_l("A2%[d%a%]3%-%a2%"))


# 2 Password generation of the set length
# 3 Set template for generate passwords
# 4 From file
# 5 Number of passwords
# 6 Verbose mode
# 7 Help


#A4%d3%-%a2% => DHRF345-st
#A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd
