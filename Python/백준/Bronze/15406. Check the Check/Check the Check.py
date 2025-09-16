ans = 0
while True:
    s = input()
    if s == "TOTAL":
        break
    d, t = map(int, input().split())
    ans += d * t

if ans >= int(input()):
    print("PAY")
else:
    print("PROTEST")
