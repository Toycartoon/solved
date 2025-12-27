for t in range(int(input())):
    x = int(input())
    s = input()

    s = s.replace("!", "10")
    ans = eval(s)

    if ans >= 10:
        print("!")
    else:
        print(ans)
