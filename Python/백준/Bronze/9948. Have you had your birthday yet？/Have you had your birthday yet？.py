while True:
    d, m = input().split()
    if d == "0" and m == "#":
        break

    if m == "February" and d == "29":
        print("Unlucky")
    elif m in ("January", "February", "March", "April", "May", "June", "July"):
        print("Yes")
    elif m == "August":
        if int(d) < 4:
            print("Yes")
        elif int(d) > 4:
            print("No")
        else:
            print("Happy birthday")
    else:
        print("No")
