import random
import sys

# importing a list of words to choose from

class GenWord:


    words = open("sowpods.txt")
    list1 = words.readlines()
    hangman_words = []
    for item in list1:
        if len(item) > 4 and len(item) < 12:
            hangman_words.append(item)

    #defining a function to select a random word from the hangman_words list

    def select_random_word(self, list):
        self.rand_idx = random.randint(0, len(list))
        return list[self.rand_idx]


    #word_to_find = select_random_word(hangman_words)
    #print(word_to_find)

    # adding the letters in the word to a list

    def create_list_of_letters(self, word):
        self.list_of_letters = []
        for letter in word:
            self.list_of_letters.append(letter)
        self.list_of_letters.pop()
        return self.list_of_letters

    #letters_to_guess = create_list_of_letters(word_to_find)
    #print(letters_to_guess)

    # creating the empty list for the users guess to be based upon:

    def create_empty_guess_list(self, list):
        self.empty_list = []
        for letter in list:
            self.empty_list.append('_')
        return self.empty_list

    def genword(self):


        self.word_to_find = self.select_random_word(self.hangman_words)
        self.letters_to_guess = self.create_list_of_letters(self.word_to_find)
        self.users_empty_guess_list = self.create_empty_guess_list(self.letters_to_guess)


    #users_empty_guess_list = create_empty_guess_list(letters_to_guess)
    #print(users_empty_guess_list)
