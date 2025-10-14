n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

ans = 0
for i in range(n):
    ans += 1
    if a[i] == i:
        break
print(ans)
