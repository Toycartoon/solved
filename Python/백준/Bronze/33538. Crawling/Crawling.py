l = int(input())
n = int(input())
t = float(input())

a = []
for i in range(n):
    f, b = map(float, input().split())
    a.append(l / f + l / b)

if min(a) < t:
    print("HOPE")
else:
    print("DOOMED")
