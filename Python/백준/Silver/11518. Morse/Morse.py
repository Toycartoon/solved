morse = {}
for i in range(26):
    a, m = input().split()
    morse[a] = m

w = {}
for _ in range(int(input())):
    s = input()
    v = ""
    for i in s:
        v += morse[i]
    w[v] = s

while True:
    n = int(input())
    if n == 0:
        break

    ans = []
    f = True
    for _ in range(n):
        s = input()
        if not f:
            continue
        if s in w:
            ans.append(w[s])
        else:
            ans = [s]
            f = False

    if f:
        print(*ans)
    else:
        print(f"{ans[0]} not in dictionary.")
