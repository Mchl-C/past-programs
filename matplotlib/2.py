import matplotlib.pyplot as plt

y1 = [1, 4, 9, 16, 25, 36]
y2 = [1, 8, 27, 16, 125, 36]
y3 = [1,2,3,4,5,6]
y4 = [5,4,3,2,1]

fig, axs = plt.subplots(4, 1)

print(fig, axs)

axs[0].plot(y1)
axs[0].set_title('First Plot')

axs[1].plot(y2)
axs[1].set_title('Second Plot')

axs[2].plot(y3)
axs[2].set_title("third")

axs[3].plot(y4)
axs[3].set_title("fourth")

plt.tight_layout()

plt.show()
