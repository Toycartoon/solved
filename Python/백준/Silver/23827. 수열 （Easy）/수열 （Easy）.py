n = int(input())
a = list(map(int, input().split()))

v = 0
for i in a:
    v += i ** 2

print((sum(a) ** 2 - v) // 2 % 1000000007)
