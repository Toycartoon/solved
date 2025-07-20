import sys

input = sys.stdin.readline

while True:
    f = input().strip()
    if f == "#":
        break

    w = {}
    t = {"L": 120, "S": 150, "B": 150, "N": 40, "C": 160, "D": 100, "R": 100, "O": 100}
    ans = 0
    while True:
        s, *a = input().strip().split()
        if s == "00A":
            break

        if s in w:
            w[s] += t[a[0]] if a[0] in t else 0
        else:
            w[s] = t[a[0]] if a[0] in t else 0

    for i in w.values():
        if i >= 200:
            ans += 1

    print(f, ans)
