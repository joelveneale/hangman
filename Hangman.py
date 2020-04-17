from GenerateWord import GenWord
#welcome the user

print("\n--- Welcome to HANGMAN ---\n")

#Generate the word via GenWord
word = GenWord()


word_to_find = word.select_random_word(word.hangman_words)
letters_to_guess = word.create_list_of_letters(word_to_find)
users_empty_guess_list = word.create_empty_guess_list(letters_to_guess)
#print(word_to_find)
#print(letters_to_guess)
#print(users_empty_guess_list)


#create a difficulty
guess_count = 10

#create an empty list relative to the amount of wrong letters we will allow the user to select

def get_new_guess(word_list, guess_list, guess_count):
    wrong_list = []
    while '_' in guess_list and len(wrong_list) < guess_count:

      users_guess = input("Please Enter a letter A-Z: " + '\n')
      users_guess = users_guess.upper()
      #print(users_guess)
      current_position = ''
      current_wrong = ''
      for letter in range(len(word_list)):

          if word_list[letter] == users_guess:
              if users_guess not in guess_list:
                  guess_list[letter] = word_list[letter]
                  print("You got a letter!!")
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

              for letter in wrong_list:
                  current_wrong = current_wrong + letter + ' '
              print(current_wrong + '\n')
          else:
              print("You have already entered that letter! Please enter another: \n")
      #print(current_wrong + '\n')
      #print(current_position + '\n')


    if len(wrong_list) == guess_count:
        print("You ran out of guesses you plonker!")
        print("The word was: " + letters_to_guess + "!")
    else:
        print('You got the word you legend')






get_new_guess(letters_to_guess, users_empty_guess_list, guess_count)
sys.exit()
