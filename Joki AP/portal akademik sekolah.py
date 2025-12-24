#-----------------------------------------------------------------------#
# Set up variables

users = {
    'a' : ['1234', 16, 'SMA 2', 'Pande', 'A'], # pass, usia, tingkat, komen, rating
    'b' : ['1111', 17, 'SMA 3', 'mager', 'B+'],
    'c' : ['2222', 3, 'SMA 1', 'Ngeri', 'A+'],
    'Pan Violyn' : ['12345', 17, 'SMA 3', 'Genius', 'A++']
}



menu = ['Home', 'Profile', 'News', 'User']
page_length = 60
current_page = 0
username = ''

#-----------------------------------------------------------------------#
# Functions

# Untuk user sebelum login
def opening_page():
    global username
    print("[ Welcome to School's academic portal ]")

    username = input("Input username : ")

    # Kalau tidak terdaftar
    if(username not in list(users)):
        print("User tidak terdaftar. Silahkan coba lagi.")
        print()
    else:
        password = input("Input password : ")
        print()
        # Check password
        if(password == users[username][0]):
            page_menu()
            home_page()
            change_page()
        else:
            print("Password tidak sesuai, coba lagi")
            print()
    

# Untuk page menu(bagian atas yg home profile news user
def page_menu():
    print('_' * page_length)
    m = int(page_length / len(menu) - 2)
    for i in range(len(menu)):
        if(i == current_page):
            print(f'|{menu[i]+"[]":^{m}}|', end = '') # Tandain page skrng
        else:
            print(f'|{menu[i]:^{m}}|', end = '')

    print()
    print('_' * page_length)
    print()

def change_page():
    global current_page
    n = input("Change page?[Y/N] ").strip().lower()
    # .strip() hapus semua spasi
    # .lower() buat jadi huruf kecil semua
    if(n == 'y'):
        page = input("Which page? ").strip().lower()
        if(page == 'home'):
            current_page = 0
            page_menu()
            home_page()
        elif page == 'profile':
            current_page = 1
            page_menu()
            profile()
        elif page == 'news':
            current_page = 2
            page_menu()
            news()
        else:
            current_page = 3
            page_menu()
            user()
    else:
        p = input('logout/close? ')
        if(p == 'close'):
            exit()
        else:
            opening_page()
    print()


# panel-panel
def home_page():
    print("=" * page_length)
    print(f'|{"[ <School Name> ]":^{page_length - 2}}|')
    print('=' * page_length)

    # Content
    print()
    print("Kegiatan terbaru ... ")
    print(" type here ...")
    print(' - ')

    print()
    print('Prestasi')
    print(' type here ...')
    print(' - ')
    print()
    change_page()


# Profile sekolah/ Info umum
def profile():
    print(f'|{"[ School Profile ]":^{page_length - 2}}|')
    print()
    print("Name : <School name>")
    print("Status : Swasta ")
    print("Akreditasi : ")
    print("Alamat : ")
    print("Desa/kelurahan : ")
    print("Kecamatan : ")
    print('Kota : ')
    print("Propinsi : ")
    print("No telp : ")
    print()
    change_page()

# News/berita
def news():
    print(f'|{"[ School News ]":^{page_length - 2}}|')
    print()
    print('[+]' + '-' * (page_length - 2) + '[+]')
    # Contents
    print(' | Isi berita ... ]')
    print('[+]' + '-' * (page_length - 2) + '[+]')
    print()
    print(
'''
Sutomo World Education Expo (SWEE) 2024
Sutomo World Education Expo (SWEE) 2024 kembali diadakan pada tanggal 4 & 5 Oktober 2024. Selain Expo pendidikan, diadakan juga berbagai lomba khusus untuk peserta SMA kelas X, XI, dan ...
''')
    print()
    change_page()

# data siswa yg login
def user():
    global username
    print("Nama siswa : %s"%username)
    print("Usia       : %i"%users[username][1])
    print("Tingkat    : %s"%users[username][2])
    print("Sifat      : %s"%users[username][3])
    print("Rating     : %s"%users[username][4])
    change_page()

    
#-----------------------------------------------------------------------#
# Main

while True:
    opening_page()
