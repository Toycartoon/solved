w = {"Franklin": 100, "Grant": 50, "Jackson": 20, "Hamilton": 10, "Lincoln": 5, "Washington": 1}
for t in range(int(input())):
    v = 0
    for i in input().split():
        v += w[i]
    print(f"${v}")
