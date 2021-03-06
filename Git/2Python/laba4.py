import csv
import argparse
import re
# from datetime import datetime
import json

#csv to json conversation
def csv_to_json(args):
    file = args.file.split(',')[0]
    newfile = args.file.split(',')[1] #json file
    data = {} #Dict creation
    # Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        csvReader = csv.DictReader(csv_file, dialect=dialect)
        for rows in csvReader:
            id = rows['id'] #Dict indexing
            data[id] = rows
        # Writing to the new json file
        with open(newfile, 'w') as json_file:
            json_file.write(json.dumps(data, ident=4))
    print('Without header')

# good to make property
def reader_dialected(args):
    file = args.file.split(',')[0]
    # Reader creation
    with open(file) as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))  # To recognise a dialect of csv file
        csv_file.seek(0)  # Move to  the start of the file
        reader = csv.reader(csv_file, dialect)
        return reader


# Function to write csv in ',' format
def without_header(args):
    file = args.file.split(',')[0]
    newfile = args.file.split(',')[1]
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
def header_check(args):
    file = args.file.split(',')[0]
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
    if header_check(args):
        print('With header')
        with_header(args)
    else:
        print('Without header')
        without_header(args)


def row_tables_select(args, delimiter=",", r1=None, r2=None, c1=None, c2=None):
    file = args.file.split(',')[0]
    newfile = args.file.split(',')[1]
    if args.delimiter:
        delimiter = args.delimiter

    with open(file) as source:
        dialect = csv.Sniffer().sniff(source.read(2048))  # To recognise a dialect of csv file
        source.seek(0)  # Move to  the start of the file
        reader = csv.reader(source, dialect)
        with open(newfile, "w") as dest:
            writer = csv.writer(dest, delimiter=delimiter)
            for row in list(reader)[r1:r2]:
                writer.writerow(row[c1:c2])


def extraction(args):
    if args.rows or args.columns:
        if args.rows:
            rows = args.rows.split(',')
            if args.columns:
                columns = args.columns.split(',')
                print('Columns presented')
                row_tables_select(args, r1=int(rows[0]), r2=int(rows[1]), c1=int(columns[0]), c2=int(columns[1]))
            else:
                row_tables_select(args, r1=int(rows[0]), r2=int(rows[1]))
        else:
            columns = args.columns.split(',')
            row_tables_select(args, c1=int(columns[0]), c2=int(columns[1]))
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


def myParser(args):
    if args.filtering:
        filtering(args)

    elif args.extraction:
        extraction(args)
    elif args.json:
        csv_to_json(args)
    else:
        start(args)


if __name__ == "__main__":

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
    my_group.add_argument('-j', '--json', action='store_true', help="To to convert to json format. Outer file should be .json")
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

    1) ???????????????? csv ?? ???????????? ??????????????____done
    2) ???????????? ???? ????????????????_______________done
    3) ???????????? ???? ??????????????________________done
    4) ???????????? ???? ??????????????________________done
    5) ???????????? ???? ????????????_________________done
    6) ??????????????????????______________________done
    7) ????????_____________________________done
    8) json_____________________________done



'''

#by rows [0-9]+(\.[0-9]+){3}

