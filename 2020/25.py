def get_private_key(public):
    private = 0
    init = 1
    while init != public:
        private += 1
        init *= 7
        init %= 20201227
    return private


def decrypt(public, private):
    init = 1
    for i in range(private):
        init *= public
        init %= 20201227
    return init


def part_one(public_a, public_b):
    return decrypt(public_b, get_private_key(public_a))


def part_two(_public_a, _public_b):
    return


def main(fn):
    with open("input", "r") as f:
        public_a, public_b = map(int, [line.strip() for line in f.readlines()])
    return fn(public_a, public_b)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))
