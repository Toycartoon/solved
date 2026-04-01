g = [input() for _ in range(20)]
g.reverse()

k = 0
while k <= 18:
    s = "#" * (k % 9) + "." + "#" * (9 - (k % 9))
    if 18 > k >= 9:
        s = s[::-1]

    if g[k] == s and g[k+1][s.index(".")] == "#":
        k += 1
    else:
        break

if k == 19:
    print("GM")
elif 10 <= k <= 18:
    print("S", k%10+1, sep="")
elif 1 <= k <= 9:
    print(10-k)
else:
    print("X")
