n = int(input())
s = input()
f = False
for i in range(1, n // 2 + 1):
    if n % i != 0:
        continue

    x = s[:i]
    a = True
    for v in range(i, len(s)+1, i):
        if s[v-i:v] != x:
            a = False
            break
    if a:
        f = True
        break

if f:
    print("Yes")
else:
    print("No")
