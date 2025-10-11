from math import gcd

a = list(map(int, input().split()))
b = list(map(int, input().split()))

nume, deno = 0, 0
for i in a:
    for j in b:
        deno += 1
        if i > j:
            nume += 1
g = gcd(nume, deno)
print(f"{nume//g}/{deno//g}")
