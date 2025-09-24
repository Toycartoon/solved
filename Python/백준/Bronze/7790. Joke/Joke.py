ans = 0
while True:
    try:
        s = input()
        ans += s.count("joke")
    except EOFError:
        break
print(ans)
