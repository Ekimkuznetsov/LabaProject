
import csv

with open('ac.csv', 'rt') as f:
    csv_reader = csv.reader(f, doublequote=True, delimiter=";")
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