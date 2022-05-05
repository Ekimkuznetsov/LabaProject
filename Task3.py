import string
import random


def genPassword(pTemplate):
    def sList(key):
        list = ''
        for s in key:
            if s == 'a': list += string.ascii_lowercase
            elif s == 'A': list += string.ascii_uppercase
            elif s == 'd': list += string.digits
            elif s == 'p': list += string.punctuation
            elif s == '-': list += '-'
            elif s == '@': list += '@'
        # print('List : ', list)
        return list

    def genPart(list, num):
        p = ''
        for i in range(num): p += random.choice(list)
        # print('password part : ', p)
        return p

    keys = ['A', 'a', 'd', 'p', '-', '@']
    tokenlist = pTemplate.split("%")
    print('Tokens : ', tokenlist)
    password = ''
    for token in tokenlist:
        key = ''
        i = 0
        try:
            while token[i] in keys: key += token[i]; i +=1
        except:
            if key == '': print('Wrong template key : ', token); break
        #print('key is : ', key)
        #print('i = ', i)

        try: n = int(token[i:])
        except:
            if key in keys: n=1
            else: print('Wrong template key : ' ,token); break
        #print('num is : ', n)
        password += genPart(sList(key),n)
    print('Password : ', password)
    return password

if __name__ == 'main':
    #pTemplate = input("Input template: ")
    #pTemplate = 'A4%da3%-%a2%'
    #pTemplate = 'Aa4%@%d3%-%a2%p4%'
    pTemplate = 'Aa6%@%[d%p%]3%-%a2'
    print('Start Template :' , pTemplate)
    find = '['+ pTemplate.partition('[')[2].partition(']')[0] + ']'
    print('Sub template : ', find)
    replace = pTemplate.partition('[')[2].partition(']')[0].replace('%','')
    print('Replace part: ', replace)
    pTemplate = pTemplate.replace(find,replace)
    print('Password template : ', pTemplate)
    genPassword(pTemplate)