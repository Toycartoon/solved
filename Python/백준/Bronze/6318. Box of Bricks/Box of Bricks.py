t = 1
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))

    s = sum(a) // n
    ans = 0
    for i in a:
        ans += abs(i - s)

    print(f"Set #{t}")
    print(f"The minimum number of moves is {ans // 2}.")
    print()

    t += 1
