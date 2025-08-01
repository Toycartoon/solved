b, d, c, l = map(int, input().split())

output = []
for i in range(l+1):
    for j in range(l+1):
        for k in range(l+1):
            if i * b + j * d + k * c == l:
                output.append((i, j, k))

if len(output) == 0:
    print("impossible")
else:
    for i in output:
        print(*i)
