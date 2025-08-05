s, e = map(int, input().split())
for i in range(s, e+1):
    if str(i) == str(i)[::-1]:
        print("Palindrome!")
    else:
        print(i)
