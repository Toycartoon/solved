from itertools import combinations as comb

for t in range(int(input())):
    a = list(map(int, input().split()))

    right, acute, obtuse = 0, 0, 0
    for x in comb(a, 3):
        i, j, k = sorted(x)
        if not k < i + j:
            continue
        if i ** 2 + j ** 2 == k ** 2:
            right += 1
        elif i ** 2 + j ** 2 > k ** 2:
            acute += 1
        elif i ** 2 + j ** 2 < k ** 2:
            obtuse += 1
    print(right, acute, obtuse)
