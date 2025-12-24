start_menu = ['Appetizer', 'Main Course','Side Dishes', 'Beverage',"Jumlah","Show",'Bayar','Remove','Exit']

appetizer = ['Stuffed mushroom','Fish n chips','Spring rolls','Artichoke and spinach dip']
price1 = [41000,49000,31000,19000]

main_course = ['Chicken wrap','Chicken fried rice','Roasted turkey with mashed potatoes','Spaghetti bolognese','Sweet potato curry','Grilled chicken salad','Marinated kimchi cheese pasta','Chicken lasagna']
price2 = [50000,80000,287000,64000,30000,59000,89000,166666]

side_dishes = ['Mixed green salad','French fries','Garlic bread']
price3 = [65000,20000,16000]

beverage = ['Soda (Coca cola, Sprite, Dr.Pepper)','Tea (Matcha, Earl Grey, Yellow Tea)','Juice (any fruit and vegetable of choice)']
price4 = [900,900,900,900]

fud = []

run = True

while run:
    for i in range (len(start_menu)):
        print (str(i+1) + ". " + start_menu[i])

    choice = int(input("Input : "))

    if(choice == 1):
        print("Appetizer's Menu")
        for x in range(len(appetizer)):
            print(str(x + 1) + '. ' + str(appetizer[x]),':',price1[x])
        n = int(input('Mo yg mana : '))
        fud.append([appetizer[n - 1],1,price1[n - 1]])
        
    elif(choice == 2):
        print("MC's Menu")
        for x in range(len(main_course)):
            print(str(x + 1) + '. ' + str(main_course[x]), ':', price2[x])
        n = int(input('Mo yg mana : '))
        fud.append([main_course[n - 1],1,price2[n - 1]])
        
    elif(choice == 3):
        print("SD's Menu")
        for x in range(len(side_dishes)):
            print(str(x + 1) + '. ' + str(side_dishes[x]), ':', price3[x])
        n = int(input('Mo yg mana : '))
        fud.append([side_dishes[n - 1],1,price3[n - 1]])

    elif(choice == 4):
        print("B's Menu")
        for x in range(len(beverage)):
            print(str(x + 1) + '. ' + str(beverage[x]), ':', price4[x])
        n = int(input('Mo yg mana : '))
        fud.append([beverage[n - 1],1,price4[n - 1]])

    elif(choice == 5):
        print("Daftar")
        for i in range(len(fud)):
            print(str(i + 1) + '. ' + fud[i][0],'%20s'%(fud[i][1]))
        n = int(input("Menu mana yang mau Anda pilih : "))
        p = int(input("Ganti jd brp : "))
        fud[n - 1][1] = p
        
    elif(choice == 6):
        print("show")
        for i in range(len(fud)):
            print(str(i + 1) + '. ' + fud[i][0],'%20s'%(fud[i][1]))

    elif(choice == 7):
        print("bayar")
        tot = 0

        app = []
        mc = []
        sd = []
        b = []
        
        for i in range(len(fud)):
            if(fud[i][0] in appetizer):
                app.append(fud[i])
            elif(fud[i][0] in main_course):
                mc.append(fud[i])
            elif(fud[i][0] in side_dishes):
                sd.append(fud[i])
            elif(fud[i][0] in beverage):
                b.append(fud[i])
        
        if(len(app) >= 1):
            print("Appetizer")
            for x in range(len(app)):
                print(str(x + 1) + '. ' + app[x][0],'%10s'%(app[x][2]))
        if(len(mc) >= 1):
            print("MC")
            for x in range(len(mc)):
                print(str(x + 1) + '. ' + mc[x][0],'%10s'%(mc[x][2]))
        if(len(sd) >= 1):
            print("SD")
            for x in range(len(sd)):
                print(str(x + 1) + '. ' + sd[x][0],'%10s'%(sd[x][2]))
        if(len(b) >= 1):
            print("b")
            for x in range(len(b)):
                print(str(x + 1) + '. ' + b[x][0],'%10s'%(b[x][2]))
        
        for i in range(len(fud)):
            tot += fud[i][1] * fud[i][2]

        print("Total bayaran :",tot)

    elif(choice == 8):
        print("Remove mana")
        for i in range(len(fud)):
            print(str(i + 1) + '. ' + fud[i][0],'%20s'%(fud[i][1]))
        n = int(input())
        fud.pop(n - 1)
        
    else:
        break
    
    print()

print("Anda dikick")
