import csv
from io import StringIO
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
def tsv_csv():
    #with open(file, 'rt') as f:
        #csv_reader = csv.reader(f, doublequote=True, delimiter=";")

    with open('access_log1.csv', 'rt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        header = csv.Sniffer().has_header(csvfile.read(1024))
        print(header)
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        print(dialect)
        for row in reader:
            print(', '.join(row))
    #10 lines print
    #count = 1
    #for line in csv_reader:
        #print(line)
        #count += 1
        #if count == 10:
            #break

if __name__ == "__main__":
    #dsv_csv()
    tsv_csv()
    print("Let's go!")




#Файл CSV должен содержать следующие колонки:
#columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")