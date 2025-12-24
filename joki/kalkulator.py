def tambah(y, z):
    print(y, "+", z, '=', y + z)

def kurang(y, z):
    print(y, "-", z, '=', y - z)

def kali(y, z):
    print(y, "*", z, '=', y * z)
    
def bagi(y, z):
    print(y, "/", z, '=', y / z)

def pangkat(y, z):
    print(y, "^", z, '=', y ** z)

pil = 0
while pil != 6:
    print('''
Kalkulator
1. Tambah
2. Kurang
3. Kali
4. Bagi
5. Pangkat
6. Keluar
''')
    pil = int(input("Masukan pil anda : "))

    if(pil == 1):
        y = int(input("Angka 1 = "))
        z = int(input("Angka 2 = "))
        tambah(y, z)
        
    elif(pil == 2):
        y = int(input("Angka 1 = "))
        z = int(input("Angka 2 = "))
        kurang(y, z)
        
    elif(pil == 3):
        y = int(input("Angka 1 = "))
        z = int(input("Angka 2 = "))
        kali(y, z)

    elif(pil == 4):
        y = int(input("Angka 1 = "))
        z = int(input("Angka 2 = "))
        bagi(y, z)

    elif(pil == 5):
        y = int(input("Angka 1 = "))
        z = int(input("Angka 2 = "))
        pangkat(y, z)
        
    else:
        print("Terima Kasih")
        
