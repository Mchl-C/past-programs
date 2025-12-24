import pickle

#--------------------------------------------------------------------------#
# Setup
# Bagian ini bisa diedit untuk settingan awalnya

#=====================================================================#
admins = {
    "Forcat" : "mc",
    "Ricky_Jantan" : "Jantan"
    }

members = {
    "a" : "abc",
    "b" : "bc"
    }

books = {
    "Ricky" : "Learning programming",
    "Hello world" : "By me"
    }

borrowers = {"Ricky" : [["Hello world", False]]}

try:
    admin = open('Admins', 'rb')
    admins = pickle.load(admin)
except:
    admin = open('Admins', 'wb')
    pickle.dump(admins, admin)
    admin.close()

try:
    member  = open('Members', 'rb')
    members = pickle.load(member)
except:
    member = open('Members', 'wb')
    pickle.dump(members, member)
    member.close()

try:
    book  = open('books', 'rb')
    books = pickle.load(book)
except:
    book = open('Books', 'wb')
    pickle.dump(books, book)
    book.close()

try:
    borrow = open('Borrows','rb')
    borrowers = pickle.load(borrow)
except:
    borrow = open('Borrows', 'wb')
    pickle.dump(borrowers, borrow)
    borrow.close()

# Bagian ini untuk simpen data perdana
#=====================================================================#

#--------------------------------------------------------------------------#
# Variable awal

identity = None

#--------------------------------------------------------------------------#
def login_screen():
    run = True
    # Login Screen
    while run:
        print("Please enter your username and password")
        username = input("Username : ")
        password = input("Password : ")

        if(username in admins):
            if(password == admins[username]):
                print("Admin")
                admin_screen("Admin")
                run = False
            else:
                print("Wrong Password")
                
        elif(username in members):
            if(password == members[username]):
                print("Member")
                member_screen("Member", username)
                run = False
            
        else:
            print("Username not registered")
        
        print()

#--------------------------------------------------------------------------#
# Untuk Admin
def admin_screen(identity):
    while identity == "Admin":
        print('~~~ Kategori yang Tersedia ~~~')
        print('''
        1. Buku
        2. Anggota
        3. Peminjaman
        4. Log out
    ''')
        pilihan = int(input("Masukan pilihan Anda : "))

        if(pilihan == 1):
            while True:
                print("--> Pilihan yang Tersedia <--")
                print('''
        1. Menambahkan Buku
        2. Menghapus Buku
        3. Mengedit Buku
        4. Melihat Buku
        5. Back
        ''')
                choice = int(input("Pilihan : "))
                book = open('Books', 'rb')
                books = pickle.load(book)
                    
                if(choice == 1 or choice == 3):
                    title = input("Masukan Judul Buku : ")
                    description = input("Masukan deskripsi Buku : ")
                    books[title] = description
                                
                elif(choice == 2):
                    while True:
                        for i in range(1,len(books)+1):
                            print(str(i) + '.', list(books)[i-1])
                        print(str(len(books) + 1) + '.', "Back")
                        n = int(input("Pilihan : "))
                        if(n >= 1 and n <= len(books)):
                            books.pop(list(books)[n-1])
                        else:
                            break
                        
                    
                elif(choice == 4):
                    while True:
                        for i in range(1,len(books)+1):
                            print(str(i) + '.', list(books)[i-1])
                        print(str(len(books) + 1) + '.', "Back")
                        n = int(input("Pilihan : "))
                        if(n >= 1 and n <= len(books)):
                            print(books[list(books)[n - 1]])
                        else:
                            break
                        print()
                else:
                    break

                book.close()
                book = open("Books", 'wb')
                pickle.dump(books, book)
                book.close()

        elif pilihan == 2:
            while True:
                print("--> Pilihan yang Tersedia <--")
                print('''
        1. Menambah Akun Anggota
        2. Menghapus Anggota
        3. Mengedit Anggota
        4. Melihat Anggota
        5. Back
        ''')
                choice = int(input("Pilihan : "))
                member = open('Members', 'rb')
                members = pickle.load(member)
                    
                if(choice == 1 or choice == 3):
                    name = input("Masukan Nama Anggota : ")
                    password = input("Masukan Password Anggota : ")
                    members[name] = password
                                
                elif(choice == 2):
                    name = input("Masukan Nama Anggota : ")
                    try:
                        members.pop(name)
                    except:
                        print("Member not in list")

                elif(choice == 4):
                    while True:
                        for i in range(1,len(members)+1):
                            print(str(i) + '.', list(members)[i-1])
                        print(str(len(members) + 1) + '.', "Back")
                        n = int(input("Pilihan : "))
                        if(n >= 1 and n <= len(members)):
                            print(members[list(members)[n - 1]])
                        else:
                            break
                        print()
                else:
                    break

                member.close()
                member = open("Members", 'wb')
                pickle.dump(members, member)
                member.close()

        elif pilihan == 3:
            while True:
                print("--> Pilihan yang Tersedia <--")
                print('''
        1. Menyetujui Peminjaman
        2. Menolak Peminjaman
        3. Back
    ''')
                choice = int(input("Pilihan : "))
                borrow = open('Borrows', 'rb')
                borrowers = pickle.load(borrow)
                
                print("--> Daftar permintaan pinjaman <--")
                for i in range(1, len(borrowers) + 1):
                    print(str(i) + '.', list(borrowers)[i - 1])
                print(str(len(borrowers) + 1) + '.', "Back")
                
                if(choice == 1):
                    num = int(input("Pilih member yang ingin disetujui : "))
                    lst = borrowers[list(borrowers)[num - 1]]
                    index = 1
                    for titles in lst:
                        print(str(index) + '.', titles[0], ":",end=' ')
                        print("Belum dipinjam") if titles[1] == False else print("Dipinjam")
                        index += 1
                        
                    n = int(input("Pilih buku yang ingin disetujui : "))
                    borrowers[list(borrowers)[num-1]][n - 1][1] = True

                elif(choice == 2):
                    num = int(input("Pilih member yang ingin ditolak : "))
                    lst = borrowers[list(borrowers)[num - 1]]
                    index = 1
                    for titles in lst:
                        print(str(index) + '.', titles[0], ":",end=' ')
                        print("Belum dipinjam") if titles[1] == False else print("Dipinjam")
                        index += 1
                        
                    n = int(input("Pilih buku yang ingin ditolak : "))
                    borrowers[list(borrowers)[num-1]][n - 1][1] = False

                else:
                    break

                borrow.close()
                borrow = open('Borrows', 'wb')
                pickle.dump(borrowers, borrow)
                borrow.close()
        else:
            identity = None
            run = True
            login_screen()

#--------------------------------------------------------------------------#
# Untuk member
def member_screen(identity, username):
    while identity == "Member":
        while True:
            print("--> Pilihan yang Tersedia <--")
            print('''
        1. Melihat Buku
        2. Meminjam Buku
        3. Mengembalikan Buku
        4. Melihat Riwayat Buku yang dipinjam
        5. Log out
    ''')
            pilihan = int(input("Pilihan : "))
            borrow = open('Borrows', 'rb')
            borrowers = pickle.load(borrow)
                
            if(pilihan == 1):
                while True:
                    for i in range(1,len(books)+1):
                        print(str(i) + '.', list(books)[i-1])
                    print(str(len(books) + 1) + '.', "Back")
                    n = int(input("Pilihan : "))
                    if(n >= 1 and n <= len(books)):
                        print(books[list(books)[n - 1]])
                    else:
                        break
                    print()
            elif(pilihan == 2):
                while True:
                    for i in range(1,len(books)+1):
                        print(str(i) + '.', list(books)[i-1])
                    print(str(len(books) + 1) + '.', "Back")
                    if(len(borrowers[username]) >= 3):
                        print("Sudah meminjam 3 buku")
                        break
                    else:
                        n = int(input("Pilih buku yang ingin dipinjam : "))
                        if(n >= 1 and n <= len(books)):
                            if(borrowers.get(username)):
                                borrowers[username].append([list(books)[n - 1], False])

                            else:
                                borrowers[username] = [[list(books)[n-1], False]]
                                
                        else:
                            break
                    print()

            elif(pilihan == 3):
                try:
                    lst = borrowers[username]
                except:
                    print("Tidak ada buku yang dipinjam")
                    continue
                    
                index = 1
                for titles in lst:
                    print(str(index) + '.', titles[0], ":",end=' ')
                    print("Belum dipinjam") if titles[1] == False else print("Dipinjam")
                    index += 1
                n = int(input("Pilih buku yang ingin dikembalikan : "))
                try:
                    borrowers[username].pop(n - 1)
                except:
                    print("Tidak ada buku yang dipinjam")
                
            elif(pilihan == 4):
                try:
                    lst = borrowers[username]
                except:
                    print("Tidak ada riwayat peminjaman buku")
                    continue
                    
                index = 1
                for titles in lst:
                    print(str(index) + '.', titles[0], ":",end=' ')
                    print("Belum dipinjam") if titles[1] == False else print("Dipinjam")
                    index += 1
            else:
                identity = None
                run = True
                login_screen()
            
            borrow.close()
            borrow = open('Borrows', 'wb')
            pickle.dump(borrowers, borrow)
            borrow.close()

#--------------------------------------------------------------------------#

login_screen()

member.close()
admin.close()
    
