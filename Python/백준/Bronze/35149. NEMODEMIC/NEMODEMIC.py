n, m = map(int, input().split())

check = [0, 0, 0, 0, 0, 0]  # 벽, 한방향, 모든 방향, 백신, 시작점, 탈출구
for y in range(n):
    s = input()
    for x in s:
        if x == "#":
            check[0] += 1
        elif x in "UDLR":
            check[1] += 1
        elif x == "A":
            check[2] += 1
        elif x == "V":
            check[3] += 1
        elif x == "S":
            check[4] += 1
        elif x == "E":
            check[5] += 1

if check[0] <= 1 and check[1] <= 1 and check[2] == check[3] == 0 and check[4] == check[5] == 1:
    print(1)
elif check[2] == check[3] == 0 and check[4] == check[5] == 1:
    print(2)
elif check[2] == 0 and check[4] == check[5] == 1:
    print(3)
elif check[4] == check[5] == 1:
    print(4)
else:
    print(-1)
