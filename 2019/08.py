def part_one(layers, *_):
    count_zeros = [layer.count(0) for layer in layers]
    min_index = min(range(len(count_zeros)), key=count_zeros.__getitem__)
    return layers[min_index].count(1) * layers[min_index].count(2)


def part_two(layers, width, height):
    image = [['' for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            for layer in layers:
                pixel = layer[i * width + j]
                if pixel == 2:
                    continue
                image[i][j] = " " if pixel == 0 else "#"
                break
    s = ""
    for row in image:
        s = s + "".join(row) + "\n"
    return s


def main(fn):
    with open("input", "r") as f:
        pixels = list(map(int, list(f.read().strip())))
    width = 25
    height = 6
    layer_size = width * height
    layers = zip(*[pixels[i::layer_size] for i in range(layer_size)])
    layers = [list(layer) for layer in layers]
    return fn(layers, width, height)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))
