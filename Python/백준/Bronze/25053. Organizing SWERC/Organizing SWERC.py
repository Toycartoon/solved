for t in range(int(input())):
    n = int(input())

    a = []
    for i in range(n):
        b, d = map(int, input().split())
        a.append((b, d))

    a.sort(key=lambda x: -x[0])
    ans = [-1 for _ in range(10)]

    for b, d in a:
        if ans[d-1] == -1:
            ans[d-1] = b

    if -1 in ans:
        print("MOREPROBLEMS")
    else:
        print(sum(ans))
