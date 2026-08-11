def base_converter(n, k):
    s = ""
    while n:
        s += str(n % k)
        n //= k

    return s[::-1]

def solution(n, k):
    num = base_converter(n, k)

    ans = 0
    for i in num.split("0"):
        if len(i) == 0 or int(i) < 2:
            continue
        
        f = True
        for x in range(2, int(int(i) ** 0.5) + 1):
            if int(i) % x == 0:
                f = False
                break
        
        if f:
            ans += 1

    return ans