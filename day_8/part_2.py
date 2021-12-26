from dataclasses import dataclass, field

ALL_SEGMENTS = 'abcdefg'

DISPLAY = {
    1: 'cf',  # 2 (unique)
    7: 'acf',  # 3 (unique)
    4: 'bcdf',  # 4 (unique)
    2: 'acdeg',  # 5
    3: 'acdfg',  # 5
    5: 'abdfg',  # 5
    0: 'abcefg',  # 6
    6: 'abdefg',  # 6
    9: 'abcdfg',  # 6
    8: 'abcdefg',  # 7 (unique)
}

TO_DECODE = {value: key for key, value in DISPLAY.items()}

UNIQUE_LENGTH = {
    2: 1,
    3: 7,
    4: 4,
    # 7: 8,  # it does not give any useful information
}

NOT_UNIQUE_LENGTH = {
    5: {'a', 'd', 'g'},
    6: {'a', 'b', 'f', 'g'},
}


@dataclass
class Display:
    _segments: dict[str, set[str]] = field(init=False)

    def __post_init__(self) -> None:
        self._segments = {segment: set(ALL_SEGMENTS) for segment in ALL_SEGMENTS}

    def add_options(self, segment: str, options: set[str]) -> None:
        self._segments[segment] &= options

    def decode(self) -> dict[str, str]:
        while self._apply_equal_set_rule():
            pass

        if not all(len(options) == 1 for options in self._segments.values()):
            raise Exception('Does not work :(')

        return {options.pop(): segment for segment, options in self._segments.items()}

    def _apply_equal_set_rule(self) -> bool:
        changed = False

        for i, (segment, options) in enumerate(self._segments.items()):
            equal_segments = self._get_equal_segments(options, search_from=i + 1)
            if len(equal_segments) + 1 != len(options):
                continue

            equal_segments.add(segment)
            for edit_segment, edit_options in self._segments.items():
                if edit_segment in equal_segments:
                    continue

                for occupied_segment in options:
                    try:
                        edit_options.remove(occupied_segment)
                    except KeyError:
                        pass
                    else:
                        changed = True

            if changed:
                return True

        return False

    def _get_equal_segments(self, required_options: set[str], search_from: int) -> set[str]:
        result = set()

        for segment, options in list(self._segments.items())[search_from:]:
            if options == required_options:
                result.add(segment)

        return result


def main() -> None:
    result = 0

    with open('input.txt') as f:
        for line in f.readlines():
            display = Display()
            pattern_str, output_str = line.split('|')
            pattern_list = pattern_str.split()
            output_list = output_str.split()

            for pattern in pattern_list:
                if digit := UNIQUE_LENGTH.get(len(pattern)):
                    options = set(pattern)
                    for segment in DISPLAY[digit]:
                        display.add_options(segment, options)

            for length, segments in NOT_UNIQUE_LENGTH.items():
                specific_len_patterns = [pattern for pattern in pattern_list if len(pattern) == length]
                common_segments = set(ALL_SEGMENTS)
                for pattern in specific_len_patterns:
                    common_segments &= set(pattern)

                for segment in segments:
                    display.add_options(segment, common_segments)

            segment_map = display.decode()
            value = ''
            for output_value in output_list:
                mapped_output_value = ''.join(sorted(segment_map[segment] for segment in output_value))
                value += str(TO_DECODE[mapped_output_value])

            result += int(value)

    print(result)


if __name__ == '__main__':
    main()
