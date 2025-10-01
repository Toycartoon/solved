w = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = input()

ans = 0
for i in range(0, len(s)-2, 2):
    v = int(s[i]) * w[s[i+1]]
    if w[s[i+1]] < w[s[i+3]]:
        ans -= v
    else:
        ans += v
ans += int(s[-2]) * w[s[-1]]
print(ans)
