n = int(input())
temp = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c, d = 1, 1, 1, 1
            for v in range(i):
                a *= temp[v]

            for v in range(i, j):
                b *= temp[v]

            for v in range(j, k):
                c *= temp[v]

            for v in range(k, n):
                d *= temp[v]

            ans = max(ans, a+b+c+d)

print(ans)
