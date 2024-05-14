def divs(n):
    r = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            r.add(d)
            r.add(n // d)
    return sorted(r)


for n in range(0, 100):
    if len(divs(80 + n)) == 4:
        print(n)
        break