def main() -> None:
    with open('input.txt') as f:
        fish_list = f.readline().split(',')

    ocean = [0] * 9
    for fish in fish_list:
        ocean[int(fish)] += 1

    for i in range(80):
        spawned = ocean.pop(0)
        ocean[6] += spawned
        ocean.append(spawned)

    result = sum(ocean)
    print(result)


if __name__ == '__main__':
    main()
