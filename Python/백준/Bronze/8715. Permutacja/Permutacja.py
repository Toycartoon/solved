n = int(input())
a = set(map(int, input().split()))
print("TAK" if len({*range(1,n+1)}-a) == 0 else "NIE")
