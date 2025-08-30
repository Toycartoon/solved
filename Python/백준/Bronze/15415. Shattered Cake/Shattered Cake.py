import sys

input = sys.stdin.readline

w = int(input())
n = int(input())

a = 0
for i in range(n):
    wi, li = map(int, input().split())
    a += wi * li

print(a // w)
