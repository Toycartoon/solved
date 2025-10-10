while True:
    try:
        n = bin(int(input()))[2:]
        if n.count("0") > n.count("1"):
            print("left")
        elif n.count("0") < n.count("1"):
            print("right")
        else:
            print("straight")
    except EOFError:
        break
