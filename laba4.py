import csv
#from io import StringIO
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

def without_header(file = 'ac.csv', newfile = 'new_ac.csv'): #default files names to simplify
    #Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024)) #To recognise a dialect of csv file
        csv_file.seek(0) #Move to  the start of the file
        reader = csv.reader(csv_file, dialect)

        #Writing to the new file
        with open(newfile, 'w') as new_file:
            csv_writer = csv.writer(new_file)
            for line in reader:
                csv_writer.writerow(line)
                print(line)
    print('Without header')

#check: Is csv file has header
def header_check(file = 'ac.csv'):
    with open(file, 'rt') as csvfile:
        header = csv.Sniffer().has_header(csvfile.read(1024))
        return header

#Function to read and write csv file with header
def with_header(file = 'ac.csv', newfile = 'new_ac.csv'):
    #Header list creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(2048)) #To recognise a dialect of csv file
        csv_file.seek(0) #Move to  the start of the file
        reader = csv.reader(csv_file, dialect)
        header = []
        header = next(reader)
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, dialect=dialect) #Creation of Reader as a dictionary with dialect

        #Creation of Writer as a dictionary with header
        with open(newfile, 'w') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=header)
            csv_writer.writeheader()
            #And writing new csv file
            for line in csv_reader:
                csv_writer.writerow(line)
                #print(line)

    print("List of column names: ", header)


if __name__ == "__main__":
    #dsv_csv()
    if header_check():
        print('With header')
        with_header()

    else:
        print('Without header')
        without_header()

    print("Let's go!")




#Файл CSV должен содержать следующие колонки:
#columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")
