n = int(input())
a  = list(map(float, input().split()))
b = {}
for i in range(n-2):
    if a[i] > a[i+1] and a[i+1]<a[i+2]:
        b[i+1] = a[i+1]
for i in reversed(b):
    del a[i]
a = list(map(int, a))
print(len(a))
print(*a)
# 1 2 3 4 5 - всего 5 прыжков по каждому числу
# 1 2 3 4 5 - если начинаем со 2-го будет 4, если убираем послендий элемент то будет 3