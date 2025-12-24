import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create the plot
plt.plot(x, y, color='green', marker='o', linestyle='--')

plt.title('Customized Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
