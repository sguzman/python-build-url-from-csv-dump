import csv
import sys
import typing
from typing import List

def assert_cmd(args: List[str]) -> None:
    if len(args) < 2:
        print('usage: <csv-file>')
        sys.exit(1)


def get_csv(args: List[str]) -> str:
    return args[1]

def main() -> None:
    assert_cmd(sys.argv)
    csv_file: str = sys.argv[1]
    
    with open(csv_file) as csv_fd:
        print('Opened file', csv_file, 'succesfully')
        csv_read = csv.reader(csv_fd, delimiter=',', quotechar='"')
        for row in csv_read:
            print(row)
    print('Hello')

if __name__ == '__main__':
    main()
