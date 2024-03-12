def n_to_p(n, p):
    r = ''
    alp = '0123456789ABCDEF'
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n, 7)
    sum_digit = sum(map(int, s1))
    sum7 = n_to_p(sum_digit, 7)
    s2 = '10' + s1[2:] + sum7
    sum_digit = sum(map(int, s2))
    sum7 = n_to_p(sum_digit, 7)
    s3 = '100' + s2[3:] + sum7
    sum_digit = sum(map(int, s3))
    sum7 = n_to_p(sum_digit, 7)
    s4 = '1000' + s3[4:] + sum7
    return int(s4, 7)


a = []
for i in range(1, 10000):
    if f(i) > 100000:
        a.append(f(i))
print(min(a))