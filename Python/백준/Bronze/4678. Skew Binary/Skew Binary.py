while True:
    n = input()
    if n == "0":
        break

    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (2 ** (len(n)-(i))-1)
    print(ans)
