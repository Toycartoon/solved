n = int(input())
s = input().split()

v = 0
for i in s:
    if v + len(i) > n:
        v = 0
        print()
    if v == 0:
        print(i, end="")
    else:
        print(" " + i, end="")
    v += len(i)
