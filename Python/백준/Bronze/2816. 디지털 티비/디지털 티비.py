n = int(input())
a = []
for i in range(n):
    a.append(input())

idx = 0
for i in range(n):
    if a[i] == "KBS1":
        break
    else:
        idx += 1
        print(1, end="")

for i in range(idx, 0, -1):
    a[i], a[i-1] = a[i-1], a[i]
    print(4, end="")

idx = 0
for i in range(n):
    if a[i] == "KBS2":
        break
    else:
        idx += 1
        print(1, end="")

for i in range(idx, 1, -1):
    a[i], a[i-1] = a[i-1], a[i]
    print(4, end="")
