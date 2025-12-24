from pyo import *

# Initialize the audio server
s = Server().boot()

# Create a sine wave oscillator
oscillator = Sine(freq=440, mul=0.5)

# Start the audio server
s.start()

# Play the sine wave
oscillator.out()

# Keep the script running to allow the sound to play
s.gui(locals())
