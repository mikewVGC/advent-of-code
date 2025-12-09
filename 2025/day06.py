
import re

columns = {}

operands = []
operators = []
with open("2025/input/day06", "r") as file:
    lines = file.read().splitlines()

    for line in lines[:-1]:
        # this is setup for part 1
        result = re.findall('(\d+) {0,}', line)
        operands.append(list(map(lambda x: int(x), result)))

        # this is setup for part 2
        row = list(line)
        for i, c in enumerate(row):
            if i not in columns:
                columns[i] = ""
            columns[i] += c

    # strip spaces and make a list
    columns = list(map(lambda x: x.strip(), columns.values()))

    # get the operators at the end
    operators = re.findall('([\+\*]{1}) {0,}', lines[len(lines) - 1])

    del lines

num_cols = len(operands[0])

final_answer = 0
for x in range(0, num_cols):
    result = 0 if operators[x] == '+' else 1
    for row in operands:
        if operators[x] == '+':
            result += row[x]
        if operators[x] == '*':
            result *= row[x]

    final_answer += result

print(f"Part 1: {final_answer}")


final_answer = 0
current_op = 0
result = 0 if operators[current_op] == '+' else 1
for i, num in enumerate(columns):
    if num == "":
        final_answer += result
        current_op += 1
        result = 0 if operators[current_op] == '+' else 1
        continue

    if operators[current_op] == '+':
        result += int(num)
    if operators[current_op] == '*':
        result *= int(num)

final_answer += result
    

print(f"Part 2: {final_answer}")
