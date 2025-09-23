while True:
    name, font = input().split()
    if name == "#" and font == "0":
        break

    print(f"{name} Library")
    for f in range(int(input())):
        w, s = input().split()
        
        if int(w) - (len(s) * int(font) + 2) < 0:
            print(f"Book {f+1} vertical")
        else:
            print(f"Book {f+1} horizontal")
