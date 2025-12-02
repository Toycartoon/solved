n = int(input())
a = list(map(int, input().split()))

if a.count(2) <= a.count(1) and (a.count(1) - a.count(2)) % 3 == 0:
    print("Yes")
else:
    print("No")
