'''
import csv
def write_file(filename, rows, delim=','):
    with open(filename, 'w', encoding='UTF-8-sig', newline='') as f:
        if isinstance((rows[0]), dict):
            csvwriter = csv.DictWriter(f, delimiter=delim, fieldnames=rows[0].keys())
            csvwriter.writeheader()
            csvwriter.writerows(rows)
        else:
            csvwriter = csv.writer(f, delimiter=delim)
            csvwriter.writerows(rows)
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
    my_group.add_argument('-l', '--length', action='store', type=int, help="Set length of the password")
    my_group.add_argument('-t', '--template', action='store', type=str, help="Set password template in format")
    my_group.add_argument('-f', '--file', action='store', type=str, help="Set password from file")
    my_parser.add_argument('-c', '--count', action='store', type=int, default=1, help="Set amount of the passwords")
    my_parser.add_argument('-v', '--verbose', action='count', default=0, help="Different levels of logging -vvv")
    #Execute the parse_args() method
    args = my_parser.parse_args()
    #Start of the program
    myParser(args)