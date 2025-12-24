symbol = '*'

n = int(input())

for i in range(n - 2):
    print((n + 1 - i) * ' ', symbol)
    if(i > 0):
        print(((1 + ((i-1) * 2)) * ' ') + symbol)
    else:
        print()
