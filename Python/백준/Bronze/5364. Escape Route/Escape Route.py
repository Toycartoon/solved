n = int(input())
x, y = map(int, input().split())
u, v = -1, -1
mx = float("inf")
for i in range(n-1):
    a, b = map(int, input().split())
    d = ((x-a) ** 2 + (y-b) ** 2) ** 0.5
    if d < mx:
        mx = d
        u, v = a, b

print(x, y)
print(u, v)
print(f"{mx:.02f}")
