ml, mr, tl, tr = input().split()

if ml != mr and tl != tr:
    print("?")
elif ml == mr:
    if ml == "R":
        if tl == "P" or tr == "P":
            print("TK")
        elif tl == "R" or tr == "R":
            print("?")
        else:
            print("MS")
    elif ml == "S":
        if tl == "R" or tr == "R":
            print("TK")
        elif tl == "S" or tr == "S":
            print("?")
        else:
            print("MS")
    elif ml == "P":
        if tl == "S" or tr == "S":
            print("TK")
        elif tl == "P" or tr == "P":
            print("?")
        else:
            print("MS")
elif tl == tr:
    if tl == "R":
        if ml == "P" or mr == "P":
            print("MS")
        elif ml == "R" or mr == "R":
            print("?")
        else:
            print("TK")
    elif tl == "S":
        if ml == "R" or mr == "R":
            print("MS")
        elif ml == "S" or mr == "S":
            print("?")
        else:
            print("TK")
    elif tl == "P":
        if ml == "S" or mr == "S":
            print("MS")
        elif ml == "P" or mr == "P":
            print("?")
        else:
            print("TK")
