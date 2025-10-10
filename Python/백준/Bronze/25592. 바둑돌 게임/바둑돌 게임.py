n = int(input())
v = 0
while True:
    v += 1
    s = v * (v+1) // 2
    if s > n:
        if v % 2 == 1:
            print(s - n)
        else:
            print(0)
        break
