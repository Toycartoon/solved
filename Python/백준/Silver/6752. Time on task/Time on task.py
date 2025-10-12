t = int(input())
c = int(input())

a = []
for i in range(c):
    a.append(int(input()))
a.sort()

ans = 0
for i in a:
    if t-i >= 0:
        t -= i
        ans += 1
    else:
        break
print(ans)
