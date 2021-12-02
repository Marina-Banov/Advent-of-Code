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


public_a, public_b = map(int, input().strip().split())
print(decrypt(public_b, get_private_key(public_a)))
