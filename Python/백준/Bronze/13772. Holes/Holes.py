w = {"A": 1, "B": 2, "D": 1, "O": 1, "P": 1, "Q": 1, "R": 1}

for t in range(int(input())):
    ans = 0
    for i in input():
        if i in w:
            ans += w[i]

    print(ans)
