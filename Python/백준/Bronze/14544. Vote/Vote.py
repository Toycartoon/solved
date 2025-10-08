for t in range(int(input())):
    n, m = map(int, input().split())
    w = {}
    for i in range(n):
        w[input()] = 0

    for _ in range(m):
        s, v, _ = input().split()
        w[s] += int(v)

    if list(w.values()).count(max(w.values())) > 1:
        print(f"VOTE {t+1}: THERE IS A DILEMMA")
    else:
        v = max(w.items(), key=lambda x: x[1])
        print(f"VOTE {t+1}: THE WINNER IS {v[0]} {v[1]}")
