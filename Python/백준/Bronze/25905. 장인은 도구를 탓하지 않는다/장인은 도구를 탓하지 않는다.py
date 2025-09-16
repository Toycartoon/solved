p = []
for i in range(10):
    p.append(float(input()) * 10)

p.sort()
ans = 1
for i in range(1, 10):
    ans *= p[i] / i
print(ans)
