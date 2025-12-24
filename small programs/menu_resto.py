menu = {"Daging anjing         " : 10000,
        "Sayur kol             " : 5000,
        "Segelas darah segar   " : 7500,
        "Daging manusia        " : 8000,
        "Hahaha                " : 9000}

pilihan = []

run = True

while run:
    print("+-------------------------------+")
    print("+-  __               _         -+")
    print("+-  |_] | |  | |_|  /_\  |\ |  -+")
    print("+-  |   | |_ | | | /   \ | \|  -+")
    print("+-------------------------------+")

    print("._______________________________.")
    print("|                               |")
    print("| 1. Milih fud                  |")
    print("| 2. Tampilin fud               |")
    print("| 3. Tampilin bill              |")
    print("| 4. G jd beli fud :v           |")
    print("| 5. Bayar ur fud               |")
    print("| 6. di kick dr resto           |")
    print("|_______________________________|")
    print()
    
    opsi = int(input("Pilihan Anda : "))
    print()
    
    if(opsi == 1):

        print("[].__..--''/--|====[]====|--\\''--..__.[]")
        for i in range(len(menu.keys())):
            print("[] ",end = '')
            print(str(i + 1) + '.', list(menu.keys())[i],':', menu[list(menu.keys())[i]],end = ' ' * (7 - len(str(menu[list(menu.keys())[i]]))))
            print("[]")
        print("[].''..--__\--|====[]====|--/__--..''.[]")
        print()

        print("Silahkan dipilih menu yang anda inginkan...(angka)")
        choice = int(input("Pilihan : "))

        print()
        print("----------------------------------------")
        print("Anda memilih :",list(menu.keys())[choice - 1])
        pilihan.append(list(menu.keys())[choice - 1])
        print("----------------------------------------")
        
    elif(opsi == 2):
        print("+" * 30)
        print("Fud pesanan Anda :")
        for i in range(len(pilihan)):
            print(str(i + 1) + '.',pilihan[i].strip())

        print("+" * 30)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    elif(opsi == 3):
        total = 0

        print(".______________________________________________.")
        print(" |[]----------------------------------------[]| ")
        print("  |          B O N    T A G I H A N          |  ")
        print(".|[]----------------------------------------[]|.")
        for i in range(len(pilihan)):
            print("    ",end = '')
            print(pilihan[i],':',' ' * (14 - len(str(menu[pilihan[i]]))),menu[pilihan[i]])
            total += menu[pilihan[i]]
            
        print("    Total Tagihan Anda     :           ",total)

    elif(opsi == 4):
        print("Silahkan pilih dari menu dibawah ini yang mau dihapus...")
        for i in range(len(pilihan)):
            print(str(i + 1) + '.',pilihan[i].strip())
        num = int(input())
        try:
            print(pilihan[num - 1].strip(),'dihapus dari daftar')
            pilihan.remove(pilihan[num - 1])
            
        except IndexError:
            print("Pilihan Tidak tersedia")

    elif(opsi == 5):
        total = 0
        for i in range(len(pilihan)):
            total += menu[pilihan[i]]
        print("Harga totalnya : ",total)
        bayar = int(input("Masukin duitnya : "))
        if(total - bayar > 0):
            print("Uang Anda kurang", total - bayar)
        elif(total - bayar == 0):
            print("Uang Anda Pas")
        elif(total - bayar < 0):
            print("Kembalian Anda : ", abs(total - bayar))
        
    elif(opsi == 6):
        run = False
        break

    else:
        print("Opsi tidak tersedia")
        
    print()

print("Dah dah ~~")
