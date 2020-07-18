import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_list = words.replace("\n", ' ').split(" ")
word_bank = {}

for idx, word in enumerate(word_list):
    if idx < (len(word_list) -2):
        if word not in word_bank:
            word_bank[word] = []
            word_bank[word].append(word_list[idx + 1])
        else:
            word_bank[word].append(word_list[idx + 1])

# pull all of the word_bank keys into a list
dict_keys = list(word_bank.keys())

def getFirstWord():
    # choose a random entry as the start word.
    first_word = random.choice(dict_keys)
    # check to see if the word is a "start word"
    if first_word[0].isupper() or first_word[0] == '"' and first_word[0] is not None:
        return first_word
    else:
       return getFirstWord()

def getRandomWord(start_word):
    rand_word = random.choice(dict_keys[start_word])
    return rand_word

print(getRandomWord(getFirstWord()))
#print(dict_keys)

# TODO: construct 5 random sentences
# Your code here

# Choose a random "start word" to begin.
# * Print the word.
# * If it's a "stop word", stop.
# * Else randomly choose a word that can follow this one.



# Will start with a capital letter, or a " followed by a capital letter.
# print the start word.
# * If it's a "stop word", stop.
# Else, choose a random word from the list associated with the start word key.
# store the values of the start word key in a new variable
# random.choice()
# 