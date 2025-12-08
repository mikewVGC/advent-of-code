
import re

id_ranges = []
with open("2025/input/day02", "r") as file:
	id_ranges = file.read().split(',')


def number_repeats(number):
	numstr = str(number)
	if len(numstr) % 2 == 1:
		return False

	midpoint = int(len(numstr) / 2)

	if numstr[:midpoint] == numstr[midpoint:]:
		return True

	return False

invalid_count = 0
for id_range in id_ranges:
	start, end = id_range.split('-')
	start = int(start)
	end = int(end)

	for i in range(start, end + 1):
		if number_repeats(i):
			invalid_count += i
	
print(f"Part 1: {invalid_count}")


def number_repeats_any(number):
	numstr = str(number)
	
	# account for a single number repeating
	if len(numstr) > 1 and len(set(numstr)) == 1:
		return True

	# 1 - 3 digit numbers can't pass at this point
	if len(numstr) <= 3:
		return False
	
	# 9 / 2 = 4, will try 4, 3, 2
	# 8 / 2 = 4, will try 4, 3, 2
	# could be more efficient!
	max_sequence_length = int(len(numstr) / 2)

	for chunk_len in range(max_sequence_length, 1, -1):
		# match sequence of chunk_len length
		res = set(re.findall('.{1,' + str(chunk_len) + '}', numstr))
		if len(res) == 1:
			return True

	return False


invalid_count = 0
for id_range in id_ranges:
	start, end = id_range.split('-')
	start = int(start)
	end = int(end)

	for i in range(start, end + 1):
		if number_repeats_any(i):
			invalid_count += i

print(f"Part 2: {invalid_count}")
