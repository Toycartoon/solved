n = int(input())
a = list(map(int, input().split()))
odd = 0
for i in a:
    if i % 2 == 1:
        odd += 1

print(int(not ((odd == 2 and (a[0] % 2 == a[-1] % 2 == 1)) or (odd == 0 and n == 1))))
