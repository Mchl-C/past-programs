value = 0

try:
    with open("sample.txt", 'r') as file:
        content = file.read()
        value = int(content)
        print(value)
except:
    value = 0

while True:
    print("Value :",value)
    print("1. Increase, 2. Decrease, 3. Exit")
    n = int(input("Choice : "))

    if(n == 1 or n == 2):
        num = int(input("Num : "))

    if(n == 1):
        value += num
    elif n == 2:
        value -= num
    else:
        break

with open("sample.txt", 'w') as file:
    file.write(str(value))

