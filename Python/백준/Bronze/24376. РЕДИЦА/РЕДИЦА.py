x, n = map(int, input().split())
s = ""
b = 1
while len(s) < 1000000:
    s += str(b)
    b *= x
print(s[n-1])
