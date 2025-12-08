
grid = []
with open("2025/input/day04", "r") as file:
	lines = file.read().splitlines()
	for line in lines:
		grid.append(list(line))

max_y = len(grid) - 1
max_x = len(grid[0]) - 1

def get_adjacent_roll_count(y, x):
	adjacent_count = 0
	for y_check in range(-1, 2):
		for x_check in range(-1, 2):
			if y_check == x_check == 0:
				continue
			if y + y_check > max_y or y + y_check < 0:
				continue
			if x + x_check > max_x or x + x_check < 0:
				continue

			if grid[y + y_check][x + x_check] == '@':
				adjacent_count += 1

	return adjacent_count


accessable_spots = set()

for y, row in enumerate(grid):
	for x, tile in enumerate(row):

		if tile == '.':
			continue

		adjacent_count = get_adjacent_roll_count(y, x)

		if adjacent_count < 4:
			accessable_spots.add((x, y))

print(f"Part 1: {len(accessable_spots)}")


total_removed = 0

while True:
	accessable_spots = set()

	for y, row in enumerate(grid):
		for x, tile in enumerate(row):

			if tile == '.':
				continue

			adjacent_count = get_adjacent_roll_count(y, x)

			if adjacent_count < 4:
				accessable_spots.add((y, x))

	# no more rolls can be moved
	if len(accessable_spots) == 0:
		break

	# remove the roll
	for spot in accessable_spots:
		grid[spot[0]][spot[1]] = '.'
		total_removed += 1

print(f"Part 2: {total_removed}")

