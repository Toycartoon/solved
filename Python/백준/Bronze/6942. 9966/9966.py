m = int(input())
n = int(input())

w = {"1": "1", "8": "8", "0": "0", "6": "9", "9": "6"}
ans = 0
for i in range(m, n+1):
    if len({*str(i)} - {"1", "8", "0", "9", "6"}) == 0:
        v = ""
        for x in str(i)[::-1]:
            v += w[x]

        if str(i) == v:
            ans += 1

print(ans)
