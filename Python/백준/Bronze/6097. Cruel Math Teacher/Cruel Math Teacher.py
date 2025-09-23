n, p = map(int, input().split())
s = str(pow(n, p))
for i in range(70, len(s)+1, 70):
    print(s[i-70:i])

if len(s) % 70 != 0:
    print(s[-(len(s) % 70):])
