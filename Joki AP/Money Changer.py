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
        print(f'|{str(i):>{spacing[0]}} || {currency[i-1]:<{spacing[1]}} |')
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
