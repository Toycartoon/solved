while True:
    n = int(input())
    if n == 0:
        break
    
    s = {*range(1, 50)}
    for i in range(n):
        s -= set(map(int, input().split()))

    if len(s) == 0:
        print("Yes")
    else:
        print("No")
