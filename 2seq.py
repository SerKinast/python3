# вводим элементы
elements = (input('введите элементы через запятую: '))

# заменяем символы в случае, если  пользователь использует разные разделители
elements = elements.replace(' ', '/')
elements = elements.replace(';', '/')
elements = elements.replace(',', '/')
# пробовал замену в одну строку через оператор "and", но из трех условий, почему то одно условие пропускается...
# не знаю, почему

# переводим строку в список
elements = elements.split('/')

# формируем и выводим список уникальных элементов
result = []
for element in elements:
    if elements.count(element) == 1:
        result.append(element)
print(result)
