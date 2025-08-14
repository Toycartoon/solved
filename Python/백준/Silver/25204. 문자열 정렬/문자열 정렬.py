import sys

input = sys.stdin.readline

for t in range(int(input())):
    a = []
    for i in range(int(input())):
        a.append(input().strip())

    a.sort(key=lambda x: ["AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-".index(i) for i in x])
    for i in a:
        print(i)
