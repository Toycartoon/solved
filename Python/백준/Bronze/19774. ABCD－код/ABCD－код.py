for t in range(int(input())):
    a, b, c, d = [*input()]
    print("YES" if (int(a+b) ** 2 + int(c+d) ** 2) % 7 == 1 else "NO")