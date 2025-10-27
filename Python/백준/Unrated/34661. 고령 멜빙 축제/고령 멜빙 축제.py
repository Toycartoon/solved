for t in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += input().count(".")

    if ans % 2 == 0:
        print("pizza")
    else:
        print("sewon")
