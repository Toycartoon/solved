a, b, c, d = map(int, input().split())
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
    print(max(d, b)-min(a, c)+1)
else:
    print(b-a+1 + d-c+1)
