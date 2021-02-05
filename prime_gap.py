"""
gap() returns the first pair of two prime numbers spaced with a gap of g
between the limits m, n
"""

def gap(g, m, n):
    prime_a = 0
    prime_b = 0
    for i in range(m,n+1):
        if is_prime(i):
            if prime_a == 0:
                prime_a = i
            elif prime_b == 0:
                prime_b = i
            else:
                prime_a = prime_b
                prime_b = i
        if prime_b - prime_a == g:
            return [prime_a, prime_b]



def is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
            return False
        i += 1
    return True

gap(2,100,110)
gap(4,100,110)
gap(6,100,110)
gap(8,300,400)
gap(10,300,400)
gap(2,100,103)
