s = input()
print(26-len({*s}) if 26-len({*s}) > 0 else "impossible")