while True:
    q = []

    s = input()
    if s == "#":
        break

    f = True
    for i in s:
        if i not in "(){}[]":
            continue

        if i in "({[":
            q.append(i)
        elif i in ")}]":
            if len(q) == 0:
                f = False
                break
            v = q.pop()
            if (i == ")" and v != "(") or (i == "}" and v != "{") or (i == "]" and v != "["):
                f = False
                break

    print("Legal" if len(q) == 0 and f else "Illegal")
