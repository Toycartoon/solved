from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    n = len(queue1) + len(queue2)
    ans = 0
    while ans <= 4 * n:
        if sum1 > sum2 and len(queue1) > 0:
            x = queue1.popleft()
            sum1 -= x
            sum2 += x
            queue2.append(x)
        elif sum1 < sum2 and len(queue2) > 0:
            x = queue2.popleft()
            sum2 -= x
            sum1 += x
            queue1.append(x)
        else:
            break
        ans += 1
    
    return -1 if ans > 4 * n else ans
