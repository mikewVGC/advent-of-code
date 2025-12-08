
banks = []
with open("2025/input/day03", "r") as file:
	banks = file.read().splitlines()

joltage = 0

for bank in banks:
	largest = 0
	largest_index = -1

	# find the biggest number for the first digit
	for i, battery in enumerate(bank[:-1]):
		if int(battery) > largest:
			largest = int(battery)
			largest_index = i

	joltage += 10 * largest

	largest = -1
	# do it again
	for battery in bank[largest_index + 1:]:
		if int(battery) > largest:
			largest = int(battery)

	joltage += largest

print(f"Part 1: {joltage}")


joltage = 0

def find_highest_joltage(bank, digit):
	largest = 0
	largest_index = -1

	end = 1 - digit
	end = None if end == 0 else end

	for i, battery in enumerate(bank[:end]):
		if int(battery) > largest:
			largest = int(battery)
			largest_index = i

	joltage = (10 ** (digit - 1)) * largest

	# print(joltage, 1 - digit, bank[:(1 - digit)])

	if digit - 1 > 0:
		joltage += find_highest_joltage(bank[largest_index + 1:], digit - 1)

	return joltage


for bank in banks:
	joltage += find_highest_joltage(bank, 12)

print(f"Part 2: {joltage}")
