n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split()[1:])))
setA = set(frozenset(item) for item in a)
base = frozenset.intersection(*setA)
base = [int(item) for item in base]
result = [item for sublist in a for item in sublist if item not in base]
if len(set(result)) == len(result):
    if base:
        print("YES")
        print(len(base))
    for i in range(n):
        print(len(set(a[i]).difference(set(base))), end = ' ')
else:
    print("NO")


#Решил. Но не проходит по времени. Оставим до лушчих времён. :)