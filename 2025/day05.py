
fresh_ranges = []
ingredients = []
with open("2025/input/day05", "r") as file:
	lines = file.read().splitlines()

	processing = 'ranges'
	for line in lines:
		if len(line) == 0:
			processing = 'ingredients'
			continue

		if processing == 'ranges':
			range_min, range_max = line.split('-')
			fresh_ranges.append([ int(range_min), int(range_max) ])
		elif processing == 'ingredients':
			ingredients.append(int(line))

fresh_count = 0

for ingredient in ingredients:
	for fresh_range in fresh_ranges:
		if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
			fresh_count += 1
			break

print(f"Part 1: {fresh_count}")

# TODO combine ranges with overlap
for i, fresh_range in enumerate(fresh_ranges):
	for k, fr in enumerate(fresh_ranges[i + 1:]):

		# head overlap:
		#      [-R1-----]
		# [-R2----]

		# tail overlap
		# [-R1------]
		#         [-R2---]

		# low range intersects with high range
		head_overlap = True if fresh_range[0] < fr[1] and fresh_range[0] > fr[0] else False
		# high range intersects with low range
		tail_overlap = True if fresh_range[1] > fr[0] and fresh_range[1] < fr[1] else False
