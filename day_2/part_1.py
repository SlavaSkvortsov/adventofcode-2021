def main() -> None:
    with open('input.txt') as f:
        horizontal, depth = 0, 0

        for row in f.readlines():
            direction, length = row.split()
            length = int(length)

            if direction == 'forward':
                horizontal += length
            elif direction == 'up':
                depth -= length
            elif direction == 'down':
                depth += length

    print(horizontal * depth)


if __name__ == '__main__':
    main()
