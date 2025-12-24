import curses
import time

screen = curses.initscr()
run =  True

animation = [
[
[' ',' ',' ','+',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ']
],
[
[' ',' ','+',' ',' '],
[' ',' ','+','+',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ']
],
[
[' ','+',' ',' ',' '],
[' ','+',' ',' ',' '],
[' ','+','+','+',' '],
[' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ']
],
[
['+',' ',' ',' ',' '],
['+',' ',' ',' ',' '],
['+',' ',' ',' ',' '],
['+','+','+','+',' '],
[' ',' ',' ',' ',' ']
]
]

while run:
	screen.clear()
	screen.border()
	for i in range(4):
		screen.clear()
		for y in range(4):
			for x in range(4):
				screen.addstr(y + 5,x + 5,animation[i][y][x])
		screen.refresh()
		time.sleep(0.2)
		
	screen.refresh()
