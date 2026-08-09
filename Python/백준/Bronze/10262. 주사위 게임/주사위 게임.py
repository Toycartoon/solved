a1, b1, a2, b2 = map(int, input().split())
c1, d1, c2, d2 = map(int, input().split())

g, e = 0, 0
for i in range(a1, b1+1):
    for j in range(a2, b2+1):
        for k in range(c1, d1+1):
            for l in range(c2, d2+1):
                if i + j > k + l:
                    g += 1
                elif i + j < k + l:
                    e += 1
if g < e:
    print("Emma")
elif g > e:
    print("Gunnar")
else:
    print("Tie")
