def solution(h1, m1, s1, h2, m2, s2):
    ans = 0
    
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    if start == 0 or start == 43200:
        ans += 1
    
    while start < end:
        h = start / 120 % 360
        m = start / 10 % 360
        s = start * 6 % 360
        
        nxt_h = 360 if (start + 1) / 120 % 360 == 0 else (start + 1) / 120 % 360
        nxt_m = 360 if (start + 1) / 10 % 360 == 0 else (start + 1) / 10 % 360
        nxt_s = 360 if (start + 1) * 6 % 360 == 0 else (start + 1) * 6 % 360
            
        if s < h and nxt_h <= nxt_s:
            ans += 1
        
        if s < m and nxt_m <= nxt_s:
            ans += 1
        
        if nxt_s == nxt_h == nxt_m:
            ans -= 1
        
        start += 1
    
    return ans
