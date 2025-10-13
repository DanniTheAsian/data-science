def gcd(m: int, n: int)-> int:
    
    if m == n:
        return m
    elif m < n:
        return gcd(m,n -m)
    else:
        return gcd(m-n, n)

print(gcd(12,8))

print(gcd(8,12))
print(gcd(12,12))