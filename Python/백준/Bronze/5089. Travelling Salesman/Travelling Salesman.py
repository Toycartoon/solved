t = 1
while True:
    n = int(input())

    if n == 0:
        break

    s = set()
    for i in range(n):
        s.add(input())

    print(f"Week {t} {len(s)}")
    t += 1
