print("Bilangan Fibonacci")
n = int(input("Jumlah angka : "))
a=1
b=1
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c

