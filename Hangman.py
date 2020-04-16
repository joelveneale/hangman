

words = open("sowpods.txt")
list1 = words.readlines()
hangman_words = []
for item in list1:
    if len(item) > 4:
        hangman_words.append(item)



