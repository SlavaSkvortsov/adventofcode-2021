from collections import defaultdict


def main() -> None:
    with open('input.txt') as f:
        vents_map = defaultdict(int)

        for line in f.readlines():
            first_point, second_point = line.split(' -> ')
            x1, y1 = [int(coord) for coord in first_point.split(',')]
            x2, y2 = [int(coord) for coord in second_point.split(',')]

            if x1 == x2:
                begin = min(y1, y2)
                for delta in range(abs(y1 - y2) + 1):
                    vents_map[(x1, begin + delta)] += 1
            elif y1 == y2:
                begin = min(x1, x2)
                for delta in range(abs(x1 - x2) + 1):
                    vents_map[(begin + delta), y1] += 1

    result = sum(heat > 1 for heat in vents_map.values())
    print(result)





if __name__ == '__main__':
    main()
