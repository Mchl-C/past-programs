hp = 5
word = 'dancer'
thespaces = '_'*len(word)

while hp > 0:
    print(thespaces)
    n = input("Guess a char: ")

    found = False
    for i in range(len(word)):
        if(word[i] == n):
            thespaces = thespaces[:i] + n + thespaces[i+1:]
            found = True

    if not found:
        hp -= 1
        print("You lose one of your body part")


if(word != thespaces):
    print("You lose completely")
else:
    print("You win")
