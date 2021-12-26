def main() -> None:
    common_bits = None

    with open('input.txt') as f:
        for row in f.readlines():
            if common_bits is None:
                common_bits = [0] * (len(row) - 1)

            for i, bit in enumerate(row[:-1]):
                common_bits[i] += 1 if bit == '1' else -1

    gamma_rate = int(''.join(str(int(bit > 0)) for bit in common_bits), 2)
    epsilon_rate = int(''.join(str(int(bit < 0)) for bit in common_bits), 2)

    print(gamma_rate * epsilon_rate)


if __name__ == '__main__':
    main()
