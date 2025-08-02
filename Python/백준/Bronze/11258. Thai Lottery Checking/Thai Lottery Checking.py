x = []
for i in range(6):
    x.append(tuple(input().split()))

while True:
    n = input()
    if n == "-1":
        break

    ans = 0
    if x[0][0] == n:
        ans += int(x[0][1])
    if x[1][0] == n[:3]:
        ans += int(x[1][1])
    if x[2][0] == n[:3]:
        ans += int(x[2][1])
    if x[3][0] == n[3:]:
        ans += int(x[3][1])
    if x[4][0] == n[3:]:
        ans += int(x[4][1])
    if x[5][0] == n[4:]:
        ans += int(x[5][1])
    print(ans)
