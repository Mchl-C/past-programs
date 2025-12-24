variable = "jeruk"

print("Progam")
print("1. Luas Permukaan")
print("2. Volume")
print("3. Keliling Balok")
pilihan = int(input('Masukkan pilihan: '))
p = int(input('Masukan Panjang : '))
l = int(input('Masukan Lebar : '))
t = int(input('Masukan Tinggi : '))

# oiya btw di ide usaco emg dia gbs jln 1 by 1
# bntr w show di pitong aj

print()
if(pilihan == 1):
    # disini kita perlu nilai p, l, sama t untuk itung
    lp = 2*((p*l) + (p*t) + (l*t)) # ini rumus utk lp balok
    print("Luas permukaan :", lp)
elif(pilihan == 2):
    V = p*l*t
    print("Volume balok :", V)
elif(pilihan == 3):
    k = 4 * (p+l+t)
    print("Keliling balok :", k)
# jd kek di sumbu-sumbunya?
#
# keliling balok sama lp ap bedanya?
# agk jrg denger sih, anggep aj bener wkwk

'''
ini fungsinya utk comment, jd yg masuk kesini g dijalankan di codenya
sampai sini bisa paham dlu g?

klo ini udh masuk ke fungsi, nnti perlahan aj baru ajarin ke sana wkwk
utk skrng mulai dari if dlu yg biasa, nnti ke looping
def luas_permukaan(p,l,t)

trus klo misnya spt diatas
kan udh ad ditanya ke user 
nnti dr pilihan user kita mau kluarin hasil yg beda
ini nnti masuk ke percabangna

if (<condition>) :
    code

jd kek
'''


