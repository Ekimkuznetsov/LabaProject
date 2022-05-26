import csv
import argparse
import re
# from datetime import datetime


# good to make property
def reader_dialected(file='ac.csv'):
    # Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        reader = csv.reader(csv_file, dialect)
        return reader


# Function to write csv in ',' format
def without_header(file='ac.csv', newfile='new_ac.csv'):  # default files names to simplify
    # Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        reader = csv.reader(csv_file, dialect)

        # Writing to the new file
        with open(newfile, 'w') as new_file:
            csv_writer = csv.writer(new_file)
            for line in reader:
                csv_writer.writerow(line)
    print('Without header')


# check: Is csv file has header
def header_check(file='ac.csv'):
    with open(file, 'rt') as csvfile:
        header = csv.Sniffer().has_header(csvfile.read(1024))
        return header


# Function to read and write csv file with header
def with_header(args):
    file = args.file.split(',')[0]
    newfile = args.file.split(',')[1]
    # Header list creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(2048))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        reader = csv.reader(csv_file, dialect)
        header = next(reader)
        print(header)
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file, dialect=dialect)  # Creation of Reader as a dictionary with dialect
        print(list(csv_reader))

        # Creation of Writer as a dictionary with header
        with open(newfile, 'w') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=header, skipinitialspace=True)
            # And write new csv file
            csv_file.seek(0)
            count = 0
            for line in csv_reader:
                if count == None:
                    count += 1
                    continue
                else:
                  csv_writer.writerow(line)
                print(line)

    print("List of column names: ", header)


# Function to chose option with or without header
def start(args):
    if header_check():
        print('With header')
        with_header(args)

    else:
        print('Without header')
        without_header(args)


def row_tables_select(args, delimiter=",", r1=None, r2=None, c1=None, c2=None):
    file = args.file.split(',')[0]
    print(file)
    newfile = args.file.split(',')[1]
    print(newfile)
    if args.delimiter:
        delimiter = args.delimiter
    print(r1, r2, c1, c2)
    with open(file) as source:
        dialect = csv.Sniffer().sniff(source.read(2048))  # To recognise a dialect of csv file
        source.seek(0)  # Move to  the start of the file
        reader = csv.reader(source, dialect)
        with open(newfile, "w") as dest:
            writer = csv.writer(dest, delimiter=delimiter)
            print("wtf")
            print(reader)
            for row in list(reader)[r1:r2]:
                print("row")
                writer.writerow(row[c1:c2])


def extraction(args):
    if args.rows or args.columns:
        if args.rows:
            print("rows is", args.rows)
            rows = args.rows.split(',')
            print(rows)
            if args.columns:
                columns = args.columns.split(',')
                print('Columns presented')
                row_tables_select(args, r1=int(rows[0]), r2=int(rows[1]), c1=int(columns[0]), c2=int(columns[1]))
            else:
                row_tables_select(args, r1=int(rows[0]), r2=int(rows[1]))
        else:
            columns = args.columns.split(',')
            row_tables_select(args, c1=int(columns[0]), c2=int(columns[1]))
            print('c1, c2')
    else:
        row_tables_select(args)


def filtering(args):
    c1 = int(args.columns.split(',')[0])
    c2 = int(args.columns.split(',')[1])
    params = args.pattern.split(',')
    files = args.file.split(',')
    pattern = str(params[1])
    with open(files[0]) as source:
        dialect = csv.Sniffer().sniff(source.read(1024))  # To recognise a dialect of csv file
        source.seek(0)  # Move to  the start of the file
        reader = csv.reader(source, dialect)
        with open(files[1], "w") as dest:
            writer = csv.writer(dest)
            if params[0] == 'c':
                for row in list(reader):
                    string = ' '.join(row[c1:c2])
                    #print(string)
                    if re.search(pattern, string):
                        writer.writerow(row[c1:c2])
                        print('Mutch')
                    else:
                        print('Dont mutch1')
                        pass
            elif params[0] == 'r':
                for row in list(reader):
                    string = ','.join(row)
                    if re.search(pattern, string):
                        writer.writerow(row)
                    else:
                        print('Dont mutch')
                        pass

#by rows [0-9]+(\.[0-9]+){3}


def myParser(args):
    if args.filtering:
        filtering(args)

    elif args.extraction:
        extraction(args)
    else:
        start(args)


if __name__ == "__main__":
    # row_tables_select()
    # start()

    # parser runtime
    # start_time = datetime.now()
    # logger Initialization
    # logger = logging.getLogger()
    # My parser variable
    my_parser = argparse.ArgumentParser()
    # creation of mutually exclusive group
    my_group = my_parser.add_mutually_exclusive_group(required=False)
    my_group.add_argument('-e', '--extraction', action='store_true',
                          help="Extract special columns or rows. Used with -c, -r")
    my_group.add_argument('-s', '--filtering', action='store_true', help="To use filter through a file. Used with -p")

    my_parser.add_argument('-p', '--pattern', action='store', type=str,
                           help="Pattern to look for in format c(or r),regex")
    my_parser.add_argument('-f', '--file', action='store', type=str, help="Source file, destination file",
                           required=True)
    my_parser.add_argument('-d', '--delimiter', action='store', type=str,
                           help="Specify delimiter next way: '\t' for tab, ';' for ';' etc")
    my_parser.add_argument('-r', '--rows', action='store', type=str, help="Specify rows: '1, 2' Use ',' as delimiter ")
    my_parser.add_argument('-c', '--columns', action='store', type=str,
                           help="Specify columns: (Start, Stop) exemple '1, 2' ")

    # Execute the parse_args() method
    args = my_parser.parse_args()
    # Start of the program
    # myParser
    myParser(args)

'''


    #Arguments set

    1) Записать csv в нужном формате____done
    2) Выбока по столбцам_______________done
    3) Выбока по строкам________________done
    4) Фильтр по столбцу________________done
    5) Фильтр по строке_________________done
    6) Разделитель______________________done
    7) Файл_____________________________done
    8) json_____________________________



'''
# Файл CSV должен содержать следующие колонки:
# columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")


