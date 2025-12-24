uang = 10000
buku = ['a','babababababa','uuuuuu']
harga = [1000, 2000, 3000]

while True:
    print('''    
========================================
       Toko Buku - ABC Book Store       
========================================''')
    print("Uang Anda:", uang)
    print("========================================")
    for i in range(len(buku)):
        print(str(i + 1) + ". Buku : %-15s"%buku[i], "| Harga :", harga[i])

    print("========================================")
    n = int(input("Beli buku mana[masukin angka]: "))
    if(n <= len(buku) and uang >= harga[n - 1]):
        print("Anda membeli buku",buku[n - 1])
        uang -= harga[n - 1]
    elif(uang < harga[n - 1]):
        print("Uang tidak mencukupi")
    else:
        print("Opsi tidak tersedia")
    
    print("Sisa uang : ", uang)
    print("========================================")
    stop = input("lanjut beli?[y/n] : ")
    if(stop == 'n'):
        break
    print()
