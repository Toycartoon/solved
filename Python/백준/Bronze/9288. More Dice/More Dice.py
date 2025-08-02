import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    print(f"Case {t+1}:")
    for i in range(1, 7):
        for j in range(6, 0, -1):
            if i + j == n and i <= j:
                print(f"({i},{j})")
