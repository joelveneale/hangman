
from GenerateWord import GenWord

class Guess:

    def runguess(self, word_list, guess_list, guess_count):
        self.word_list = word_list
        self.guess_list = guess_list
        self.guess_count = guess_count
        self.wrong_list = []

        while '_' in guess_list and len(self.wrong_list) < guess_count:

            self.get_new_guess()
            self.check_guess(word_list, guess_list, self.users_guess, self.wrong_list)

            if self.guess in guess_list:
                self.print_current()

            elif self.guess not in guess_list:
               self.print_wrong()

            self.check_result(guess_count)
            guess_count = guess_count - 1


    def get_new_guess(self):
            self.users_guess = input("Please Enter a letter A-Z: " + '\n')
            self.users_guess = self.users_guess.upper()
            print("You entered the letter: " + self.users_guess)

    def check_guess(self, word_list, guess_list, guess, wrong_list):
        self.guess = guess
        self.wrong_list = wrong_list
        self.guess_list = guess_list

        for letter in range(len(word_list)):
            if word_list[letter] == self.guess:
                guess_list[letter] = word_list[letter]

        if self.guess not in word_list:
            if self.guess not in self.wrong_list:
                self.wrong_list.append(self.guess)

    def print_current(self):
        current_position = ''
        current_wrong = ''
        if self.guess_list:
            print('This is your current position: ')
            for letter in self.guess_list:
                current_position = current_position + letter + ' '
            print(current_position + '\n')
        if self.wrong_list:
            print('Here are your previous wrong guesses: ')
            for letter in self.wrong_list:
                current_wrong = current_wrong + letter + ' '
            print(current_wrong + '\n')

    def print_wrong(self):
        current_position = ''
        current_wrong = ''
        if self.wrong_list:
            print('That letter isn\'t in the word')
            print('Here are your previous wrong guesses: ')
            for letter in self.wrong_list:
                current_wrong = current_wrong + letter + ' '
            print(current_wrong + '\n')
        if self.guess_list:
            print('This is your current position: ')
            for letter in self.guess_list:
                current_position = current_position + letter + ' '
            print(current_position + '\n')

    def check_result(self, count):
        self.count = count

        if len(self.wrong_list) == self.count:
            print("You ran out of guesses you plonker!")
            print("The word was: " + self.letters_to_guess + "!")
        elif self.guess_list == self.word_list:
            print('You got the word you legend! Well done. ')
        else:
            pass

