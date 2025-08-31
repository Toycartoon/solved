n, m, k = map(int, input().split())
a = [*input()]
s = [False for _ in range(n)]

for i in range(n):
    if a[i] == "R":
        for v in range(max(0, i-k), min(n, i+k+1)):
            s[v] = True

if s.count(True) <= m:
    print("Yes")
else:
    print("No")
