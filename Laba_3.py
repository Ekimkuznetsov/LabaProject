# Task3
import string
import random
import argparse
import logging
from datetime import datetime


# The verbose function to set the level of Logging
def verbose_func(arg):
    if arg == 1:
        logging.basicConfig(level="WARNING")
        print("Level WARNING set")
    elif arg == 2:
        logging.basicConfig(level="INFO")
        print("Level INFO set")
    elif arg == 3:
        logging.basicConfig(level="DEBUG")
    else:
        logging.basicConfig(level="INFO")


# The function to generate tokens list for the password of set length
def set_length(length=10):
    tokens_list = ""
    for i in range(length):
        tokens_list += random.choice(["a", "A", "d"])       #Randome chose from 3 types of tokens

    tokens_list = (tokens_list + "_") * num
    #logging.info(f'tokens_list generated : {tokens_list}') #Logging message
    password_gen(tokens_list)                               #Start of password_gen function with clean list of tokens


#The Function to read lines from the file
def from_file(n):
    file_list = ""
    with open (args.file, "r") as fn:
        lines = fn.readlines()
        for line in lines:
            file_line = line.strip()
            file_list += file_line + "_%"
    #logging.info(f'List of tokens from file generated:  {file_list}')
    return tokens_l(file_list)


#The Function to make raw_tokens list from input
def tokens_l(raw_tokens = "A4%d3%-%a2"):
    template = ""
    #To remove last "%" symbol
    if raw_tokens.endswith("%"):
        template = raw_tokens[:-1]
    else:
        template = raw_tokens
        #logging.info(f'Normal operation going:')
    #To solve "[" case
    if "[" in template:
        a = int(template.index("["))
        b = int(template.index("]"))
        c = template[a + 1 : b]
        d = c.replace("%", "")
        template = template.replace(template[a:b+1], d)
    template = template.split("%")
    #logging.info(f'Template generated:  {template}')
    list_of_tokens(template)


#The Function to create list of tokens from prepared raw_tokens list
def list_of_tokens(template):
    tokens = ["d", "A", "a", "p", "-", "@", "_"]
    tokens_list = []
    global num
    for token in template:
        type_token = ''
        i = 0
        block = ""
        try:
            while token[i] in tokens:
                type_token += token[i]
                i += 1
        except:
            if type_token == '':
                logger.error(f'Wrong template key: {token}')
                print('Wrong template key : ', token)
                break
        try:
            count = int(token[i:])
        except:
            if type_token in tokens:
                count = 1
            else:
                logger.error(f'Wrong template key: {token}')
                print('Wrong template key : ', token)
                break
        if len(type_token) > 1:
            for i in range(count):
                block += random.choice(type_token)
        else:
            block = count * type_token
        tokens_list += block
    tokens_list *= num
    #logger.info(f'List of tokens generated: {tokens_list}')
    password_gen(tokens_list)

#The Function to generate password from the list
def password_gen(tokens_list):

    pas = ''
    for token in tokens_list:
        if token == "a":
            pas += random.choice(list(string.ascii_lowercase))
        elif token == "A":
            pas += random.choice(list(string.ascii_uppercase))
        elif token == "d":
            pas += random.choice(list(string.digits))
        elif token == "p":
            pas += random.choice(list(string.punctuation))
        elif token == "-":
            pas += "-"
        elif token == "@":
            pas += "@"
        elif token == "_":
            pas += "_"
    if "_" in pas:
        pas = pas.replace("_", " ")
    #logging.info(f'Password generated:  {pas}')
    print("Your password(s) is: \n", pas)
    print("Working time: ", datetime.now() - start_time)

#The Function to Parse CLI
def myParser(args):
    verbose_func(args.verbose)
    global num
    num = args.count
    if args.template != None:
        tokens_l(args.template)
    elif args.length != None:
        set_length(args.length)
    elif args.file != None:
        nFile = args.file
        from_file(nFile)
    else:
        logger.warning(f"Ammount of passwords set to 0. <-c> <amount> ")
        print("Ammount of passwords set to 0. <-c> <amount> ")



if __name__ == '__main__':
    # parser runtime
    start_time = datetime.now()
    # logger Initialization
    logger = logging.getLogger()
    # My parser variable
    my_parser = argparse.ArgumentParser()
    #mutually exclusive group created
    my_group = my_parser.add_mutually_exclusive_group(required=False)
    #Arguments set
    my_group.add_argument('-l', '--length', action='store', type=int, help="Set length of the password")
    my_group.add_argument('-t', '--template', action='store', type=str, help="Set password template in format")
    my_group.add_argument('-f', '--file', action='store', type=str, help="Set password from file")
    my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help="Set amount of the passwords")
    my_parser.add_argument('-v', '--verbose', action='count', default=0, help="Different levels of logging -vvv")
    #Execute the parse_args() method
    args = my_parser.parse_args()
    #Start of the program
    myParser(args)




# 1 Template password generation___________done
# 2 Password generation of the set length__done
# 3 Set template for generate passwords____done
# 4 From file _____________________________done
# 5 Number of passwords ___________________done
# 6 Verbose mode __________________________done
# 7 Help __________________________________done
# 8 Logging _______________________________done