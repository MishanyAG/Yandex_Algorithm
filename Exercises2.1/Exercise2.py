size  = int(input())
data = list(map(int, input().split()))

maxAnswear = [0, 0]
minAnswear = [0, 0]


maxLeft = float('-inf')
minLeft = float('inf')
maxDiff = float('-inf')
minDiff = float('inf')
maxIndex = 0
minIndex = 0

for i in range(size-1):
    j = i + 1
    if maxLeft < data[i]:
        maxLeft = data[i]
        maxIndex = i
    if minLeft > data[i]:
        minLeft = data[i]
        minIndex = i
    if maxDiff < maxLeft - data[j]:
        maxDiff = maxLeft - data[j]
        maxAnswear = [maxIndex, j]
    if minDiff > minLeft - data[j]:
        minDiff = minLeft - data[j]
        minAnswear = [minIndex, j]

print(f"{minAnswear[0]+1} {minAnswear[1]+1}")
print(f"{maxAnswear[0]+1} {maxAnswear[1]+1}")

"""
Массив может быть чётным или нечётным, учитывая это что мы можем сделать?
Как нам сделать из O(n^2) -> O(n)
Нужно сократить проходы по циклы до одного.
Мы будем идти по циклу сравнивая
"""

