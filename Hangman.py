import random

words = open("sowpods.txt")
list1 = words.readlines()
hangman_words = []
for item in list1:
    if len(item) > 4:
        hangman_words.append(item)

#defining a function to select a random word from the hangman_words list

def select_random_word(list):
    rand_idx = random.randint(0, len(list))
    return list[rand_idx]


word_to_find = select_random_word(hangman_words)
print(word_to_find)

# adding the letters in the word to a list

def create_list_of_letters(word):
    list_of_letters = []
    for letter in word:
        list_of_letters.append(letter)
    list_of_letters.pop()
    return list_of_letters

letters_to_guess = create_list_of_letters(word_to_find)
print(letters_to_guess)

# creating the empty list for the users guess to be based upon:

def create_empty_guess_list(list):
    empty_list = []
    for letter in list:
        empty_list.append('_')
    return empty_list

users_empty_guess_list = create_empty_guess_list(letters_to_guess)
print(users_empty_guess_list)