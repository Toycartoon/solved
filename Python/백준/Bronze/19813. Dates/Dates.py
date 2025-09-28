for t in range(int(input())):
    s = input()
    if "." in s:
        d, m, y = map(int, s.split("."))
    elif "/" in s:
        m, d, y = map(int, s.split("/"))
    print(f"{str(d).zfill(2)}.{str(m).zfill(2)}.{str(y).zfill(4)}", f"{str(m).zfill(2)}/{str(d).zfill(2)}/{str(y).zfill(4)}")
