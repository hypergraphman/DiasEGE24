for x in range(20):
    a = 1 * 20**7 + 2 * 20**6 + 3 * 20**5 + 4 * 20**4 + 5 * 20**3 + x * 20**2 + 7 * 20**1 + 8 * 20**0
    b = 9 * 20**4 + x * 20**3 + 7 * 20**2 + 6 * 20**1 + 5 * 20**0
    s = a + b
    if s % 19 == 0:
        print(x, s // 19)