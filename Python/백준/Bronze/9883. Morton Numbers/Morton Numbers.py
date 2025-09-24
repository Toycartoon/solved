x, y = map(int, input().split())
x = bin(x)[2:].zfill(16)
y = bin(y)[2:].zfill(16)

s = ""
for i in range(len(x)):
    s += x[i] + y[i]
print(int(s, 2))
