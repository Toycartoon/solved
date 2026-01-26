n = int(input())
a = list(map(int, input().split()))

oey = 0
odd = True
eyo = 0
even = True

for i in a:
    if i % 2 == 0:
        if even:
            even = False
            eyo += 1
        if not odd:
            odd = True
            oey += 1
    else:
        if odd:
            odd = False
            oey += 1
        if not even:
            even = True
            eyo += 1
print(max(oey, eyo))
