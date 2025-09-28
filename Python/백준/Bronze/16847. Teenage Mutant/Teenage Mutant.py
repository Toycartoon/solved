for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    nume, deno = 0, k
    a = []
    for i in range(n):
        a.append(input())

    for i in range(k):
        if s[i] not in list(zip(*a))[i]:
            nume += 1

    print(f"Data Set {t+1}:")
    print(f"{nume}/{deno}")
    print()
