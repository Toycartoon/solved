s = input()

if "+" in s:
    s = s.split("+")
else:
    print("No Money")
    exit()

if s[0].isnumeric() and s[1].isnumeric() and s[0] == s[1] and not s[0].startswith("0") and not s[1].startswith("0"):
    print("CUTE")
else:
    print("No Money")
