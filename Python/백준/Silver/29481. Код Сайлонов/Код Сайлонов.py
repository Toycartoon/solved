n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c11, c12, c21, c22 = map(int, input().split())

b = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == j == 0:
            b[i][j] = a[i][j] // c22
        elif i == 0:
            b[i][j] = (a[i][j] - b[i][j-1] * c21) // c22
        elif j == 0:
            b[i][j] = (a[i][j] - b[i-1][j] * c12) // c22
        else:
            b[i][j] = (a[i][j] - b[i-1][j-1] * c11 - b[i-1][j] * c12 - b[i][j-1] * c21) // c22

for v in b:
    print(*v)
