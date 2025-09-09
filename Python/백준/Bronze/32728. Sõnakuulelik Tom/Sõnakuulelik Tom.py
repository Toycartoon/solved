n, k = map(int, input().split())
a = ["" for _ in range(3)]
s = input()
for i in s:
    if i == "s":
        idx = 0
    elif i == "r":
        idx = 1
    elif i == "p":
        idx = 2

    f = True
    while f:
        if len(a[idx]) < k:
            a[idx] += i
            f = False
        else:
            idx = (idx + 1) % 3

for i in a:
    print(i)
