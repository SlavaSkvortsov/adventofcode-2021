from typing import List, Optional


# def _get_most_common_bit(sorted_lines: List[str], minimum: int, maximum: int, bit_position: int) -> Optional[str]:
#     interval = maximum - minimum + 1
#     mid = (minimum + interval) // 2
#     if interval & 2:  # odd
#         left_bit = sorted_lines[mid][bit_position]
#         right_bit = sorted_lines[mid + 1][bit_position]
#         if left_bit != right_bit:
#             return None
#
#         return left_bit
#     else:  # even
#         return sorted_lines[mid][bit_position]


def _find_border(sorted_lines: List[str], minimum: int, maximum: int, bit_position: int) -> int:
    if minimum == maximum:
        return minimum

    mid = (maximum - minimum) // 2
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


def _extract_rating(sorted_lines: List[str], oxygen: bool = True) -> str:
    minimum = 0
    maximum = len(sorted_lines)

    bit_position = 0
    while minimum != maximum:
        border = _find_border(sorted_lines, minimum, maximum, bit_position)
        interval = maximum - minimum
        even = interval & 2
        mid = interval // 2

        if oxygen:
            if border < mid or even and border == mid:
                minimum = border
            else:  #  border > mid or not even and border == mid
                maximum = border
        else:
            if border < mid or even and border == mid:
                maximum = border
            else:  #  border > mid or not even and border == mid
                minimum = border

        bit_position += 1

    return sorted_lines[minimum]





if __name__ == '__main__':
    common_bits = None

    with open('input.txt') as f:
        sorted_lines = sorted(f.readlines())

    oxygen_rating = int(''.join(_extract_rating(sorted_lines)), 2)
    co2_rating = int(''.join(_extract_rating(sorted_lines, oxygen=False)), 2)

    print(oxygen_rating * co2_rating)
