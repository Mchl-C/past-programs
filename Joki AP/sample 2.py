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
print(str(len(mata_uang) + 1) + '. exit')

asal = int(input("Masukan mata uang awal : "))

if(asal >= len(mata_uang) + 1):
    exit()
    
uang = float(input("Masukkan mata uang => "))
akhir = int(input("Masukan mata uang tujuan : "))

for i in range(1, len(mata_uang) + 1):
    for x in range(1, len(mata_uang) + 1):
        if(asal == i and akhir == x):
            print("Hasil konversi mata uang dari %s ke %s"%(mata_uang[i - 1],mata_uang[x - 1]))
            print("Hasil -> %.2f"%convert_to_hasil(i - 1, uang, x))


# Membatasi angka ribuan
# 1_000_000

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
'''
#------------------------------------------------------------------------#
# Set up variables

currency = ['ID Rupiah RP', 'USD', 'Thai Bath', 'India Rupee INR', 'New Taiwan dollar TWD', 'Malaysian Ringgit MYR','Japanese Yen JPY', 'Euro EUR','Won KRW']

# Convert all to dollar first
pricing = {
    currency[0] : 15_682.3159,
    currency[1] : 1,
    currency[2] : 33.7554,
    currency[3] : 84.097,
    currency[4] : 31.9424,
    currency[5] : 4.3799,
    currency[6] : 152.9741,
    currency[7] : 0.9219,
    currency[8] : 1_378.3366
}

spacing  = [2, 30]
length = 40


#------------------------------------------------------------------------#
# Functions

def menu():
    print("_" * length)
    print(f' | {"Money Currency":^36} |')
    print('=' * length)
    for i in range(1, len(currency) + 1):
        print(f'|{str(i):>2} || {currency[i-1]:<30} |')
    print(f'|{"10":>{spacing[0]}} || {"Quit":<{spacing[1]}} |')
    print('=' * length)
    print("Input number of choice")
    
    n = int(input("= Input your currency => "))

    if n >= 9 or n <= 0:
        exit()
        
    amt = float(input("[ Input the amount ] "))
    
    n1 = int(input("= Convert to? => "))
    print()
    
    return n, n1, amt

def convert_to_usd(n, amt):
    return amt / pricing[currency[n - 1]]
    

def convert_to_currency(n, n1, amt):
    dollar = convert_to_usd(n , amt)
    return dollar * pricing[currency[n1 - 1]]

#------------------------------------------------------------------------#
# Main

while True:
    n, n1, amt = menu()
    print("=" * length)
    print("Conversion from %.2f %s to %s :"%(amt, currency[n - 1], currency[n1 - 1]))
    print('{s} : {res:,}'.format(s = currency[n1 - 1], res = convert_to_currency(n, n1, amt)))
    print()

~~~
Border

 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
   | |                                            | |
   | |                                            | |
   | |                                            | |
   | |                                            | |
   | |                                            | |
 __| |dc__________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
'''
