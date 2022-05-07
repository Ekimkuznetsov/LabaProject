# Task3
import string
import random
import argparse
from datetime import datetime


#Constants. Tokens groups
alphabet_small = list(string.ascii_lowercase)
alphabet_big = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)

# 2 Password generation of the set length
#Parameter -l
#The function to generate tokens list for the password of set length
def set_length(length = 10):
    tokens_list = ""
    #Iteration of every element of length
    for i in range(length):
        tokens_list += random.choice(["a", "A", "d"])    #Randome chose from 3 types of tokens
    password_gen(tokens_list)                            #Start of password_gen function with new list of tokens

#function to read lines from the file

def from_file(n):
    file_list = ""
    with open (args.file, "r") as fn:
        lines = fn.readlines()
        for line in lines:
            file_line = line.strip()

            file_list += file_line + "_%"
    #print(file_list)

    tokens_l(file_list)

# 1 Template password generation
#Function to make raw_tokens list from input
def tokens_l(raw_tokens = "A4%d3%-%a2"):
    #To remove last "%" symbol
    try:
        if raw_tokens.endswith("%"):
            raw_tokens = raw_tokens[:-1]
    except:
        pass
    #To solve "[""]" case
    try:
        "[" in raw_tokens
        a = int(raw_tokens.index("["))
        b = int(raw_tokens.index("]"))
        c = raw_tokens[a + 1 : b]
        d = c.replace("%", "")
        raw_tokens = raw_tokens.replace(raw_tokens[a:b+1], d)
    except:
        pass
        #print("There is simple token list")

    raw_tokens = raw_tokens.split("%")
    #print("Raw_tokens: ", raw_tokens)
    list_of_tokens(raw_tokens)



# Function to create list of tokens from prepared raw_tokens list
def list_of_tokens(raw_tokens):
    tokens = ["d", "A", "a", "p", "-", "@", "_"]
    tokens_list = []
    for token in raw_tokens:
        type_token = ''
        i = 0
        block = ""

        try:
            while token[i] in tokens:
                type_token += token[i]
                i += 1
        except:
            if type_token == '':
                print('Wrong template key : ', token)
                break
        try:
            count = int(token[i:])
        except:
            if type_token in tokens:
                count = 1
            else:
                print('Wrong template key : ', token)
                break

        if len(type_token) > 1:
            for i in range(count):
                block += random.choice(type_token)
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
        elif token == "_":
            pas += "_"

    print("Your password is: ", pas)
    print("Working time: ", datetime.now() - start_time)

#tokens_l("A2%[d%a%]3%-%a2%")

# Create the parser
start_time = datetime.now()

my_parser = argparse.ArgumentParser()
# - l: Set length of password and generate random password from set {small lateral ASCII, big lateral ASCII,
# digit}




#mutually exclusive group created
my_group = my_parser.add_mutually_exclusive_group(required=True)

my_group.add_argument('-l', '--length', action='store', type=int, help= "Set length of the password")
my_group.add_argument('-t', '--template', action='store', type=str, help=" Set password template")
my_group.add_argument('-f', '--file', action='store', type=str, help="Set password from file")
my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help= "Set amount of the passwords")
#my_parser.add_argument('-vvv', '--verbose', action='store', type=int, help= "Set length of the password")

#Execute the parse_args() method
args = my_parser.parse_args()

#the function to Parse CLI
def myParser(args):
    if args.count != None:
        for i in range(args.count):
            if args.template != None:
                tokens_l(args.template)
            elif args.length != None:
                set_length(args.length)
            elif args.file != None:
                n = args.file
                from_file(n)


            else:
                pass

myParser(args)
# 3 Set template for generate passwords____done
# 4 From file



# 5 Number of passwords __________________ done
# 6 Verbose mode


# 7 Help


#A4%d3%-%a2% => DHRF345-st
#A4%[d%a%]3%-%a2% => DHRF3s4-st | FHGFds4-vt | DERS774-sd