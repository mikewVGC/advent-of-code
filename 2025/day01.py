
rotations = []
with open("2025/input/day01", "r") as file:
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

print(f"Part 1: {zero_count}")


pos = 50
zero_count = 0

last_pos = 50
for rotation in rotations:
	direction = rotation[:1]
	num = int(rotation[1:])

	# count all full rotations
	zero_count += int(num / 100)

	pos += (num * (1 if direction == "R" else -1))

	if pos > 99 or pos < 0:
		pos %= 100

	went_right_past_zero = direction == "R" and last_pos > 0 and pos < last_pos
	went_left_past_zero = direction == "L" and last_pos > 0 and pos > last_pos
	landed_on_zero = pos == 0

	if landed_on_zero or went_right_past_zero or went_left_past_zero:
		zero_count += 1

	last_pos = pos

print(f"Part 2: {zero_count}")
