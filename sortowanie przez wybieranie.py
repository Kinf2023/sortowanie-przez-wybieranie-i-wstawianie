l = [5,4,6,8,2,6]

for a in range(0, len(l) - 1):
    b = a
    for c in range(a + 1, len(l)):
        if l[c] < l[b]:
            b = c

    l[b], l[a] = l[a], l[b]
print(l)
