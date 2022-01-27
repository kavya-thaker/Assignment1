k = input()
lst = list(map(int, input().split()))
i = set()
j = set()
for s in lst:
    if s in i:
        j.add(s)
    else:
        i.add(s)

s1 = i.difference(j)
print(*s1)
