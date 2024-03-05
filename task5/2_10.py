def f(n):
    d1, d2, d3, d4, d5 = map(int, str(n))
    s1 = d1 + d3 + d5
    s2 = d2 + d4
    if s1 > s2:
        return str(s2) + str(s1)
    else:
        return str(s1) + str(s2)


for i in range(10000, 100000):
    if f(i) == '321':
        print(i)
        break