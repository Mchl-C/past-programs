# Source: https://usaco.guide/general/io


#-------------------------------------------------------------------#
# Set up
# Mata uang yang tersedia
# List bisa menampung beberapa nilai 
# Untuk memanggil element tertentu dari sebuah list bisa dengan index
# Misnya arr = [1,2,3,4,5]
# Index mulai dr 0
# Untuk mendapatkan 1 bisa pakai arr[0]
mata_uang = ['USD', 'Euro', 'Yen', 'Singapore Dollar']

# Dictionary, bisa mendapatkan value dari sebuah key
# {key : value}
# untuk dapat value bisa dict[key]
# Ini untuk harga
pricing = {
    mata_uang[0] : 1,
    mata_uang[1] : 1.09,
    mata_uang[2] : 0.0065,
    mata_uang[3] : 0.75
}

#-------------------------------------------------------------------#
# Functions

# Varible vs Function
# Variable sebuah wadah, function untuk jalankan 1 bagian program
# def function(arguments)

# Untuk mengubah mata uang asal ke USD
def convert_to_dolar(asal, jumlah):
    return jumlah / pricing[mata_uang[asal - 1]]

# def f(args):
#   return args
# f(args)

# yen -> usd
# 1 yen = 0.0065 usd
# 1 usd = bagi 0.0065

# Dari mata uang asli, convert dlu ke USD
# baru convert balek ke mata uang tujuan
def convert_to_hasil(asal, jumlah, akhir):
    usd = convert_to_dolar(asal,jumlah)
    return usd / pricing[mata_uang[akhir - 1]]

#-------------------------------------------------------------------#
# Main Program
print("Money Changer")

# 0 1 2 3 <| 4
# for i in range(start, stop, step)
for i in range(len(mata_uang)):
    print(str(i + 1) + '. ' + mata_uang[i])

asal = int(input("Masukan mata uang awal : "))
uang = int(input("Masukkan mata uang => "))
akhir = int(input("Masukan mata uang tujuan : "))

print("Hasil konversi mata uang dari %s ke %s"%(mata_uang[asal-1],mata_uang[akhir-1]))
print(convert_to_hasil(asal, uang, akhir))

