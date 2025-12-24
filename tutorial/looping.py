# looping
# jadi looping itu kayak jalanin code yg sama berulang terus
# looping sendiri terbagi jadi 2 di python
# ada for loop sama while loop

# for loop
for i in range(5):
    print("Nomor",i)

# ini outputnya
'''
Nomor 0
Nomor 1
Nomor 2
Nomor 3
Nomor 4
'''
# In case bingung knp ngk 1 2 3 4 5
# range mulainya dari 0 itungnya
# jadi dia loop dari 0 sampe sebelum 5
# tp klo mau dr 1 bisa jg
# for i in range(*start, stop, *step)
# yg ada * artinya optional

print()
print("Ini contoh for loop lain")
for i in range(1,6,2):
    print(i)

# for loop bisa digabungin sama fungsi lain spt input jg
print()
for i in range(3):
    # ini untuk kluarin menunya
    print("Menu")
    print("1. tambah")
    print("2. kali")
    print("3. exit")

    # Ini fungsi untuk input, jadi nnti nilainya disimpan di var a,b,n
    n = int(input("Masukin input : "))
    a = int(input("Angka pertama : "))
    b = int(input("Angka kedua   : "))

    # -----------------------------------------------------
    # Ini fungsi percabangan
    # klo kondisi if tidak terpenuhi masuk ke elif
    # klo yg if sama elif tidak terpenuhi smua baru masuk ke else
    
    if(n == 1):
        print("Hasil :", a + b)
    elif(n == 2):
        print("Hasil :", a * b)
    else:
        print("Quit")
        break
    # Break fungsinya untuk keluar dari looping
    print()

print()
# print() untuk skip 1 baris btw
# kalau mau habis print g skip 1 baris bisa pakai print("", end = '')

# Selain dari break ada juga continue di looping
# Fungsinya untuk balek ke atas dari tab looping

# Habis for looping ada juga while loop
# Bedanya sama for, while dia jalan sampai condition dlm while false atau break
# Biasa for loop dipakai untuk code yg kita tahu jalan brp kali
# Sedangkan while untuk yg kita g pasti jlnnya sampe brp kali

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# While loop

duit = 0
while (duit < 100000):
    print("Choices")
    print("1. add 10000")
    print("2. multiply by 2")
    print("3. exit")

    n = int(input("Choice : "))
    if(n == 1):
        duit += 10000
    elif(n == 2):
        duit *= 2
    else:
        break

# Ini codenya bakalan jalan terus sampai duitnya sama dengan atau diatas 100k
# Kalau g dia akan loop terus yang di dalamnya ini

# Looping merupakan slh satu topik penting di programming, jadi kuasain baik"

'''
Tugas 1
Buatlah program yang bisa memprint persegi ukuran m * n, dengan m jumlah baris
dan n jumlah kolom

sample case 1
m = 5
n = 4

xxxx
xxxx
xxxx
xxxx
xxxx

sample case 2
m = 6
n = 12
xxxxxxxxxxxx
xxxxxxxxxxxx
xxxxxxxxxxxx
xxxxxxxxxxxx
xxxxxxxxxxxx
xxxxxxxxxxxx
'''

'''
Tugas 2
Buatlah program Kalkulator sederhana yang bisa menggunakan operasi
tambah kurang kali bagi pangkat sama exit :)
'''

'''
Tugas 3
Buatlah program yg bisa menginput sisi dan mengoutput persegi
s x s dengan diagonalnya mempunyai pola yang berbeda

sample case 1
s = 7
x.....x
.x...x.
..x.x..
...x...
..x.x..
.x...x.
x.....x

sample case 2
s = 8
x......x
.x....x.
..x..x..
...xx...
...xx...
..x..x..
.x....x.
x......x
'''

# Semangat belajarnya !!!

