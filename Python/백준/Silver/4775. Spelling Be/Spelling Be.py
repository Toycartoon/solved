s = set()
for i in range(int(input())):
    s.add(input())

for t in range(int(input())):
    f = True
    a = []
    while True:
        v = input()
        if v == "-1":
            break

        if v not in s:
            f = False
            a.append(v)

    if f:
        print(f"Email {t+1} is spelled correctly.")
    else:
        print(f"Email {t+1} is not spelled correctly.")
        for i in a:
            print(i)
print("End of Output")
