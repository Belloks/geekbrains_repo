# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

firstname = input('First name ')
lastname = input('Last name ')
year = int(input('Year of Birth '))
city = input('Enter your city ')
mail = input('Enter your email ')
phone = input('Enter your telephone ')

def f(firstname, lastname, year, city, mail, phone):
    v=[firstname, lastname, year, city, mail, phone]
    s='; '.join (v)
    return (s)