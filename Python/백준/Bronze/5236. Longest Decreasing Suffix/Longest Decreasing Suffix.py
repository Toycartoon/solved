for t in range(int(input())):
    s = input()

    ans = s[-1]
    s = s[::-1]
    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            ans += s[i]
        else:
            break

    print(f"The longest decreasing suffix of {s[::-1]} is {ans[::-1]}")
