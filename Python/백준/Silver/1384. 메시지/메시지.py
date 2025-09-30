t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        a.append(input().split())

    print(f"Group {t}")
    nasty = False
    for i in range(n):
        for v in range(1, n):
            if a[i][v] == "N":
                print(f"{a[i-v][0]} was nasty about {a[i][0]}")
                nasty = True

    if not nasty:
        print("Nobody was nasty")
    print()
    t += 1
