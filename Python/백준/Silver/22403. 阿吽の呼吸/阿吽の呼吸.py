q = 0
f = True
for i in range(int(input())):
    s = input()
    if s == "A":
        q += 1
    elif s == "Un":
        if q == 0:
            f = False
            break
        q -= 1

if q > 0 or not f:
    print("NO")
else:
    print("YES")
