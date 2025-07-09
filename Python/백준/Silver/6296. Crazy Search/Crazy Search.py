n, nc = map(int, input().split())
s = input()

v = set()
for i in range(n, len(s)+1):
    v.add(s[i-n:i])

print(len(v))
