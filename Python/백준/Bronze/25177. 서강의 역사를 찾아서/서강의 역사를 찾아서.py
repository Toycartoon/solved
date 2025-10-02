n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.extend([0] * (max(n, m)-len(a)))
b.extend([0] * (max(n, m)-len(b)))
s = sum(a)

ans = 0
for i in range(len(a)):
    v = 0
    for j in range(len(a)):
        if i == j:
            v += b[j]
        else:
            v += a[j]
    ans = max(v-s, ans)
print(ans)
