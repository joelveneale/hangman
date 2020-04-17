
from GenerateWord import GenWord

class Guess:



    current_position = ''
    current_wrong = ''

    def runguess(self, word_list, guess_list, guess_count):
        self.word_list = word_list
        self.guess_list = guess_list
        self.guess_count = guess_count
        self.wrong_list = []
        while '_' in guess_list and len(self.wrong_list) < guess_count:

            self.get_new_guess()
            self.check_guess(word_list, guess_list, self.users_guess)
            self.check_result(guess_count)


    def get_new_guess(self):

            self.users_guess = input("Please Enter a letter A-Z: " + '\n')
            self.users_guess = self.users_guess.upper()
        

            print(self.users_guess)

    def check_guess(self, word_list, guess_list, guess):
        self.guess = guess

        for letter in range(len(word_list)):

            if word_list[letter] == self.guess:
                if self.guess not in guess_list:
                    guess_list[letter] = word_list[letter]
                    print("You got a letter!!")
                    for letter in guess_list:
                        self.current_position = self.current_position + letter + ' '
                    print(self.current_position + '\n')

                else:
                    print(self.current_position + '\n')
                    print("You have already entered that letter! Please enter another: \n")

            if self.guess not in word_list:
                if self.guess not in self.wrong_list:
                    self.wrong_list.append(self.guess)
                    print('That letter isn\'t in the word')
                    print('Here are your previous wrong guesses: ')

                    for letter in self.wrong_list:
                        self.current_wrong = self.current_wrong + letter + ' '
                    print(self.current_wrong + '\n')
                else:
                    print("You have already entered that letter! Please enter another: \n")
                # print(current_wrong + '\n')
                # print(current_position + '\n')

    def check_result(self, count):
        self.count = count
        if len(self.wrong_list) == self.count:
            print("You ran out of guesses you plonker!")
            print("The word was: " + self.letters_to_guess + "!")
        else:
            print('You got the word you legend')



