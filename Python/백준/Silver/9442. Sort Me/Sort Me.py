t = 1
while True:
    n, *s = input().split()
    if n == "0":
        break

    a = []
    for i in range(int(n)):
        a.append(input())

    a.sort(key=lambda x: [s[0].index(i) for i in x])
    print(f"year {t}")
    for i in a:
        print(i)
    t += 1
