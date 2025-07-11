import sys

input = sys.stdin.readline

for t in range(int(input())):
    _ = input() # 나는 빈 공백이 싫다
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    ps = [0]
    v = 0
    for i in a:
        v += i
        ps.append(v)

    for x in range(q):
        i, j = map(int, input().split())
        print(ps[j+1]-ps[i])
    print()
