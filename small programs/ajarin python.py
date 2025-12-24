run = True

print("+--\\'-_---__-\\___-----___/-__-----_-'/--+")# 
print("|_\\~\\~~\\~/ Buatan Tok Darren \\~~~/~~/~/_|")
while run:                                          
    print ("Cepat Milih sana :v")
    print ("1. Penjumlahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("5. Perpangkatan")
    print ("6. Banting Kalkulator")
    n = int(input("Pilihanmu: "))

    if n == 6:
        pass
    else:
        a = int(input("a : "))
        b = int(input("b : "))

    if n == 1:
        Hasil_jumlah = a+b
        print("Hasil jumlah : ",Hasil_jumlah)
    elif n == 2:
        Hasil_kurang = a-b
        print("Hasil Utang : ",Hasil_kurang)
    elif n == 3:
        Hasil_kali = a*b
        print("Hasil Investasi Bondong : ",Hasil_kali)
    elif n == 4:
        Hasil_bagi = a/b
        print("Hasil Dirampok Istri : ",Hasil_bagi)
    elif n == 5:
        variabel = a
        for i in range (b): 
            a *= variabel  
        print("Jumlah atom di rambut atok : ",a)
    elif n == 6:
        print("sep, kalkulatormu rusak")
        break
    else:
        print("Hadeh Mabok Lagi")
    print()
