import csv

def main():
    x = ['sn', 'pid', 'ip']
    dict = [{'sn': '101',
            'pid': 'ws01',
            'ip': '1.1.1.1'},
            {'sn': '102',
            'pid': 'ws02',
            'ip': '1.1.1.2'},
            {'sn': '104',
             'pid': 'ws03',
             'ip': '1.1.1.3'}
            ]

    with open('test.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=x, lineterminator='\n', delimiter=';')
        writer.writeheader()
        writer.writerows(dict)


if __name__ == '__main__':
    main()