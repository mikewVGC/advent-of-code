
coords = []
with open("2025/input/day09", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        coords.append(list(map(lambda x: int(x), line.split(','))))

biggest_square = 0
for i, coord in enumerate(coords):
    for k in range(i + 1, len(coords)):
        w = abs(coord[0] - coords[k][0]) + 1
        h = abs(coord[1] - coords[k][1]) + 1

        area = w * h
        if area > biggest_square:
            biggest_square = area

print(f"Part 1: {biggest_square}")
