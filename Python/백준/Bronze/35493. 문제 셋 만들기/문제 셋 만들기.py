n = int(input())
d = list(map(int, input().split()))

if n == 1 and sum(d) % 2 == 1:
    print("NO")
else:
    print("YES")
