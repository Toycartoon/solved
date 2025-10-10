n = int(input())
a = ["*" * n]
for i in range(n - 2, -1, -2):
    for _ in range(2):
        a.append(" " * ((n-i) // 2) + "*" * i + " " * ((n-i) // 2))

for i in range(1, n, 2):
    for _ in range(2):
        a.append(" " * ((n-i) // 2) + "*" * i + " " * ((n-i) // 2))
a.append("*" * n)

for i in zip(*a):
    print(*i, sep="")
