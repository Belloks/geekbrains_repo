a = input("Введите число в секундах: ")
a = int(a)

hours = a // 3600
scnd = a % 3600
minutes = scnd // 60
seconds = scnd % 60

print(f"{a} секунд это в формате 'чч:мм:сс' - {hours:02}:{minutes:02}:{seconds:02}")
print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))