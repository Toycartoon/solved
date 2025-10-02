n = int(input())
a = list(map(int, input().split()))

a.sort()
for i in range(n, -1, -1):
    if i <= a[-i]:
        print(i)
        break
