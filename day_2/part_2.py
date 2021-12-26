def main() -> None:
    with open('input.txt') as f:
        horizontal, depth, aim = 0, 0, 0

        for row in f.readlines():
            direction, length = row.split()
            length = int(length)

            if direction == 'forward':
                horizontal += length
                depth += length * aim
            elif direction == 'up':
                aim -= length
            elif direction == 'down':
                aim += length

    print(horizontal * depth)


if __name__ == '__main__':
    main()
