import random
# import module random
# Ini untuk import module random, biar bisa pakek fungsi random
# random bukan built-in function dari python, artinya random itu bukan langsung ada di python kayak print(), input()
# makanya kalau mau pakek harus pakek import modulenya dlu

options = ['R','P','S'] # set-up pilihan apa saja yang bisa dipilih komputer
while True: # selama gamenya masih jalan, karena while tetap jalan selama conditionnya True, jadi ini tetap jalan
    print("= Rock Paper Scissors =")
    print(" R : Rock ")
    print(" P : Paper ")
    print(" S : Scissors")
    n = input("enter ur input: ")
    bot = random.randint(0,2) # random.randint fungsinya random ambil 1 angka dari range yang dikasih, di case ini dia
    # random pilih dari 0 sampai 2
    bot_choice = options[bot] # ini pakek kita tentuin apa pilihan botnya pakek index
    # kalau misalnya kita ada sebuah list arr = [1,2,3,4,5]
    # kita mau panggil salah satu dari elementnya, misnya mau 3
    # bisa pakai yang namannya index untuk access element itu, index itu selalu mulai dari 0
    # jadi arr[0] = 1, arr[1] = 2, arr[2] = 3, and so on
    # disini tadi kan bot itu udah kita random dari 0 sampai 2, jadi indexnya random, hasilnya random jg
    
    res = 'Lose'
    # secara default set kemungkinan ke kalah, g penting sih, mau set ap aj blh

    # masuk ke conditional, kemungkinan buat player bisa menang itu cuman 3 case, jadi pakek itu yang paling simple
    if(n == 'R' and bot_choice == 'S'): # case pertama, player Rock, comp Scissors, jd menang
        res = 'Win'
    elif(n == 'P' and bot_choice == 'R'): # case kedua, player Paper, comp rock
        res = 'Win'
    elif(n == 'S' and bot_choice == 'P'): # case ketiga, player scissors, comp paper
        res = 'Win'
    elif(n == bot_choice): # kalau pilihannya sama, artinya seri
        res = 'Draw'
    else: # kemungkinan lainnya semua player kalah
        res = 'Lose'

    print("You choose to play",n)
    print("Computer choose to play", bot_choice)
    print("Result :",res)

    again = input("Play again?[y/n] ")
    # ingat python itu Case Sensitive, jd inputan harus sama persis baru bs masuk ke if ini
    if(again == 'n'): # kalau input "N", g masuk sini, harus "n"
        break # break buat keluar dari loop, jd disini dia keluar dari while True

    print()

print("Thank you for playing")
