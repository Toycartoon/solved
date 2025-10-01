s = input().lower()
kangaroo, kiwi = 0, 0

for i in s:
    kangaroo += "kangaroo".count(i)
    kiwi += "kiwibird".count(i)

if kangaroo > kiwi:
    print("Kangaroos")
elif kangaroo < kiwi:
    print("Kiwis")
else:
    print("Feud continues")
