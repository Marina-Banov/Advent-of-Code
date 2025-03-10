f = open("input.txt", 'r')
pixels = list(map(int, list(f.read().strip())))
width = 25
height = 6
layer_size = width * height
layers = zip(*[pixels[i::layer_size] for i in range(layer_size)])
layers = [list(layer) for layer in layers]
image = [[None for i in range(width)] for i in range(height)]

for i in range(height):
    for j in range(width):
        for layer in layers:
            pixel = layer[i*width + j]
            if pixel == 2:
                continue
            image[i][j] = " " if pixel == 0 else "#"
            break

for row in image:
    print("".join(row))
