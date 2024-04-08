from itertools import product

words = [''.join(word) for word in product(sorted('МИЛЯ'), repeat=6)]
# print(words[:10])
k = 0
for i, word in enumerate(words, start=1):
    t = word.replace('М', '1').replace('И', '0').replace('Л', '1').replace('Я', '0')
    if i % 2 == 0 and word[0] != 'И' and '00' not in t and '11' not in t:
        k += 1
    # print(word)
print(k)