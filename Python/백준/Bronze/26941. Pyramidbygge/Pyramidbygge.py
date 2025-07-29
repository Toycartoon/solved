n = int(input())
x = 1
idx = 3
ans = 1
while True:
    if x > n:
        print(ans-1)
        break
    ans += 1
    x += idx ** 2
    idx += 2
