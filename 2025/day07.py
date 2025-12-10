
tree = []
with open("2025/input/day07", "r") as file:
    tree = file.read().splitlines()

def beam_down():
    ...

start = -1
for x, tile in enumerate(tree[0]):
    if tile == 'S':
        start = x
        break

max_y = len(tree) - 1
max_x = len(tree[0]) - 1

split_count = 0

# using a dict to dedupe because you can't make a set of lists
beam_ends = { f"{start}-0": [ start, 0 ] }

while True:
    for i, beam_end in enumerate(beam_ends):
        [ x, y ] = beam_ends[beam_end]

        # move the beam down

        # we reached the bottom
        if y + 1 > max_y:
            del beam_ends[beam_end]
            break

        # move the beam!
        if tree[y + 1][x] == '.':
            beam_ends[f"{x}-{y + 1}"] = [ x, y + 1 ]
            del beam_ends[beam_end]
            break

        # we hit a splitter
        if tree[y + 1][x] == '^':
            if x - 1 >= 0:
                beam_ends[f"{x - 1}-{y + 1}"] = [ x - 1, y + 1 ]
            if x + 1 < max_x:
                beam_ends[f"{x + 1}-{y + 1}"] = [ x + 1, y + 1 ]
            split_count += 1
            del beam_ends[beam_end]
            break

    if len(beam_ends) == 0:
        break

print(f"Part 1: {split_count}")

