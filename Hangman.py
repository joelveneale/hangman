
from GenerateWord import GenWord
from Guess import Guess
#welcome the user

print("\n--- Welcome to HANGMAN ---\n")

#Generate the word via GenWord
guess_count = 10
word = GenWord()
word.genword()
print(word.word_to_find)




#printing the word for testing purposes


guess = Guess()
guess.runguess(word.letters_to_guess, word.users_empty_guess_list, guess_count)

sys.exit()
