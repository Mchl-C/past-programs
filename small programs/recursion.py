def fact(n):
    if(n == 1):
        return 1
    return n * fact(n-1)

import math
n = int(input())
print(fact(n))
