#1 Чтение файла в csv---------------------------------------------done
#2 Запись файла в csv---------------------------------------------done
#3 Добавить параметры (path, delimiter, запись в файл)------------
#4 Header


import csv


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

