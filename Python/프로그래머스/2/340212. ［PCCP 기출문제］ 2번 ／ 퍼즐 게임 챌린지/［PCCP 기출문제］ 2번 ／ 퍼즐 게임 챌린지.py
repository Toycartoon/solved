def solution(diffs, times, limit):
    l, r = 0, limit+1
    
    while l + 1 < r:
        mid = (l + r) // 2  # 숙련도
        time = 0
        
        for i in range(len(diffs)):
            if mid >= diffs[i]:
                time += times[i]
            else:
                time += (times[i] + times[i-1]) * (diffs[i]-mid) + times[i]
        
        if time <= limit:
            r = mid
        else:
            l = mid
    return r