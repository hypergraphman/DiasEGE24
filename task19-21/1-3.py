def f(s, c, m, b):
    if c > m:
        return False
    if s >= 141:
        return c % 2 == m % 2
    moves = []
    if b[0] == 0:
        moves.append(f(s + 1, c + 1, m, (1, 0)))
    if b[1] == 0:
        moves.append(f(s * 2, c + 1, m, (0, 1)))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 141):
    for m in range(1, 5):
        if f(s, 0, m, (0, 0)):
            if m == 4:
                print(s)
            break