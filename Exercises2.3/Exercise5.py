n = int(input())
a = []
unic = 0
for i in range(n):
    a.append(list(input()))

for i in range(n):
    for j in range(i+1, n):
        death = 0
        for z in range(len(a[i])):
            if a[i][z] != a[j][z]:
                death += 1
            if death > 1:
                break
        if death == 1:
            unic += 1
print(unic)

#Не оптимиизровал :P




# n = int(input())
# a = []
# sample = {}
# unic = 0
# for i in range(n):
#     a.append(input())

# #Делаем словарь с пропусками
# for i in range(n):
#     for j in range(len(a[i])):
#         sample.update({a[i][:j] + "_" + a[i][j+1:]: 0})
# print(f"Словарь готов - {sample}")


# #Проверяем наличие слов в словаре
# for i in range(n):
#     print(f"Сейчас смотртят на слово {a[i]}")
#     for j in range(len(a[i])):
#         print(f"Его вариация {a[i][:j] + "_" + a[i][j+1:]}. Есть ли в словаре = {a[i][:j] + "_" + a[i][j+1:] in sample}")
#         sample[a[i][:j] + "_" + a[i][j+1:]] = sample.get(a[i][:j] + "_" + a[i][j+1:], 0) + 1
#         unic += 1

# print(sample)
# print(unic)