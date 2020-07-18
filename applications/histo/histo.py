# Your code here

# Read from the file.
with open("robin.txt") as f:
    words = f.read()

word_list = words.split(' ')
# create a hash table
histogram = {}

# iterate through the word list and make each word the key, and the value a list
# if the word is in the hash table already, add a hash symbol to the value list.

for word in word_list:
    if word.lower() not in histogram:
        histogram[word.lower()] = '#'
    else:
        histogram[word.lower()] += '#'

frequency = list(histogram.items())
frequency.sort(key=lambda x: x[1], reverse=True)

for key, value in frequency:
    print(f'{key:} {value}')