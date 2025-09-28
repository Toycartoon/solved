n, m = map(int, input().split())

a = m // 26
b = m % 26

if a == 0 or a == 1 and b == 0:
    print(f"SN {n}{chr(b + 64) if b != 0 else "Z"}")
elif a > 26:
    print(f"SN {n}zz")
else:
    if b == 0:
        print(f"SN {n}{chr(a+95)}z")
    else:
        print(f"SN {n}{chr(a + 96)}{chr(b + 96)}")
