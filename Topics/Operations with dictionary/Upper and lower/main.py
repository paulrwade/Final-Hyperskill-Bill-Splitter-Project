# the list with words from string
# please, do not modify it
some_iterable = input().split()
my_dictionary = dict()

for word in some_iterable:
    my_dictionary[word.upper()] = word.lower()

print(my_dictionary)