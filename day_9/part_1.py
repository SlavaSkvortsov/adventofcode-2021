def _parse_line(line: str) -> list[int]:
    return [int(number) for number in line[:-1]]


def _check_area(area: list[list[int]]) -> int:
    return _check_lines(area[1], area[0], area[2])


def _check_lines(check_line: list[int], *adjust_lines: list[int]) -> int:
    result = []

    for i, number in enumerate(check_line):
        adjust_numbers = [adjust_line[i] for adjust_line in adjust_lines]
        if i > 0:
            adjust_numbers.append(check_line[i - 1])
        if i < len(check_line) - 1:
            adjust_numbers.append(check_line[i + 1])

        if all(adjust_number > number for adjust_number in adjust_numbers):
            result.append(number)

    return sum(result) + len(result)


def main() -> None:
    area = []
    result = 0

    with open('input.txt') as f:
        area.append(_parse_line(f.readline()))
        area.append(_parse_line(f.readline()))

        # check first line
        result += _check_lines(*area)

        area.append(_parse_line(f.readline()))
        result += _check_area(area)

        for line in f.readlines():
            area.pop(0)
            area.append(_parse_line(line))
            result += _check_area(area)

        # check last line
        result += _check_lines(area[2], area[1])

    print(result)


if __name__ == '__main__':
    main()
