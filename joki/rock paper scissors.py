import random # Ini untuk import module random, biar bisa pakek fungsi random
# random bukan built-in function dari python, artinya random itu bukan langsung ada di python kayak print(), input()
# makanya kalau mau pakek harus pakek import modulenya dlu

while True: # selama gamenya masih jalan, karena while tetap jalan selama conditionnya True, jadi ini tetap jalan
    print("Permainan Batu, Gunting, Kertas")

    choice = input("pilihan : ")
    comp = random.choice(["batu", "gunting", "kertas"]) # random ambil 1 pilihan dari list yang disediakan
    # cara pakeknya random.choice([items])
    winner = '' # ini set buat nanti tentuin siapa yang menang

    # habis itu ini pakek conditional cek 1 per 1 kondisi yang bisa muncul
    if(choice == "batu"): # saat player pilih batu
        if(comp == 'gunting'): # kalau komputer pilih gunting
            winner = 'pemain' # player menang
        elif(comp == 'kertas'): # setelah if g masuk, dia lanjut cek elif
            # jadi ini dia cek lg komp klo pilih kertas
            winner = 'komputer' # komp menang
        else: # else itu klo if sama elif g masuk, sisanya semua ke else
            # jadi klo player milih batu, komp g milih kertas sama gunting
            winner = 'seri' # hasilnya seri
            # ini kebetulan cuman 3 choices, jd bs dianggep selain gunting dan kertas sisa batu
            # which is the same option as pemain
    elif(choice == "gunting"):
        if(comp == 'kertas'):
            winner = 'pemain'
        elif(comp == 'batu'):
            winner = 'komputer'
        else:
            winner = 'seri'
    elif(choice == "kertas"):
        if(comp == 'batu'):
            winner = 'pemain'
        elif(comp == 'gunting'):
            winner = 'komputer'
        else:
            winner = 'seri'

    print("Komputer memilih", comp)
    print("[| Pemenang :", winner,'|]')
        
    restart = input("main lagi?[y/n] ")
    # disini di cek mau lanjut main g
    if(restart == 'n'):
        # kalau ngk, langsung break, break fungsinya keluar dari looping, jd krn ini letaknya
        # di dalam while loop, dia keluar dari while True yang td
        break
    
    print() # skip a line

# setelah game end, ini baru di print keluar( setelah while True siap)s
print("~ Thanks for playing ~")
        
            
