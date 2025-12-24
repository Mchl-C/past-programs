def tambah(a, b):
    print(a, "+", b, '=', a + b)

def kurang(a, b):
    print(a, "-", b, '=', a - b)

def kali(a, b):
    print(a, "*", b, '=', a * b)
    
def bagi(a, b):
    print(a, "/", b, '=', a / b)

choice = 0
while choice != 5:
    print("Kalkulator")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    
    choice = int(input("Masukan choice anda : "))

    if(choice == 5):
        print("Terima kasih")
        break
    else:
        a = int(input("Angka 1 = "))
        b = int(input("Angka 2 = "))
        
    if(choice == 1):
        tambah(a, b)
        
    elif(choice == 2):
        kurang(a, b)
        
    elif(choice == 3):
        kali(a, b)

    elif(choice == 4):
        bagi(a, b)

    print()
