a = []
for i in range(int(input())):
    s = input()
    if s == "Present!":
        a.pop()
    else:
        a.append(s)

if len(a) == 0:
    print("No Absences")
else:
    for i in a:
        print(i)
