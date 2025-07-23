n = int(input())
a = list(map(int, input().split()))

mx = max(a)
for i in range(n):
    if mx == a[i]:
        print(chr(i+65), end="")
