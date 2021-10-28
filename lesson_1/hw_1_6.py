a, b = input("Введите значения a и b через пробел : ").split()
print("a = {} и b = {} ".format(a, b))

per = int(a)
i = 1
while per <= int(b):
    per = per + per*0.1
    i += 1
print('На {} день спортсмен достиг результата — не менее {} км.'.format(i, b))

N = int(a)*int(b)
per = int(a)
for i in range(1, N):
    per = per + per*0.1
    if per >= int(b):
        break
print('На {} день спортсмен достиг результата — не менее {} км.'.format(i+1, b))