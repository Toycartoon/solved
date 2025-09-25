w = {"A": (11, 11), "K": (4, 4), "Q": (3, 3), "J": (20, 2), "T": (10, 10), "9": (14, 0), "8": (0, 0), "7": (0, 0)}
n, b = input().split()
ans = 0
for i in range(4 * int(n)):
    s = input()
    if s[-1] == b:
        ans += w[s[0]][0]
    else:
        ans += w[s[0]][1]
print(ans)
