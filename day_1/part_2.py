def main() -> None:
    result = 0
    bucket = [0, 0, 0]
    previous = None

    with open('input.txt') as f:
        for i, row in enumerate(f.readlines()):
            current_value = int(row)

            if previous is None:
                measurement = i % 3
                for j in range(measurement + 1):
                    bucket[j] += current_value

                if measurement == 2:
                    previous = bucket.pop(0)
                    bucket.append(0)

            else:
                for j in range(3):
                    bucket[j] += current_value

                current_window = bucket.pop(0)
                bucket.append(0)
                result += current_window > previous
                previous = current_window


    print(result)


if __name__ == '__main__':
    main()
