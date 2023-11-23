#letters = {'a', 'b', 'c', 'd', 'e'}

double_alphabet = dict.fromkeys(letters)

for i in double_alphabet.keys():
    double_alphabet[i] = i + i
