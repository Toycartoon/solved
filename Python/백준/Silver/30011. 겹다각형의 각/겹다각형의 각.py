n = int(input())
a = list(map(int, input().split()))

angle = a[0]
for i in range(1, n):
    angle += a[i]

angle -= 2
print(angle * 180)
