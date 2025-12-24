import matplotlib.pyplot as plt

# Create a figure with custom size, dpi, and background color
plt.figure(figsize=(8, 6), dpi=150, facecolor='lightgray', edgecolor='black')

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, marker='o')

plt.title('Customized Figure')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
