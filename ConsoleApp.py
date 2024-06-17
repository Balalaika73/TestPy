import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Вводим переменные с клавиатуры
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
city = input("Введите ваш город проживания: ")

# Выводим информацию
print("Привет, меня зовут", name)
print("Мне", age, "лет")
print("Я живу в городе", city)
