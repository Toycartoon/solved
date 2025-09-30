w = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
a = []
for i in range(int(input())):
    a.append(input())
s = input()

ans = 0
for i in a:
    f = True
    for x in range(len(s)):
        if w[ord(i[x])-97] != int(s[x]):
            f = False
            break
    if f:
        ans += 1
print(ans)
