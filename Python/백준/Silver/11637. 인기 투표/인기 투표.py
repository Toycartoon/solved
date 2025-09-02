import sys

input = sys.stdin.readline

for t in range(int(input())):
    a = []
    for i in range(int(input())):
        a.append(int(input()))

    if a.count(max(a)) == 1 and max(a) > sum(a) // 2:
        print(f"majority winner {a.index(max(a))+1}")
    elif a.count(max(a)) == 1 and max(a) <= sum(a) // 2:
        print(f"minority winner {a.index(max(a))+1}")
    else:
        print("no winner")
