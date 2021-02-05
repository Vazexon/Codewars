primes = []
def gap(g, m, n):
    prime_a = 0
    prime_b = 0
    for i in range(m, n+1):
        count = 0
        if i in primes:
            pass
        else:
            for j in range(2, i):
                if i % j == 0:
                    count += 1
        if count == 0:
            primes.append(i)
            if prime_a == 0:
                prime_a = i
            elif prime_b == 0:
                prime_b = i
            else:
                prime_a = prime_b
                prime_b = i
        if prime_b - prime_a == g:
            print([prime_a, prime_b])
            break


gap(8,300,400)
