n = int(input())
x = list(map(int, input().split()))

a = 0
for i in x:
    a += i ** 2

print((sum(x) ** 2 - a) // 2)
