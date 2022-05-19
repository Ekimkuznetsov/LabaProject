'''
#For the case if the file not big and it is NO NESTED BRACKETS
#Creating new file object
def dsv_csv():
    converted = StringIO() #FileObject creation
    with open('access-code-password-recovery-code.csv', 'rt') as f:
        converted.write(f.read().replace('(', ']').replace(')', ']').replace('[', ']').replace('"', ']'))
        csv_reader = csv.reader(converted, doublequote=True, delimiter=";", quotechar=']')
    converted.seek(0) #Set the cursor at index 0
    #10 lines print
    count = 1
    for line in csv_reader:
        print(line)
        count += 1
        if count == 10:
            break
'''