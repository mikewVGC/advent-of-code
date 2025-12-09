
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


while True:
    changes_found = False

    # TODO combine ranges with overlap
    for i, fresh_range in enumerate(fresh_ranges):

        new_min = -1
        new_max = -1

        for k, fr in enumerate(fresh_ranges):
            if k <= i:
                continue

            # head overlap:
            #      [-R1-----]
            # [-R2----]

            # tail overlap
            # [-R1------]
            #         [-R2---]

            # full overlap (delete R2)
            # [-R1-------]
            #  [-R2---]

            # full underlap (delete R1)
            #   [-R1---]
            # [-R2------]

            # low range intersects with high range
            head_overlap = True if fresh_range[0] <= fr[1] and fresh_range[0] >= fr[0] else False
            # high range intersects with low range
            tail_overlap = True if fresh_range[1] >= fr[0] and fresh_range[1] <= fr[1] else False

            full_overlap = True if fresh_range[0] <= fr[0] and fresh_range[1] >= fr[1] else False
            full_underlap = True if fresh_range[0] >= fr[0] and fresh_range[1] <= fr[1] else False

            if head_overlap or tail_overlap:
                new_min = min(fresh_range[0], fr[0])
                new_max = max(fresh_range[1], fr[1])
                break

            if full_overlap:
                del fresh_ranges[k]
                changes_found = True
                break

            if full_underlap:
                del fresh_ranges[i]
                changes_found = True
                break

        # if we found overlap, delete the originals and insert a new one
        if new_min > 0 and new_max > 0:
            fresh_ranges[i] = [ new_min, new_max ]
            del fresh_ranges[k]
            changes_found = True

        if changes_found == True:
            break

    # keep going until we are out of overlaps
    if changes_found == False:
        break


fresh_count = 0
for fresh_range in fresh_ranges:
    fresh_count += (fresh_range[1] - fresh_range[0] + 1)

print(f"Part 2: {fresh_count}")
