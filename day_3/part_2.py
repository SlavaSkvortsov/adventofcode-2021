from typing import List


def _find_border(sorted_lines: List[str], minimum: int, maximum: int, bit_position: int) -> int:
    if minimum + 1 == maximum:
        return minimum

    mid = (maximum - minimum + 1) // 2 + minimum
    bit = sorted_lines[mid][bit_position]
    if bit == '0':
        return _find_border(
            sorted_lines=sorted_lines,
            minimum=mid,
            maximum=maximum,
            bit_position=bit_position
        )
    else:
        return _find_border(
            sorted_lines=sorted_lines,
            minimum=minimum,
            maximum=mid,
            bit_position=bit_position
        )


def _extract_rating(sorted_lines: List[str], invert: bool = False) -> str:
    minimum = 0
    maximum = len(sorted_lines)

    bit_position = 0
    while minimum + 1 != maximum:
        border = _find_border(sorted_lines, minimum, maximum, bit_position)

        zeros = border - minimum + 1
        ones = maximum - minimum - zeros

        if zeros > ones:
            pick_top = True
        elif zeros < ones:
            pick_top = False
        else:
            pick_top = False

        if invert:
            pick_top = not pick_top

        if pick_top:
            maximum = border + 1
        else:
            minimum = border + 1

        bit_position += 1

    return sorted_lines[minimum]


if __name__ == '__main__':
    common_bits = None

    with open('input.txt') as f:
        sorted_lines = sorted(f.readlines())

    oxygen_rating = int(''.join(_extract_rating(sorted_lines)), 2)
    co2_rating = int(''.join(_extract_rating(sorted_lines, invert=True)), 2)

    print(oxygen_rating * co2_rating)
