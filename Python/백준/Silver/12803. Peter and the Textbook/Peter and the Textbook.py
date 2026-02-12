for t in range(int(input())):
    n, q = map(int, input().split())
    p = [i+1 for i in range(n)]
    
    for i in range(q):
        c, v = input().split()
        
        if c == "-":
            p[int(v)-1] = 0
            p[n-int(v)] = 0
        elif c == "?":
            ans = 0
            for x in p:
                if x != 0:
                    ans += 1
                    if ans == int(v):
                        print(x)
                        break
