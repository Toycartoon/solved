n = int(input())
a = list(map(int, input().split()))

mn = min(a)
mx = max(a)
for i in a:
    if i != mn and i != mx:
        print(max(abs(i - mn), abs(i - mx)))
    elif i == mn:
        print(mx-i)
    elif i == mx:
        print(i-mn)
