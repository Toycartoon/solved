def solution(s):
    ans = True
    q = 0
    for i in s:
        if i == "(":
            q += 1
        elif i == ")":
            if q < 1:
                ans = False
                break
            else:
                q -= 1
    
    return (not q) and ans
