n = input()
if len(n) == 1:
    print(n)
    exit()

if int(n[1]) >= 5:
    print(int(n[0])+1, "0" * len(n[1:]), sep="")
else:
    print(n[0] + "0" * len(n[1:]))
