from collections import Counter

n = int(input())
a = list(map(int, input().split()))
print("No" if Counter(a).most_common(1)[0][1] >= 3 else "Yes")
