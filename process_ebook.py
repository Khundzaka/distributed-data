# Open file
# Read content from stream
# Split into lines
# split lines in words
# count occurrences of words in document

# File URL: https://www.gutenberg.org/cache/epub/36099/pg36099.txt

file = open('pg36099.txt', 'r')

content = file.read()

lines = content.split("\n")

# for i in range(11, 7, -1):
#     print(i)

words_map = {}

for line in lines:
    if len(line) > 0:
        words = []
        for word in line.split(" "):
            if len(word) > 0:
                words.append(word)
        for word in words:
            if word.lower() in words_map.keys():
                words_map[word.lower()] += 1
            else:
                words_map[word.lower()] = 1

value = ''
count = 0

for word in words_map.keys():
    if words_map[word] > count:
        count = words_map[word]
        value = word

# print(value)
# print(count)

# print(sorted(words_map.keys()))

result = {k: v for k, v in sorted(words_map.items(), key=lambda x: x[1])}

print(list(result.items())[-1]) # the most used word in e-book

# a = [1,2,3,4]

# print(a[:-2])