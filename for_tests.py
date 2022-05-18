def write_file(filename, rows, delim=','):
    with open(filename, 'w', encoding='UTF-8-sig', newline='') as f:
        if isinstance((rows[0]), dict):
            csvwriter = csv.DictWriter(f, delimiter=delim, fieldnames=rows[0].keys())