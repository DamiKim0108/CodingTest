MOD = 1234567891

def mod_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def mod_inverse(a):
    return pow(a, MOD - 2, MOD)

def combination(n, r):
    if r > n:
        return 0
    numerator = mod_factorial(n)
    denominator = (mod_factorial(r) * mod_factorial(n - r)) % MOD
    return (numerator * mod_inverse(denominator)) % MOD

T = int(input())

for tc in range(1, T + 1):
    N, R = map(int, input().split())
    result = combination(N, R)
    print(f"#{tc} {result}")