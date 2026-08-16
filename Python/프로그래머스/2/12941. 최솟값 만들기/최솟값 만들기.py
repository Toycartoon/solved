def solution(a, b):
    a.sort()
    b.sort()
    
    ar, br = 0, 0
    for i in range(len(a)):
        br += a[i] * b[-i-1]
        ar += b[i] * a[-i-1]
    
    return min(ar, br)
