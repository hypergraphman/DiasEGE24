def f(n):
    d1, d2, d3 = map(int, str(n))
    s1 = d1 + d2
    s2 = d2 + d3
    if s1 > s2:
        return str(s1) + str(s2)
    else:
        return str(s2) + str(s1)


for num in range(100, 1000):
    if f(num) == '145':
        print(num)
        break
