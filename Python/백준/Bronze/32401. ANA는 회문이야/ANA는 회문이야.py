n = int(input())
s = input()

a = []
for i in range(n):
    if s[i] == "A":
        a.append(i)

ans = 0
for i in range(1, len(a)):
    if s[a[i-1]:a[i]].count("N") == 1:
        ans += 1

print(ans)
