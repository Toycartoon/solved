l, a = map(int, input().split())
h = list(map(int, input().split()))

f = True
for i in range(1, l+1):
    if h[i] - h[i-1] > a:
        f = False
        break

if f:
    print("POSSIBLE")
else:
    print("BUG REPORT")
