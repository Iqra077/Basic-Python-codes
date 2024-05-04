def mul(val, n):
    if n==1:
        return val
    t = mul(val, n-1)
    return val + t

print(mul(15,5))
