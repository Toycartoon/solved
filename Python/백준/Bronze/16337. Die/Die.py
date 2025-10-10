g = tuple(input() for _ in range(3))
a = {(":::", ":o:", ":::"): 1, ("o::", ":::", "::o"): 2, ("::o", ":::", "o::"): 2, ("o::", ":o:", "::o"): 3,
     ("::o", ":o:", "o::"): 3, ("o:o", ":::", "o:o"): 4, ("o:o", ":o:", "o:o"): 5, ("o:o", "o:o", "o:o"): 6,
     ("ooo", ":::", "ooo"): 6}

if g in a:
    print(a[g])
else:
    print("unknown")
