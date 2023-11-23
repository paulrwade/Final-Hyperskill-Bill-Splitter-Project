sum_items = 0
sum_distance = 0

for i in walks:
    sum_distance += int(i['distance'])
    sum_items += 1

mean = int(sum_distance / sum_items)

print(mean)
