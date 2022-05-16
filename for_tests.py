#1 Чтение файла в csv---------------------------------------------done
#2 Запись файла в csv---------------------------------------------done
#3 Добавить параметры (path, delimiter, запись в файл)------------
#4 Header: есть или нет. Если есть то пишем Header, если нет, то записываем без хедера


import csv
'''

def convertor_csv(file_location):
    with open(file_location, 'r') as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file, dialect)
        with open('new_ac.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            for line in csv_reader:
                csv_writer.writerow(line)


if __name__ == "__main__":

    convertor_csv('ac.csv')
    print("Let's go!")
'''
#header
with open('ac.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    dict_from_csv = dict(list(csv_reader)[0])
    list_of_column_names = list(dict_from_csv.keys())
    print("List of column names: ", list_of_column_names)
    '''
    with open("new_ac.csv","w") as new_f:
        csv_WRITER = csv.DictWriter(new_f,fieldnames = list_of_column_names)
        for line in csv_READER:
            print(line)
            csv_WRITER.writeheader()
            csv_WRITER.writerow(line)
# opening the csv file by specifying
# the location
# with the variable name as csv_file
with open('ac.csv') as csv_file:
    # creating an object of csv reader
    # with the delimiter as ,
    dialect = csv.Sniffer().sniff(csv_file.read(1024))
    csv_file.seek(0)
    csv_reader = csv.reader(csv_file, dialect)

    # list to store the names of columns
    list_of_column_names = []

    # loop to iterate through the rows of csv
    for row in csv_reader:
        # adding the first row
        list_of_column_names.append(row)

        # breaking the loop after the
        # first iteration itself
        break

# printing the result
print("List of column names : ", list_of_column_names[0])

'''