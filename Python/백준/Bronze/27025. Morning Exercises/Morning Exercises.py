n = int(input())
ans = []
v = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == b == 0:
        v += 2
    else:
        ans.append(v)
        v = 0
ans.append(v)
print(max(ans))
