hp = 5
word = 'liegay'
guess = ['_']*len(word)

while hp > 0:
    print(''.join(guess))
    n = input("Input a single char : ")
    if n in word:
        guess[word.find(n)] = n
        print("correct")
    else:
        hp -= 1
        print("Wrong ans, hp : %i"%hp)

    if(''.join(guess) == word):
        print("You win!")
        print("Hp left : %i"%hp)
        break
    
    print()

if(guess != word):
    print('You lose, ans is : %s'%word)
    
    
