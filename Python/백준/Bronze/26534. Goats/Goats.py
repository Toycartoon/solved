a = list(map(int, input().split()))
b = list(map(int, input().split()))

nume = 0
deno = 0
for i in a:
    for j in b:
        if i != j:
            deno += 1
        if i > j:
            nume += 1
print(f"{nume / deno:.5f}")
