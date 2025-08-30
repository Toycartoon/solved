n, s, p = map(int, input().split())
if n == 0: print(1); exit()
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < s:
        print(i+1)
        break
    elif a[i] == s:
        if a[i:].count(s) == n-i and n == p:
            print(-1)
        else:
            print(i+1)
        break

if a[-1] > s:
    if n < p:
        print(n+1)
    else:
        print(-1)
