import sys
import typing
from typing import List

def assert_cmd(args: List[str]) -> None:
    if len(args) < 2:
        print('usage: <csv-file>')
        sys.exit(1)


def main() -> None:
    print("Hello")

if __name__ == '__main__':
    main()
