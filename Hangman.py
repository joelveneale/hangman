from GenerateWord import GenWord
from Guess import Guess
#welcome the user

print("\n--- Welcome to HANGMAN ---\n")

#Generate the word via GenWord
word = GenWord()
word.genword()
print(word.word_to_find)
guess = Guess()
guess.get_new_guess(word.letters_to_guess, word.users_empty_guess_list, guess.guess_count)









sys.exit()
