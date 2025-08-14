for t in range(int(input())):
    n, *a = input().split()
    ans = []
    v = 0
    for i in a:
        if i == "X":
            v += 1
        else:
            ans.append(v)
            v = 0
    ans.append(v)
    print(f"The longest contiguous subsequence of X's is of length {max(ans)}")
