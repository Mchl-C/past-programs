import random
words_list = ["tok darren","se grace","se cynthia"];
word_choice = random.choice(words_list)
found_word = []
for i in range(len(word_choice)):
    found_word.append('_')
    
chances = 7
run = True

while run:
    print("Chances Left : ",chances)
    print("Guess a char...")
    print("Word : ",''.join(found_word))
    print("Input = ",end = ' ')
    n = str(input())[0].lower()
    found = word_choice.find(n)
    print(found)
    if found >= 0:
        found_word[found] = word_choice[found]
    else:
        chances -= 1
