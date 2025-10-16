r, c, k = map(int, input().split())
f = True
for i in range(r):
    m, p = input().split()
    if "*" in p and "-" in m:
        f = False
        break
print("Y" if f else "N")
