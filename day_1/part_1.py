def main() -> None:
    result = 0
    previous = None

    with open('input.txt') as f:
        for row in f.readlines():
            current = int(row)

            if previous is not None:
                result += current > previous

            previous = current

    print(result)


if __name__ == '__main__':
    main()
