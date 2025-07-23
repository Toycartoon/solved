w = {}
for i in range(int(input())):
    s, p = input().split()
    w[p] = s

x = input()
ans = ""
for i in range(4, len(x)+1, 4):
    if x[i-4:i] in w:
        ans += w[x[i-4:i]]
    else:
        ans += "?"

print(ans)
