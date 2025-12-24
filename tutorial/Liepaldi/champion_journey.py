import random, json

print("Champion Journey")
print("Lievaldy sedang kia kia ki bataksua, ai ciak BPK, ai ki mikkie, ai ciak bbq, ki indomaret bei mik kia")

uang = 100000
backpack = []

try:
    with open('data.json', 'r') as file:
        loaded_data = json.load(file)
        
    backpack = loaded_data['backpack']
    uang = loaded_data['uang']
except:
    uang = 100000
    backpack = []
    
market = {
    "Aqua 1.5 L" : 6000,
    "Payung" : 25000,
    "Popmie" : 7000,
    "Kondom" : 50000
}

while True:
    print("Actions : ")
    print("1. Beli barang")
    print("2. Merampok orang")
    print("3. Puak kiao")
    print("4. Pakek item")
    print("5. Show isi bp")
    print("6. save data")
    print("7. exit")

    n = int(input("=> : "))
    if(n == 1):
        while True:
            print()
            print("~~ Welkam to indomaret ~~")
            i = 1
            for item in market:
                print(str(i) + '. ' + item + ': ', market[item])
                i += 1
            print(str(i) + '. exit')

            print()
            print("Duit : ", uang)
            print("Mau beli ap?")
            beli = int(input("=> : "))

            try:
                item = list(market.keys())[beli-1]
                if(uang >= market[item] and beli < i - 1):
                    print("Anda membeli " + item)
                    uang -= market[item]
                    backpack.append(item)
                else:
                    print("Uang tidak cukup")
            except:
                break

    elif n == 2:
        print()
        print("Livaldy merampok berapa?")
        quan = int(input("=> "))
        uang += quan

    elif n == 3:
        print()
        print("double or double")
        uang *= 2

    elif(n == 5):
        print()
        i = 1
        print()
        for item in backpack:
            print(str(i) + '. ' + item)
            i += 1


    elif n == 6:
        dic = {
            "backpack" : backpack,
            "uang"  : uang
        }
        
        with open('data.json', 'w') as file:
            json.dump(dic, file)

    elif n == 7:
        break
        
