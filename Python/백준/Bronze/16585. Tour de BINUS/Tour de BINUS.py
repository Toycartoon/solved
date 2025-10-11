n = int(input())
a = list(map(int, input().split()))
x1, d1 = input().split()
x2, d2 = input().split()

if d1 == "left":
    print(sum(a[:int(x1)]), end=" ")
elif d1 == "right":
    print(sum(a[int(x1)-1:]), end=" ")

if d2 == "left":
    print(a[:int(x2)].count(0))
elif d2 == "right":
    print(a[int(x2)-1:].count(0))
