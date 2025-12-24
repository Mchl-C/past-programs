admin = {"user" : "admin","password" : "admin"}
anggota = [{"nama" : 'a', "password" : 'b'}]
password = []
buku = ["Bumi manusia","Laskar pelangi","Anak Semua Bangsa"]
peminjaman = []


def startScreen():
    print("Selamat datang di perpustakaan XYZ")
    print("1. Login sebagai Admin.")
    print("2. Login sebagai Anggota.")
    print("0. Keluar.")

def adminLoginScreen():
    print()
    print("Login sebagai Admin")
    user = input("user : ")
    password = input("password : ")
    if(user == admin["user"]and password == admin["password"]):
        adminScreen()
    else :
        print("User atau Password Salah!")

def adminScreen():
    print()
    print("Admin Dashboard")
    print("1. Kelola Anggota")
    print("2. kelola buku")
    print("3. Kelola Peminjaman")
    print("0. Keluar")
    pil = int(input("Pilih menu : "))
    if(pil == 1):
        adminMemberManagePage()
    if(pil == 2):
        adminManageBook()
    if(pil == 3):
        adminManageLoans()

def adminMemberManagePage():
    print()
    print("Kelola Anggota")
    print("1. Tambah Anggota")
    print("2. Edit Anggota")
    print("3. Hapus Anggota")
    print("4. Tampilkan Anggota")
    print("0. Kembali")
    pil = int(input("Pilih menu : "))
    if(pil == 1):
        adminAddMember()
    elif(pil == 2):
        adminEditMember()
    elif(pil == 3):
        adminDeleteMember()
    elif(pil == 4):
        adminShowMember()
    else:
        if(pil != 0):
            print("Menu tidak terdaftar")
        else:
            adminScreen()
            
    
def adminAddMember():
    print()
    print("Tambah Anggota")
    nama = input("Masukkan nama : ")
    password = input("Masukkan password : ")
    while(len(password)<8):
        print("Password harus lebih dari 8 digit")
        print()
        print("Tambah Anggota")
        nama = input("Masukkan nama : ")
        password = input("Masukkan password : ")
    anggota.append({"nama": nama, "password": password})
    print("Angoota berhasil ditambahkan!")
    adminMemberManagePage()

def adminEditMember():
    print()
    print("Edit Anggota")
    n = int(input("Edit Member ke: "))
    nama = input("Masukkan nama anggota : ")
    password = input("Masukkan password :")
    anggota[n-1] = ({"nama": nama, "password" : password})
    print(nama,"Anggota berhasil diubah")
    adminMemberManagePage()      

def adminDeleteMember():
    print()
    print("Hapus Anggota")
    nama = int(input("Hapus anggota ke :"))
    anggota.pop(nama-1)
    print(nama,"Anggota berhasil dihapus")
    adminMemberManagePage()

def adminShowMember():
    print()
    print("Tampilkan Anggota")
    for i in range(len(anggota)):
        print(str(i+1)+".",anggota[i])
    adminMemberManagePage()

def adminManageBook():
    print()
    print("Kelola Buku")
    print("1. Tambah buku")
    print("2. Hapus Buku")
    print("3. Edit buku")
    print("4. Tampilkan Buku")
    pil = int(input("Pilih menu :"))
    if(pil == 1):
        adminAddBook()
    if(pil == 2):
        adminDeleteBook()
    if(pil == 3):
        adminEditBook()
    if(pil == 4):
        adminShowBook()

def adminAddBook():
    print()
    print("Tambah buku")
    nama = input("Masukkan judul buku : ")
    buku.append(nama)
    print("Buku berhasil ditambahkan!")
    adminManageBook()

def adminDeleteBook():
    print()
    print("Hapus Anggota")
    nama = int(input("Hapus anggota ke :"))
    buku.pop(nama-1)
    print(nama,"Buku berhasil dihapus")
    adminManageBook()

def adminEditBook():
    print()
    print("Edit Buku")
    n = int(input("Edit Buku ke: "))
    nama = input("Masukkan nama buku : ")
    buku[n-1] = nama
    print(nama,"Buku berhasil diubah")
    adminMangaeBook()   

def adminShowBook():
    print()
    print("Tampilkan Buku")
    for i in range(len(buku)):
        print(str(i+1)+".",buku[i])
    adminManageBook()

def adminManageLoans():
    print()
    print("Kelola Peminjaman")

def memberLogin():
    print()
    print("Login sebagai Member")
    n=int(input("Masukkan Nomor Registrasi : "))
    user = input("user : ")
    password = input("password : ")
    if(anggota[n-1] == ({"nama": user, "password" : password})):
        memberLoginScreen()
    else :
        print("User atau Password Salah!")

def memberLoginScreen():
    print()
    print()
    print("Member Dashboard")
    print("1. Tampilkan buku")
    print("2. Pinjam buku")
    print("3. Kembalikan buku")
    print("4. Tampilkan Riwayat Buku yang dipinjam")
    print("0. Keluar")
    pil = int(input("Pilih menu : "))
    if(pil == 1):
        memberShowBook()
    if(pil == 2):
        memberBorrowBook()
    if(pil == 3):
        memberReturnBook()
    if(pil == 4):
        memberHistoryBook()

def memberShowBook():
    print()
    print("Tampilkan Buku")
    for i in range(len(buku)):
        print(str(i+1)+".",buku[i])
    memberLoginScreen()
    
def memberBorrowBook():
    print()
    print("Pinjam Buku")
    username = input("nama :")
    flag = True
    while flag :
        namabuku = input("Judul buku :")
        for book in buku :
            if namabuku in book :
                print("Buku yang di pinjam:",namabuku.format(book[0],book[1]))
                if(len(book[1]) > 0):
                      for siswa in anggota:
                          if username in siswa:
                              pass
                              break
                            
                      else : 
                            sbooks = set()
                            sbooks.add(buku)
                            sbooks_list = [username,sbooks]
                            buku.append(sbooks_list)
                            book[1]-= 1
                            flag = False
                            print(" buku berhasil dipinjam")
                
                break
            else :
                print("Buku tidak ditemukan!")
    
    

##def memberReturnBook():
##    if user in account["anggota"]

def memberHistoryBook():
    import readline
    for i in range(readline.get_current_history_lenght()):
        print(readline.get_history_item(i+1))
    

pil = ""
while(pil != 0):
    startScreen()
    pil = int(input("Pilih menu : "))
    if(pil == 1):
        adminLoginScreen()
    elif(pil == 2):
        memberLogin()
    else:
        if(pil != 0):
            print("Menu tidak terdaftar")
    print()
    
