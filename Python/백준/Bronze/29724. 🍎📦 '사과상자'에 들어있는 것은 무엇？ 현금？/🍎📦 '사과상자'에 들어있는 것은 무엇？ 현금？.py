g = 0
a = 0
for _ in range(int(input())):
    t, w, h, l = input().split()
    if t == "A":
        v = (int(w) // 12) * (int(h) // 12) * (int(l) // 12)
        g += 1000 + (v * 500)
        a += v
    elif t == "B":
        g += 6000
print(g)
print(a * 4000)
