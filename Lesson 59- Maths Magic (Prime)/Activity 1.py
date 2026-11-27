def sieve(n):

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    crossings = 0
    prime = 2
    while prime * prime <= n:
        if is_prime[prime]:
            for multiple in range(prime * prime, n + 1, prime):
                is_prime[multiple] = False
                crossings = crossings + 1
        prime = prime +1
    prime = []
    for k in range(2, n + 1):
        if is_prime[k]:
            prime.append(k)
    return prime, crossings

def reversed_numbers(n):
    rev, steps = 0, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
        steps = steps + 1
    return rev, steps

print("prints up to 30:", sieve(30)[0])
print()
print(" n primes crossings crossings per number")
for n in [10 ** 4, 10 ** 5, 10** 6]:
    primes, crossings = sieve(n)
    print(f" {n:>9} {len(primes)} {crossings:>11} {crossings / n:>22.3f}")
print(0)