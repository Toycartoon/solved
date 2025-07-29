point = []
ans = 0

for i in range(5):
    point.append(int(input()))

for j in range(len(point)):
    ans += point[j]

print(ans)