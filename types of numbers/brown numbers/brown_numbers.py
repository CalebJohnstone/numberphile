import sys
import math

limit = int(sys.argv[1])

for n in range(1, limit):
    n_factorial_plus_1 = math.sqrt(math.factorial(n) + 1)

    # check for perfect square
    if math.ceil(n_factorial_plus_1) == math.floor(n_factorial_plus_1):
        print("n =", n, ", m =", math.floor(n_factorial_plus_1))