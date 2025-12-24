from pyo import *
import time

# Initialize the audio server
s = Server().boot()

def set_up(midi_note, duration):
    freq = 440 * (2 ** ((midi_note - 69) / 12))
    sine = Sine(freq=freq, mul=0.5)
    sine.out()
    time.sleep(duration)

do4, re4, mi4, fa4, sol4, la4, si4 = 60, 62, 64, 65, 67, 69, 71
do5, re5, mi5, fa5, sol5, la5, si5 = 72, 74, 76, 77, 79, 81, 83

melodies = [[mi4, mi4, mi4, (1, mi4, sol4), (2, sol4), fa4, mi4],
            [mi4, (1, mi4, re4), mi4, (1, mi4, sol4), (1.5, sol4), (0.5, fa4), (2, mi4)],
            [mi4, (1, mi4, re4), mi4, (1, mi4, sol4), (1.5, sol4), (0.5, fa4), mi4],
            [mi4, (1, mi4, re4), mi4, (1, mi4, sol4), (1.5, sol4), (0.5, fa4), (2, mi4)],
            [(2, sol4), (2, la4, sol4, fa4, mi4)],
            [(2, fa4), (2, sol4, fa4, mi4, re4), (2, mi4), (1.5, fa4, mi4, re4)],
            [(1.5, re4), (0.5, re4), re4, mi4, fa4, (4, mi4, re4), (2, sol4), (2, la4, sol4, fa4, mi4)],
            [(2, fa4), (2, sol4, fa4, mi4, re4), (2, mi4), (1.5, fa4, mi4, re4)],
            [(1.5, re4), (0.5, re4), re4, mi4, fa4, (4, mi4, re4), (2, do4)]]

s.start()

#s.gui(locals())
speed = 0.5

for line in melodies:
    for i in line:
        if(type(i) == int):
            set_up(i, speed)
        elif(type(i) == tuple):
            temp_speed = speed * i[0] / (len(i) - 1)
            for x in i[1:]:
                set_up(x, temp_speed)
