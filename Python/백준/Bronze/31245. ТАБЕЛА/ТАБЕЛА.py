cena1, cena2, cena3 = input().split()
ans = cena1
if cena1[-1] == cena2[0]:
    ans += f"\'{cena2[1:]}"
else:
    ans += cena2

if cena2[-1] == cena3[0]:
    ans += f"\'{cena3[1:]}"
else:
    ans += cena3

print(ans)
