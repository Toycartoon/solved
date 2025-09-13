import re

s = "".join(re.findall("[a-z]+", input().lower()))
f = False
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        f = True

for i in range(1, len(s)-1):
    if s[i-1] == s[i+1]:
        f = True

if f:
    print("Palindrome")
else:
    print("Anti-palindrome")
