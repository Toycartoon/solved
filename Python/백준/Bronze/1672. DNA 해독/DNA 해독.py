w = {("A", "A"): 'A', ("A", "G"): "C", ("A", "C"): "A", ("A", "T"): "G",
     ("G", "A"): "C", ("G", "G"): "G", ("G", "C"): "T", ("G", "T"): "A",
     ("C", "A"): "A", ("C", "G"): "T", ("C", "C"): "C", ("C", "T"): "G",
     ("T", "A"): "G", ("T", "G"): "A", ("T", "C"): "G", ("T", "T"): "T"}

n = int(input())
s = [*input()]
while len(s) > 1:
    v = s.pop()
    s.append(w[(s.pop(), v)])

print(s[0])
