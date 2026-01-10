n = int(input())
rule = {}

for i in range(n):
    x, m, *y = input().split()
    rule[x] = set(y)

s = input()
ans = True
for i in range(len(s)-1):
    if s[i] in rule and s[i+1] not in rule[s[i]]:
        ans = False
        break
print("yes" if ans else "no")
