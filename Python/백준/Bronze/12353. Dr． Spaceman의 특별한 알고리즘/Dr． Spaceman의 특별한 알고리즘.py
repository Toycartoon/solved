for t in range(int(input())):
    gen, mom, dad = input().split()
    m = int(mom.split("\'")[0]) * 12 + int(mom.split("\'")[1][:-1])
    d = int(dad.split("\'")[0]) * 12 + int(dad.split("\'")[1][:-1])

    a = (d + m + (5 if gen == "B" else -5))
    mn, mx = (a + 1) // 2 - 4, a // 2 + 4
    print(f"Case #{t+1}: {mn // 12}\'{mn % 12}\" to {mx // 12}\'{mx % 12}\"")
