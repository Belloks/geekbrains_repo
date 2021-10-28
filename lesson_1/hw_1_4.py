a = input("Введите целое число n в диапазоне [100:]  ")
a = str(a)

v = []
for i in range(len(a)):
    v.append(int(a[i]))

v = [int(a[x]) for x in range(len(a))]

v = [int(x) for x in a]

ind = v.index(max(v))

print('Самая большая цифра в числе: {} и находится на {} позиции, отсчет с нуля'.format(max(v), ind))

a = input("Введите целое число n: ")
v = [int(x) for x in a]
print('Самая большая цифра в числе: {}'.format(max(v)))