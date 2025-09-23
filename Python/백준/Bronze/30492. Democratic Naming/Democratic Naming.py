n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())

for i in zip(*a):
    w = [0 for _ in range(26)]
    for v in i:
        w[ord(v)-97] += 1
    print(chr(w.index(max(w))+97), end="")
