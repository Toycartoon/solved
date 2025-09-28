for t in range(int(input())):
    row, col, w, h = map(int, input().split())
    print(f"Case #{t+1}:")
    for i in range(row):
        print(("+" + "-" * w) * col + "+")
        for j in range(h):
            print(("|" + "*" * w) * col + "|")
    print(("+" + "-" * w) * col + "+")
