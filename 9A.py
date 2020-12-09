def is_sum_of_two(n, preamble):
    s = set()
    for i in range(25):
        temp = n - preamble[i]
        if temp in s:
            return True
        s.add(preamble[i])
    return False


def main():
    f = open("input.txt", "r").read().strip().split()
    numbers = list(map(int, f))

    for i in range(25, len(numbers)):
        if not is_sum_of_two(numbers[i], numbers[i-25:i]):
            print(numbers[i])
            break


if __name__ == '__main__':
    main()
