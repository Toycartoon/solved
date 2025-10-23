n = int(input())
a, b = map(int, input().split())
if a + b > n:
    k = a+b-n
else:
    k = n-(a+b)

ans = 0
for i in range(n-1, k-1, -1):
    ans += pow(2, i)
print(ans)
