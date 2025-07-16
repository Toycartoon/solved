a = input().split("|")
b = input().split("|")

a = {a[0].count("."), a[-1].count(".")}
b = {b[0].count("."), b[-1].count(".")}

print("Yes" if len(a & b) >= 1 else "No")
