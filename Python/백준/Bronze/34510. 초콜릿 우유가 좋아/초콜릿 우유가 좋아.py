h1, h2, h3 = map(int, input().split())
n = int(input())

if n % 2 == 0:
    print(h2 * (n // 2) + h3 * n)
else:
    print(h2 * (n // 2 + 1) + h3 * n + h1)