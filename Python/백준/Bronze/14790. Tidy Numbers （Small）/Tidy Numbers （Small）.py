for t in range(int(input())):
    n = input()
    for i in range(int(n), 0, -1):
        f = True
        for j in range(1, len(str(i))):
            if int(str(i)[j-1]) > int(str(i)[j]):
                f = False
                break

        if f:
            print(f"Case #{t+1}: {i}")
            break
