import re

p = re.compile("[What is][a-z ',;]*[?]")
s = input()

for i in re.findall(p, s):
    print(i.replace("What", "Forty-two").replace("?", "."))
