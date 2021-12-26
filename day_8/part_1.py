UNIQUE_LENGTH = {2, 3, 4, 7}


def main() -> None:
    result = 0
    with open('input.txt') as f:
        for line in f.readlines():
            _pattern, output = line.split('|')

            for digit in output.split():
                result += len(digit) in UNIQUE_LENGTH

    print(result)


if __name__ == '__main__':
    main()
