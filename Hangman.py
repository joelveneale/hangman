import random
import sys

# importing a list of words to choose from

words = open("sowpods.txt")
list1 = words.readlines()
hangman_words = []
for item in list1:
    if len(item) > 4 and len(item) < 12:
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
#print(letters_to_guess)

# creating the empty list for the users guess to be based upon:

def create_empty_guess_list(list):
    empty_list = []
    for letter in list:
        empty_list.append('_')
    return empty_list

users_empty_guess_list = create_empty_guess_list(letters_to_guess)
#print(users_empty_guess_list)

#welcome the user

print("\n--- Welcome to HANGMAN ---\n")




#create a difficulty

guess_count = 10



#create an empty list relative to the amount of wrong letters we will allow the user to select

def get_new_guess(word_list, guess_list, guess_count):
    wrong_list = []
    while '_' in guess_list and len(wrong_list) < guess_count:

      users_guess = input("Please Enter a letter A-Z: " + '\n')
      users_guess = users_guess.upper()
      #print(users_guess)
      for letter in range(len(word_list)):

          if word_list[letter] == users_guess:
              if users_guess not in guess_list:
                  guess_list[letter] = word_list[letter]
                  print("You got a letter!!")
                  current_position = ''
                  for letter in guess_list:
                      current_position = current_position + letter + ' '
                  print(current_position + '\n')
              else:
                  print(current_position + '\n')
                  print("You have already entered that letter! Please enter another: \n")

      if users_guess not in word_list:
          if users_guess not in wrong_list:
              wrong_list.append(users_guess)
              print('That letter isn\'t in the word')
              print('Here are your previous wrong guesses: ')
              current_wrong = ''
              for letter in wrong_list:
                  current_wrong = current_wrong + letter + ' '
              print(current_wrong + '\n')
          else:
              print(current_wrong + '\n')
              print("You have already entered that letter! Please enter another: \n")



    if len(wrong_list) == guess_count:
        print("You ran out of guesses you plonker!")
        print("The word was: " + letters_to_guess + "!")
    else:
        print('You got the word you legend')




get_new_guess(letters_to_guess, users_empty_guess_list, guess_count)
sys.exit()
