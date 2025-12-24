def eat():
    hunger += 5

def sleep():
    fatigue -= 10

def play_game():
    happiness += 10

def stress():
    happiness -= 10

hunger = 50 #max 100
fatigue = 0
happiness = 50

alive = True
while alive:
    eat()
    sleep()
    play_game()
    
