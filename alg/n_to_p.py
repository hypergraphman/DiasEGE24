def n_to_p(n, p):
    r = ''
    alp = '0123456789ABCDEF'
    while n:
        r = alp[n % p] + r
        n //= p
    return r


print(n_to_p(255, 16))