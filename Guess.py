

class Guess:


    guess_count = 10
    current_position = ''
    current_wrong = ''

    def get_new_guess(self, word_list, guess_list, guess_count):
        self.wrong_list = []
        while '_' in guess_list and len(self.wrong_list) < guess_count:

            self.users_guess = input("Please Enter a letter A-Z: " + '\n')
            self.users_guess = self.users_guess.upper()
            # print(users_guess)

            for letter in range(len(word_list)):

                if word_list[letter] == self.users_guess:
                    if self.users_guess not in guess_list:
                        guess_list[letter] = word_list[letter]
                        print("You got a letter!!")
                        for letter in guess_list:
                            self.current_position = self.current_position + letter + ' '
                        print(self.current_position + '\n')

                    else:
                        print(self.current_position + '\n')
                        print("You have already entered that letter! Please enter another: \n")

            if self.users_guess not in word_list:
                if self.users_guess not in self.wrong_list:
                    self.wrong_list.append(self.users_guess)
                    print('That letter isn\'t in the word')
                    print('Here are your previous wrong guesses: ')

                    for letter in self.wrong_list:
                        self.current_wrong = self.current_wrong + letter + ' '
                    print(self.current_wrong + '\n')
                else:
                    print("You have already entered that letter! Please enter another: \n")
            # print(current_wrong + '\n')
            # print(current_position + '\n')

        if len(self.wrong_list) == guess_count:
            print("You ran out of guesses you plonker!")
            print("The word was: " + self.letters_to_guess + "!")
        else:
            print('You got the word you legend')



