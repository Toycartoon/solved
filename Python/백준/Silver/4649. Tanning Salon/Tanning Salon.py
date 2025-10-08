while True:
    n, *s = input().split()
    if n == "0":
        break

    v = set()
    a = 0
    for i in s[0]:
        if i in v:
            v.remove(i)
        else:
            if len(v) >= int(n):
                a += 1
            else:
                v.add(i)

    if a == 0:
        print("All customers tanned successfully.")
    else:
        print(f"{a // 2} customer(s) walked away.")
