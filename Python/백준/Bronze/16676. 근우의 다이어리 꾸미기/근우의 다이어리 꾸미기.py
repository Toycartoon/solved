n = int(input())
i = 1
while True:
    if int("1" * (i-1) + "0") <= n <= int("1" * i + "0"):
        print(i)
        break
    i += 1
