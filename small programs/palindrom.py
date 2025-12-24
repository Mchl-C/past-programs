n = input()
def palindrom(idx):
    if(idx == len(n)):
        return "Palindrom"
    if(n[idx] != n[len(n) - 1 - idx]):
        return "No"
    else:
        return palindrom(idx + 1)

#print("palindrom") if (n == n[::-1]) else (print("no"))
print(palindrom(0))
