import csv
with open('access_log.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))





if __name__ == "__main__":



 '''

#Файл CSV должен содержать следующие колонки:
#columns = (["MAC address", "hostname",
           "IPv4(null)", "IPv6(null)",
           "netmask(xxx.xxx.xxx.xxx)", "user login",
           "full user name", "email",
           "ssh private key", "ssh public key",
           "description host", "list of installed app",
           "UUID"])
'''