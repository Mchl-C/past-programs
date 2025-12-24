def constant(eq):
    c = ''
    var = ''
    for i in eq:
        if i.isnumeric() : c += i
        else : var += i
    return int(c), var

n = input("Integral ").split("^")
pangkat = int(n[1])
pangkat += 1

k, v = constant(n[0])
print(k, v)

k /= pangkat
if k == 1: k = ''
print(str(k) + v + '^' + str(pangkat))
