while True:
    name, z = input().split()
    if name == "#" and z == "0":
        break

    p = int(input())
    for i in range(int(input())):
        _out, _in = map(int, input().split())
        p -= _out
        p = min(int(z), p+_in)
    print(name, p)
