import csv
from io import StringIO

converted = StringIO()
with open('access_log1.csv', 'rt') as f:
    converted.write(f.read().replace('(', ']').replace(')', ']').replace('[', ']').replace('"', ']'))
    csv_reader = csv.reader(converted, doublequote=True, delimiter=" ", quotechar=']')

converted.seek(0)
count = 1
for line in csv_reader:
    print(line)
    count += 1
    if count == 10:
        break


if __name__ == "__main__":
    print("Let's go!")




#Файл CSV должен содержать следующие колонки:
#columns = ("MAC address", "hostname", "IPv4(null)", "IPv6(null)", "netmask(xxx.xxx.xxx.xxx)", "user login", "full user name", "email", "ssh private key", "ssh public key", "description host", "list of installed app","UUID")