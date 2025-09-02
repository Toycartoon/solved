for t in range(int(input())):
    n = int(input())
    b = input().replace("I", "1").replace("O", "0")

    print(f"Case #{t+1}: ", end="")
    for i in range(7, len(b), 8):
        print(chr(int(b[i-7:i+1], 2)), end="")
    print()
