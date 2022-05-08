# Task3
import string
import random
import argparse
import logging
from datetime import datetime

#logger Initialization
logger = logging.getLogger()

#The verbose function to set the level of Verbosity (Logging)
def verbose_func(loglevel):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')

'''
    if arg == 1:
        getattr(logging, arg.upper())
        print(arg)
    elif arg == 2:
        getattr(logging, arg.upper())
        print(arg)
    elif arg == 3:
        getattr(logging, arg.upper())
        print(arg)
    else:
        getattr(logging, arg.DEBUG)
        print('Verbose mode will be set to level "DEBUG": ')
        print(arg)
'''

#The function to generate tokens list for the password of set length
def set_length(length = 10):
    tokens_list = ""
    #Iteration of every element of length
    for i in range(length):
        tokens_list += random.choice(["a", "A", "d"])       #Randome chose from 3 types of tokens
    logging.debug(f'tokens_list generated : {tokens_list}') #Logging message
    password_gen(tokens_list)                               #Start of password_gen function with clean list of tokens
#The Function to read lines from the file
def from_file(n):
    file_list = ""
    with open (args.file, "r") as fn:
        lines = fn.readlines()
        for line in lines:
            file_line = line.strip()
            file_list += file_line + "_%"
            logging.debug(f'Special symbol _% was meeted: ')
    logging.debug(f'file_list formated:  {file_list}')
    return tokens_l(file_list)


#The Function to make raw_tokens list from input
def tokens_l(raw_tokens = "A4%d3%-%a2"):
    template = []
    #To remove last "%" symbol
    try:
        if raw_tokens.endswith("%"):
            template = raw_tokens[:-1]
    except:
        template = raw_tokens
        logging.info(f'Normal operation going:')
    #To solve "[" and "]" case
    try:
        "[" in template
        a = int(template.index("["))
        b = int(template.index("]"))
        c = template[a + 1 : b]
        d = c.replace("%", "")
        template = template.replace(template[a:b+1], d)
        logging.info(f'There is simple token list:  {template}')
    except:
        logging.info(f'There is simple token list:  {template}')
        #print("There is simple token list")

    template = template.split("%")
    logging.debug(f'There is template to be formated:  {template}')
    list_of_tokens(template)



#The Function to create list of tokens from prepared raw_tokens list
def list_of_tokens(template):
    tokens = ["d", "A", "a", "p", "-", "@", "_"]
    tokens_list = []

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

    logger.warning(f'Ready? tokens_list generated: {tokens_list}')
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
        pas = pas.replace("_", ", ")

    print("Your password is: ", pas)
    print("Working time: ", datetime.now() - start_time)

# parser runtime
start_time = datetime.now()

#Logger initialization


# My parser variable
my_parser = argparse.ArgumentParser()
#mutually exclusive group created
my_group = my_parser.add_mutually_exclusive_group(required=True)
#Arguments set
my_group.add_argument('-l', '--length', action='store', type=int, help="Set length of the password")
my_group.add_argument('-t', '--template', action='store', type=str, help="Set password template")
my_group.add_argument('-f', '--file', action='store', type=str, help="Set password from file")
my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help="Set amount of the passwords")
my_parser.add_argument('-v', '--verbose', action='count', default=2, help="Different levels of logging -vvv")

#Execute the parse_args() method
args = my_parser.parse_args()

#The Function to Parse CLI
def myParser(args):
    if args.count != None:
        if args.verbose != None:
            verbose_func(args.verbose)
            for i in range(args.count):
                if args.template != None:
                    tokens_l(args.template)
                elif args.length != None:
                    set_length(args.length)
                elif args.file != None:
                    n = args.file
                    from_file(n)
                else:
                    logger.warning(f'Ready? tokens_list generated')
        else:
            logger.warning(f"Nothing to show")
            print("Nothing to show")
    else:
        logger.warning(f"Ammount of passwords set to 0. <-c> <amount> ")
        print("Ammount of passwords set to 0. <-c> <amount> ")
#Start of the program
myParser(args)

# 1 Template password generation___________done
# 2 Password generation of the set length__done
# 3 Set template for generate passwords____done
# 4 From file _____________________________done
# 5 Number of passwords ___________________done
# 6 Verbose mode __________________________-
# 7 Help __________________________________
# 8 Logging _______________________________-