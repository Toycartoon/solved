for t in range(int(input())):
    n = int(input())
    x, y = map(float, input().split())

    x1, y1, x2, y2 = x, y, x, y
    for i in range(n-1):
        x, y = map(float, input().split())

        x1 = min(x, x1)
        y1 = min(y, y1)
        x2 = max(x, x2)
        y2 = max(y, y2)

    print(f"Case {t+1}: Area {(x2-x1) * (y2-y1)}, Perimeter {2 * (x2-x1) + 2 * (y2-y1)}")
