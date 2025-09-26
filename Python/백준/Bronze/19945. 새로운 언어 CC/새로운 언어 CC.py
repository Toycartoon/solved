n = int(input())
if n >= 0:
    print(len(bin(n)[2:]))
else:
    print(32)
