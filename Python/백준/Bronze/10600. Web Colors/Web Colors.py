w = [(255, 255, 255, 1, "White"), (192, 192, 192, 2, "Silver"), (128, 128, 128, 3, "Gray"), (0, 0, 0, 4, "Black"),
     (255, 0, 0, 5, "Red"), (128, 0, 0, 6, "Maroon"), (255, 255, 0, 7, "Yellow"), (128, 128, 0, 8, "Olive"),
     (0, 255, 0, 9, "Lime"), (0, 128, 0, 10, "Green"), (0, 255, 255, 11, "Aqua"), (0, 128, 128, 12, "Teal"),
     (0, 0, 255, 13, "Blue"), (0, 0, 128, 14, "Navy"), (255, 0, 255, 15, "Fuchsia"), (128, 0, 128, 16, "Purple")]

while True:
    r, g, b = map(int, input().split())
    if r == g == b == -1:
        break

    ans = ""
    idx = float('inf')
    dist = float('inf')
    for i in range(16):
        d = ((w[i][0]-r) ** 2 + (w[i][1]-g) ** 2 + (w[i][2]-b) ** 2) ** 0.5
        if dist > d or (dist == d and idx > w[i][3]):
            dist = d
            idx = w[i][3]
            ans = w[i][-1]
    print(ans)
