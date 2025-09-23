for t in range(int(input())):
    b, p = map(float, input().split())
    bpm = 60 * (b / p)
    x = bpm / b
    print(bpm - x, bpm, bpm + x)
