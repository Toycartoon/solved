from math import lcm

def solution(numbers):
    num = set()
    for i in numbers:
        num.add(len(str(i)))
    
    c = lcm(*num)
    arr = sorted(numbers, key=lambda x: (c * str(x)), reverse=True)
    
    ans = ""
    for i in arr:
        ans += str(i)
    
    if ans[0] == "0":
        return "0"
    return ans
