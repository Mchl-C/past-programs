from pyo import *

# Start the Pyo server
s = Server().boot()
s.start()

# Define the frequencies for the notes of the C major chord
c_freq = 261.63  # C note frequency
e_freq = 329.63  # E note frequency
g_freq = 392.00  # G note frequency

# Define the frequencies for the notes of the F major chord
f_freq = 349.23  # F note frequency
a_freq = 440.00  # A note frequency
c_freq_high = 523.25  # High C note frequency

# Define the frequencies for the notes of the G major chord
g_freq = 392.00  # G note frequency
b_freq = 493.88  # B note frequency
d_freq_high = 587.33  # High D note frequency

# Create sine wave oscillators for each note of the C major chord
c_note = Sine(freq=c_freq, mul=0.5)
e_note = Sine(freq=e_freq, mul=0.5)
g_note = Sine(freq=g_freq, mul=0.5)

# Create sine wave oscillators for each note of the F major chord
f_note = Sine(freq=f_freq, mul=0.5)
a_note = Sine(freq=a_freq, mul=0.5)
c_note_high = Sine(freq=c_freq_high, mul=0.5)

# Create sine wave oscillators for each note of the G major chord
g_note = Sine(freq=g_freq, mul=0.5)
b_note = Sine(freq=b_freq, mul=0.5)
d_note_high = Sine(freq=d_freq_high, mul=0.5)

# Combine the oscillators to create the chords
c_chord = c_note + e_note + g_note
f_chord = f_note + a_note + c_note_high
g_chord = g_note + b_note + d_note_high

# Play the chord progression
c_chord.out()
time.sleep(2)  # Wait for 2 seconds before playing the next chord
f_chord.out()
time.sleep(2)
g_chord.out()

# Keep the script running

