for n in range(int(input())):
    c = int(input())
    p = int(input())
    i = list(map(int, input().split()))
    
    print(f"Case #{n+1}: ", end="")
    for v in range(p):
        if c-i[v] in i[v+1:]:
            print(v+1, i[v+1:].index(c-i[v])+v+2)
            break
