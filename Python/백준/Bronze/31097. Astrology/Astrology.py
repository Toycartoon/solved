y, m, d = map(int, input().split("-"))
v = m * 100 + d
if 120 <= v <= 218:
    print("Aquarius")
elif 219 <= v <= 320:
    print("Pisces")
elif 321 <= v <= 419:
    print("Aries")
elif 420 <= v <= 520:
    print("Taurus")
elif 521 <= v <= 620:
    print("Gemini")
elif 621 <= v <= 722:
    print("Cancer")
elif 723 <= v <= 822:
    print("Leo")
elif 823 <= v <= 922:
    print("Virgo")
elif 923 <= v <= 1022:
    print("Libra")
elif 1023 <= v <= 1122:
    print("Scorpio")
elif 1123 <= v <= 1221:
    print("Sagittarius")
else:
    print("Capricorn")
