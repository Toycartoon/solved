n, k = map(int, input().split())
s = input()

a, b, c, d = s[:n//4], s[n//4:n//2], s[n//2: n//2+n//4], s[n//2+n//4:]
if k % 3 == 1:
    print(a+d+b+c)
elif k % 3 == 2:
    print(a+c+d+b)
else:
    print(a+b+c+d)
