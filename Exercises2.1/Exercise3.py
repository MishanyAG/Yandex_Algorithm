n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
slovar = {}
for i in range(n):
    slovar.setdefault(a[i], i)

for i in range(q):
    if x[i] in slovar:
        print(slovar[x[i]]+1)
    else:
        print(-1)

"""
Что от нас требуется?
Нужно найти первые вхождения чисел x в массиве a, индексы в задаче как всегда увеличены на единицу... Зачем-то.
На первый взгляд сложность O(n)^2
Проблема состоит в выводе -1 при не найденном значении
"""
