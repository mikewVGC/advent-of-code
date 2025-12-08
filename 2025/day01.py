
rotations = []
with open("input/day01", "r") as file:
	rotations = file.read().splitlines()

pos = 50
zero_count = 0

for rotation in rotations:
	direction = rotation[:1]
	num = int(rotation[1:])

	pos += (num * (1 if direction == "R" else -1))

	if pos > 99 or pos < 0:
		pos %= 100

	if pos == 0:
		zero_count += 1

print(zero_count)

	

