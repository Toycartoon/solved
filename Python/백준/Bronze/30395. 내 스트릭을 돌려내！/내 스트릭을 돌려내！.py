n = int(input())
p = list(map(int, input().split()))

ans = []
v = 0 if p[0] == 0 else 1
for i in range(1, n):
    if p[i] == 0:
        if p[i-1] == 0:
            ans.append(v)
            v = 0
    else:
        v += 1

ans.append(v)
print(max(ans))
