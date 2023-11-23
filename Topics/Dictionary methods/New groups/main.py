number_of_groups = int(input())

groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

total_children = 0

group_sizes = dict.fromkeys(groups)
counter = 0

for i in group_sizes.keys():

    counter += 1

    if counter > number_of_groups:
        break

    group_size = int(input())
    group_sizes[i] = group_size

print(group_sizes)