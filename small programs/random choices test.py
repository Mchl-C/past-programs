import random

total_average = 0
for x in range(10):
    lst = []
    for i in range(10):
        n = 0
        total = 0

        while n < 1:
            b = random.choices([0,1],weights = [99,1],k = 1)
            if(int(b[0]) == 1):
                n += 1
            total += 1

        lst.append(total)

    print(lst)

    average = 0
    for i in range(len(lst)):
        average += lst[i]

    average /= len(lst)
    print("Average : ",average)
    print()
    total_average += average

total_average /= 10
print("Total Average : ",total_average)
