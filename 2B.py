f = open("input.txt", "r")
valid = 0

while True:
    n = f.readline().strip()
    if n == '':
        break
    pos1, password = n.split("-")
    pos2, letter, password = password.split(" ")
    letter = letter.strip(":")
    if password[int(pos1)-1] == letter or password[int(pos2)-1] == letter:
        valid += 1
    if password[int(pos1)-1] == letter and password[int(pos2)-1] == letter:
        valid -= 1

print(valid)
