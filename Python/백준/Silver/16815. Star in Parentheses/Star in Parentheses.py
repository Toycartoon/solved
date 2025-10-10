s = input()
q = 0
for i in s:
    if i == "(":
        q += 1
    elif i == ")":
        q -= 1
    elif i == "*":
        print(q)
        break
