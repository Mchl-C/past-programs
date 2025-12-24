import sys, urllib.request

try:
    rfc_num = int(sys.argv[1])
except(IndexError,ValueError):
    print('error')
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = templat.format(rfc_num)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)
