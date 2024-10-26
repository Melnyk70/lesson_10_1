# ДЗ 10.1. Форматування тексту з snake_case на CamelCase
# Написати програму, яка перетворює ім`я змінної у форматі snake_case у формат CamelCase.
# Вивести результат за допомогою print. Доповнити код:
# s = input()
# your code here
s = input("Введіть текст з стилем snake_case:")
new_s = s.replace("_"," ")
new_s = new_s.title()
s = new_s.replace(" ","")
print("Відформатований текст з стилем CamelCase:   ", s)