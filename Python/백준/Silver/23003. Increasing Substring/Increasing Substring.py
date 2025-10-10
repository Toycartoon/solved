for t in range(int(input())):
    n = int(input())
    s = input()

    v = 1
    print(f"Case #{t+1}: ", end="")
    for i in range(1, n):
        print(v, end=" ")
        if s[i-1] < s[i]:
            v += 1
        else:
            v = 1
    print(v)
