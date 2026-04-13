a, b = map(int, input().split())
if a == 0:
    print(b)
elif b == 0:
    if a == 1:
        print(f"x")
    elif a == -1:
        print("-x")
    else:
        print(f"{a}x")
else:
    if a == 1:
        print(f"x{b if b < 0 else f'+{b}'}")
    elif a == -1:
        print(f"-x{b if b < 0 else f'+{b}'}")
    else:
        print(f"{a}x{b if b < 0 else f'+{b}'}")
