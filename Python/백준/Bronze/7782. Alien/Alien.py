n = int(input())
b1, b2 = map(int, input().split())

f = False
for i in range(n):
    lx, ly, hx, hy = map(int, input().split())
    if lx <= b1 <= hx and ly <= b2 <= hy:
        f = True
        break

if f:
    print("Yes")
else:
    print("No")
