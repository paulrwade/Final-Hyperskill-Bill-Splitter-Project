import operator


input_string = str(input())

word_list = input_string.lower().split()
word_counts = dict.fromkeys(word_list, 0)

for word in word_list:

    word_counts[word] = word_counts[word] + 1

word_counts_sorted = dict(sorted(word_counts.items(), key=operator.itemgetter(0)))

# print(word_counts_sorted)

for key in word_counts_sorted:
    print(key, word_counts_sorted[key])