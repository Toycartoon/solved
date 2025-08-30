n = int(input())
a = list(map(int, input().split()))

mx = max(a)
r = a.index(mx)
b = a[::-1].index(mx)

if r < b:
    print("R")
elif r > b:
    print("B")
else:
    print("X")
