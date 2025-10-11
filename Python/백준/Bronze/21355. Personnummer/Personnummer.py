s = input()
if "-" in s:
    if int(s[:2]) < 20:
        print("20" + "".join(s.split("-")))
    else:
        print("19" + "".join(s.split("-")))
else:
    if int(s[:2]) < 20:
        print("19" + "".join(s.split("+")))
    else:
        print("18" + "".join(s.split("+")))
