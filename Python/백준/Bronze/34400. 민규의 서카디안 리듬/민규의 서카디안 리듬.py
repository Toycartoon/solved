for t in range(int(input())):
    n = int(input()) % 25
    if n <= 16:
        print("ONLINE")
    else:
        print("OFFLINE")
