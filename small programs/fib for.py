arr = []
n = int(input())

for i in range(1,n + 1,1):
    if(i <= 2):
        arr.append(1)
    else:
        arr.append(arr[i - 2] + arr[i - 3])

for i in range(len(arr)):
    print(i + 1,':',arr[i])

