import random

run = True
# set sebuah var boolean "run" jadi True, nanti selama run True, while run tetap jalan
score = 0 # ini untuk keep track score player sama komp udh brp
comp_score = 0

while run:
    print("[ Rock | Paper | Scissors ]")
    print("===========================")
    print("Player score :", score) # show score player n comp
    print("Comp   score :", comp_score)
    print("===========================")
    
    player = input("=> ")
    computer = random.choice(['Rock','Paper','Scissors'])
    # random ambil 1 pilihan dari list yang disediakan
    # cara pakeknya random.choice([items])

    # ini cara barbar sih, cek semua kemungkinan yang bisa keluar
    # kalau g suka cara ini bisa ganti sama cara di file kedua
    if(player == 'Rock' and computer == 'Paper'): # kalau player rock n comp paper
        print("Computer played %s, player loses!"%computer) # comp menang
        comp_score += 1 # score comp + 1
    elif(player == 'Rock' and computer == 'Scissors'): # kalau player rock n comp scissors
        print("Computer played %s, player wins!"%computer) # komp yang kalah
        score += 1 # player score + 1
    elif(player == 'Rock' and computer == 'Rock'): # ini case klo seri
        print("Computer played %s, it's a draw!"%computer)

    # print("%s"%comp) itu namanya formatting
    # jadi ini biasa dipakai kalau kita mau tambahin string lain didalam print
    # kek print("hello %s, how are you?"%"world") hasilnya jadi "hello world, how are you?"
    # dia cuman ubah yang %s jadi yang di blkng itu
    # tapi formatting sendiri ada bbrp jenis, %i untuk integer, %f float, dll

    # Oiya ingat python itu case sensitive, krn di condition td kita buat "Rock" artinya cuman
    # bakalan jalan kalau inputannya "Rock", gbs 'rock','RocK', 'rOck' atau kombinasi lain
    # kalau mau fix bisa pakek input.lower() trus ubah semua yang di if jd huruf kecil semua

    if(player == 'Paper' and computer == 'Scissors'):
        print("Computer played %s, player loses!"%computer)
        comp_score += 1
    elif(player == 'Paper' and computer == 'Rock'):
        print("Computer played %s, player wins!"%computer)
        score += 1
    elif(player == 'Paper' and computer == 'Paper'):
        print("Computer played %s, it's a draw!"%computer)

    if(player == 'Scissors' and computer == 'Rock'):
        print("Computer played %s, player loses!"%computer)
        comp_score += 1
    elif(player == 'Scissors' and computer == 'Paper'):
        print("Computer played %s, player wins!"%computer)
        score += 1
    elif(player == 'Scissors' and computer == 'Scissors'):
        print("Computer played %s, it's a draw!"%computer)

    print("Continue playing? [yes/no]")
    proceed = input("=> ")
    if(proceed == 'no'):
        run = False # run dibuat false, jadi while g jln lg
        
    print() # skip a line

print("Game Over!")
