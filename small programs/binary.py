while True:
    n = str(input())
    v = 1
    tot = 0
    for i in n[::-1]:
        tot += int(i)*v
        v *= 2
    print(chr(tot))
    
