import csv
#from io import StringIO

#good to make property
def reader_dialected(file='ac.csv'):
    # Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        reader = csv.reader(csv_file, dialect)
        return reader

#Function to write csv in ',' format
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

#Function to chose option with or without header
def start():
    if header_check():
        print('With header')
        with_header()

    else:
        print('Without header')
        without_header()


def row_select(fileI='ac.csv', fileO='new_ac.csv', delimiter=",", start=2, stop=4):
    with open (fileI) as source:
        with open (fileO, "w") as dest:
            reader = csv.reader(source, delimiter=';')
            writer = csv.writer(dest, skipinitialspace=True, delimiter=delimiter)
            for row in list(reader)[start:stop]:
                writer.writerow(row)

def tables_select(fileI='ac.csv', fileO='new_ac.csv', delimiter=",", start=2, stop=4):
    with open (fileI) as source:
        with open (fileO, "w") as dest:
            reader = csv.reader(source, delimiter=';')
            writer = csv.writer(dest, skipinitialspace=True, delimiter=delimiter)
            for row in list(reader):
                writer.writerow(row[start:stop])




if __name__ == "__main__":
    #row_select()
    tables_select()
    #start()
'''
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
    файл Positional argument
    фильтрация опция (столбцы, строки) (диапазон)(выражение(IP))
    Работа с диапазоном, (берем диапазон(столбцы-строки), пишем изменения, возвращаем диапазон)
    Задать разделитель (С каким разделителем сохранить)


    my_group.add_argument('-l', '--length', action='store', type=int, help="Set length of the password")
    my_group.add_argument('-t', '--template', action='store', type=str, help="Set password template in format")
    my_group.add_argument('-f', '--file', action='store', type=str, help="Set password from file")
    my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help="Set amount of the passwords")
    my_parser.add_argument('-v', '--verbose', action='count', default=0, help="Different levels of logging -vvv")
    #Execute the parse_args() method
    args = my_parser.parse_args()
    #Start of the program
    myParser(args)



'''
#Файл CSV должен содержать следующие колонки:
#columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")
