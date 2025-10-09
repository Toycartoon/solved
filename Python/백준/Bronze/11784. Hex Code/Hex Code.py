while True:
    try:
        s = input()
        for i in range(1, len(s)+1, 2):
            print(chr(int(s[i-1:i+1], 16)), end="")
        print()
    except EOFError:
        break
