from collections import Counter


def _calc(data: Counter[str], check: int) -> int:
    return sum(abs(int(position) - check) * occurrences for position, occurrences in data.items())


def main() -> None:
    with open('input.txt') as f:
        numbers = f.readline().split(',')

    data = Counter(numbers)
    check = data.most_common()[0][1]

    check_left = True  # if we guessed correctly we still need to check left
    result = _calc(data, check)
    while (new := _calc(data, check + 1)) < result:  # checking right
        result = new
        check_left = False
        check += 1

    if check_left:
        while (new := _calc(data, check - 1)) < result:  # checking left
            result = new
            check -= 1

    print(result)
    

if __name__ == '__main__':
    main()
