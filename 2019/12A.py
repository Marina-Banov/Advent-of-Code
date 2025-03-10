f = open("input.txt", 'r')


def get_xyz(line=None):
    x, y, z = 0, 0, 0
    if line is not None:
        x, y, z = list(map(int, [el.split('=')[1].replace('>', "") for el in line.split(',')]))
    return {'x': x, 'y': y, 'z': z}


moons = []
for line in f:
    moons.append({"pos": get_xyz(line), "vel": get_xyz(), "pot": 0, "kin": 0, "tot": 0})

for step in range(1000):
    for i in range(len(moons)):
        for j in range(i+1, len(moons)):
            for key in ['x', 'y', 'z']:
                if moons[i]["pos"][key] > moons[j]["pos"][key]:
                    moons[i]["vel"][key] -= 1
                    moons[j]["vel"][key] += 1
                elif moons[i]["pos"][key] < moons[j]["pos"][key]:
                    moons[i]["vel"][key] += 1
                    moons[j]["vel"][key] -= 1
        for key in ['x', 'y', 'z']:
            moons[i]["pos"][key] += moons[i]["vel"][key]

tot = 0
for i in range(len(moons)):
    for key in ['x', 'y', 'z']:
        moons[i]["pot"] += abs(moons[i]["pos"][key])
        moons[i]["kin"] += abs(moons[i]["vel"][key])
    moons[i]["tot"] = moons[i]["pot"] * moons[i]["kin"]
    tot += moons[i]["tot"]

print(tot)
