while True:
    s = input()
    if s == "I quacked the code!":
        break
    if s[-1] == ".":
        print("*Nod*")
    elif s[-1] == "?":
        print("Quack!")
