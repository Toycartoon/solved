import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
snake = []
for i in range(b):
    s, e = map(int, input().split())
    snake.append((s, e))

pos = [1 for _ in range(a)]
for i in range(c):
    n = int(input())
    p = pos[i % a] + n

    for s, e in snake:
        if p == s:
            p = e
            break

    if p >= 100:
        pos[i % a] = 100
        break
    pos[i % a] = p

for i in range(a):
    print(f"Position of player {i+1} is {pos[i]}.")
