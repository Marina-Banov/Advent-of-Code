f = open("input.txt", 'r')
pixels = list(map(int, list(f.read().strip())))
layer_size = 25 * 6
layers = zip(*[pixels[i::layer_size] for i in range(layer_size)])
layers = [list(layer) for layer in layers]
count_zeros = [layer.count(0) for layer in layers]
min_index = min(range(len(count_zeros)), key=count_zeros.__getitem__)
print(layers[min_index].count(1) * layers[min_index].count(2))
