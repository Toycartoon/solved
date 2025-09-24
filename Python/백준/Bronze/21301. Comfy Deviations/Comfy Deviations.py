t = list(map(float, input().split()))
v = sum(t) / 10
s = 0
for i in range(10):
    s += (t[i] - v) ** 2
e = (s / 9) ** 0.5

if e <= 1.0:
    print("COMFY")
else:
    print("NOT COMFY")
