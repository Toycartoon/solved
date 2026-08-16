def solution(s):
    ans = []
    for i in s.split(' '):
        ans.append(i.capitalize())
    
    return " ".join(ans)
