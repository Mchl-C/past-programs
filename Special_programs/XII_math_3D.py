  # Math Project XII
# ---------------------------- #
import math

# Additional function
def vector_diff(va, vb):
    vr = []
    for i in range(len(vb)):
        vr.append(vb[i] - va[i]) #Vector 2 - vector 1
    return vr

def show_diff(va, vb):
    print(f"{vb[0] - va[0]}i + {vb[1] - va[1]}j + {vb[2] - va[2]}k")

def show_vector(v):
    print(f"[{v[0]}, {v[1]}, {v[2]}]", end = ' ')
    
def vector_multiplication(va, vb):
    vr = []
    for i in range(len(vb)):
        vr.append(vb[i] * va[i])
    return vr

def vector_add(v):
    tot = 0
    for num in v:
        tot += num
    return tot

def vector_resultant(v):
    res = 0
    for vector in v:
        res += vector ** 2
    return res ** 0.5
    
# ---------------------------- #
# 1. Titik
# 1.1. Jarak titik ke titik

def dot_to_dot(x1,y1,z1,x2,y2,z2):
    print(f"sqrt[{x2 - x1}^2 + {y2 - y1}^2 + {z2 - z1}^2]")
    tot = (x2 - x1) ** 2 + (y2-y1)**2 + (z2 - z1)**2
    print(f"sqrt[{tot}]")
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return d

# 1.2. Jarak titik ke garis
def dot_to_line(pos, line):
    x, y = pos[0], pos[1]
    xi, yi = -1, -1
    coef = []
    total = 0

    for j in range(len(line)):
        if 'x' in line[j]:
            xi = j
            coef.append(int(line[j][:-1]))
            
        elif 'y' in line[j]:
            yi = j
            coef.append(int(line[j][:-1]))

        else:
            coef.append(int(line[j]))
        
    print('[' + (" + ".join(line)) + ']', '/', "sqrt[" + str(coef[xi]) + '^2' + '+' + str(coef[yi]) + '^2' + ']')
    hypot = math.hypot(abs(coef[xi]), abs(coef[yi]))

    eq = []
    for j in range(len(coef)):
        if(xi == j):
            eq.append((str(coef[j]) + "(" + str(x) + ")"))
            total += (coef[j] * x)
        elif(yi == j):
            eq.append((str(coef[j]) + "(" + str(y) + ")"))
            total += (coef[j] * y)
        else:
            eq.append(str(coef[j]))
            total += coef[j]

    print('[' + (" + ".join(eq)) + ']', '/', hypot)
    print("Total :", total/ hypot)
    

# 1.3. Jarak titik ke bidang

def dot_to_field(dots, r, field, added, titik):
    # Cara agk ngebrute :v
    positions = {
        0 : [r, 0, 0],
        1 : [r, r, 0],
        2 : [0, r, 0],
        3 : [0, 0, 0],
        4 : [r, 0, r],
        5 : [r, r, r],
        6 : [0, r, r],
        7 : [0, 0, r]
    }

    cn = 8
    for ad in added:
        positions.update({cn : ad})
        cn += 1
        
    field_dots = []
    dot_loc = [0,0,0]
    
    for i in range(len(dots)):
        if(titik == dots[i]):
            dot_loc = positions[i]
                
    for alp in field:
        for i in range(len(dots)):
            if(alp == dots[i]):
                field_dots.append(positions[i])
                continue

    print('===========')
    for i in range(len(points)):
        print(points[i],':',field_dots[i])
        
    vector_12 = vector_diff(field_dots[0], field_dots[1])
    vector_13 = vector_diff(field_dots[0], field_dots[2])

    print('-----------')
    print("Bidang : ")
    print('vektor', field[0] + field[1], '=', field[1],'-',field[0])
    print('=', vector_12)
    print()

    print('vektor', field[0] + field[2], '=', field[2],'-',field[0])
    print('=', vector_13)
    print()

    vector_1dot = vector_diff(field_dots[0], dot_loc)
    print("Titik : ")
    print('vektor', field[0] + titik, '=', titik,'-',field[0])
    print('=', vector_1dot)

    print()
    print('-----------')
    print("Vektor normal")
    print('n =',field[0] + field[1], 'x',field[0] + field[2])
    print(f"{'i':<3} {vector_12[0]:<3} {vector_13[0]:<3} {'|':<3} {'i':<3} {vector_12[0]:<3}")
    print(f"{'j':<3} {vector_12[1]:<3} {vector_13[1]:<3} {'|':<3} {'j':<3} {vector_12[1]:<3}")
    print(f"{'k':<3} {vector_12[2]:<3} {vector_13[2]:<3} {'|':<3} {'k':<3} {vector_12[2]:<3}")
    print()
    
    print(f"{vector_12[1] * vector_13[2]}i + {vector_13[0] * vector_12[2]}j + {vector_12[0] * vector_13[1]}k", end = ' - ')
    print(f"{vector_12[2] * vector_13[1]}i + {vector_13[2] * vector_12[0]}j + {vector_12[1] * vector_13[0]}k")
    
    disc_1 = [vector_12[1] * vector_13[2], vector_13[0] * vector_12[2], vector_12[0] * vector_13[1]] # i, j, k
    disc_2 = [vector_12[2] * vector_13[1], vector_13[2] * vector_12[0], vector_12[1] * vector_13[0]] # i, j, k
    n = vector_diff(disc_2, disc_1)
    show_diff(disc_2, disc_1)
    print("n =",n)

    print()
    d = vector_add(vector_multiplication(vector_1dot, n))/vector_resultant(n)
    print("d = n x %s/|n|"%(field[0] + titik))
    print("d =", end = ' ')
    show_vector(n)
    print(f" x {vector_1dot} / {vector_resultant(n)})")
    print("d =",d)
    
# ---------------------------- #
# Main
run = True

while run:
    print(
'''
<-- Choices -->
1. Dot to dot
2. Dot to line
3. Dot to field
''')

    n = int(input("choice = "))

    if(n == 1):
        x1, y1, z1 = map(int, input("x1, y1, z1 : ").split())
        x2, y2, z2 = map(int, input("x2, y2, z2 : ").split())

        print(dot_to_dot(x1,y1,z1,x2,y2,z2))

    elif(n == 2):
        pos  = list(map(int, input("x1, y1 : ").split()))
        line = input("Line : ").split()
        dot_to_line(pos, line)

    elif(n == 3):
        added = []
        points = []

        name = input("Input variable kubus : ")
        rusuk = int(input("Masukan rusuk kubus : "))

        while True:
            confirm = input("Add dot? (N/<char>) ")
            if(confirm == 'N' or confirm == 'n'):
                break
            else:
                add_dot = list(map(int, input("x y z : ").split()))
                points.append(confirm)
            added.append(add_dot)
            
        field = input("Masukan Bidang : ")        
        titik = input("Titik : ")
        
        dots = [i for i in name]
        bidang = [i for i in field]

        for point in points:
            dots.append(point)
        dot_to_field(dots, rusuk, bidang, added, titik)

    else:
        break

