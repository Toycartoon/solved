q = []

f = True
for i in range(int(input())):
    com, x = input().split()
    if com == "Add":
        q.append(x)
    elif com == "Vote":
        if len(q) >= 1:
            v = q.pop()
            if v != x:
                f = False
                break
        else:
            f = False
            break

print("Yes" if len(q) == 0 and f else "No")
