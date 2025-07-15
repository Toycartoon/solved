n, m = map(int, input().split())
for y in range(n):
    if y % 2 == 0:
        for x in range(2, m+1, 2):
            print(f"? {y+1} {x}", flush=True)
            s = int(input())

            if s == 1:
                exit()
    else:
        for x in range(1, m+1, 2):
            print(f"? {y+1} {x}", flush=True)
            s = int(input())

            if s == 1:
                exit()
