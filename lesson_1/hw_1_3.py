a = input("Введите целое число n в диапазоне [0, 10)  ")

if str(a).isdigit():
    print('Это число', a)
if not str(a).isdigit():
    print('Это не число')

if str(a).isdigit():
    print('Это число ' + str(a))
else:
    print('Это не число')

n = str(a)
nn = n+n
nnn = nn+n

res = int(n) + int(nn) + int(nnn)
print('Сумма чисел n + nn + nnn = ', res)