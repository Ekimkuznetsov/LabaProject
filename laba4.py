import csv
import argparse
#import logging
#from datetime import datetime


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


def row_tables_select(fileI='ac.csv', fileO='new_ac.csv', delimiter=",", r1=None, r2=None, c1=None, c2=None):
    print(fileI, fileO, delimiter, r1, r2, c1, c2)
    #files, rows, columns

    with open (fileI) as source:
        with open (fileO, "w") as dest:
            reader = csv.reader(source, delimiter=';')
            writer = csv.writer(dest, delimiter=delimiter)
            for row in list(reader)[r1:r2]:
                writer.writerow(row[c1:c2])

def rows_and_columns(args):
    files = args.file.split(',')
    if args.rows and args.columns:
        rows = args.rows.split(',')
        r1, r2 = int(rows[0]), int(rows[1])
        columns = args.columns.split(',')
        c1, c2 = int(columns[0]), int(columns[1])
        row_tables_select(fileI=files[0], fileO=files[1], delimiter=args.delimiter, r1=r1, r2=r2, c1=c1, c2=c2)
        print(r1, r2, c1, c2)
    elif args.columns:
        columns = args.columns.split(',')
        c1, c2 = int(columns[0]), int(columns[1])
        row_tables_select(fileI=files[0], fileO=files[1], delimiter=args.delimiter, c1=c1, c2=c2)
        print(c1, c2)
    else:
        if args.rows:
            rows = args.rows.split(',')
            r1, r2 = int(rows[0]), int(rows[1])
            row_tables_select(fileI=files[0], fileO=files[1], delimiter=args.delimiter, r1=r1, r2=r2)
            print(r1, r2)

#Check for the arguments
def myParser(args):
    files = args.file.split(',')
    if args.rows or args.columns:
        rows_and_columns(args)
    else:
        if args.delimiter:
            row_tables_select(fileI=files[0], fileO=files[1], delimiter=args.delimiter)
        else:
            row_tables_select(fileI=files[0], fileO=files[1])




if __name__ == "__main__":

    #row_tables_select()
    #start()

    # parser runtime
    #start_time = datetime.now()
    # logger Initialization
    #logger = logging.getLogger()
    # My parser variable
    my_parser = argparse.ArgumentParser()
    # Arguments set
    my_parser.add_argument('-f', '--file', action='store', type=str, help="Source file, destination file", required=True)
    my_parser.add_argument('-d', '--delimiter', action='store', type=str, help="Specify delimiter next way: '\t' for tab, ';' for ';' etc")
    my_parser.add_argument('-r', '--rows', action='store', type=str, help="Specify rows: '1, 2' Use ',' as delimiter ")
    my_parser.add_argument('-c', '--columns', action='store', type=str, help="Specify columns: (Start, Stop) exemple '1, 2' ")

    #Execute the parse_args() method
    args = my_parser.parse_args()
    #Start of the program
    myParser(args)



'''
if __name__ == '__main__':
    

    
    
    1) Записать csv в нужном формате____done
    2) Выбока по столбцам_______________done
    3) Выбока по строкам________________done
    4) Фильтр по столбцу________________
    5) Фильтр по строке_________________
    6) Разделитель______________________
    7) Файл_____________________________done



    my_group.add_argument('-t', '--template', action='store', type=str, help="Set password template in format")
   
    my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help="Set amount of the passwords")
    my_parser.add_argument('-v', '--verbose', action='count', default=0, help="Different levels of logging -vvv")




'''
#Файл CSV должен содержать следующие колонки:
#columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")
