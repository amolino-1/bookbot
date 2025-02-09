my_string = "the QUICK brown fox jumped over the lazy dog."

my_dict = {}

words = my_string.lower()

for word in words:
    my_dict[word] = 0

for word in words:
    my_dict[word] += 1

print(my_dict)
