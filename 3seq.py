# Вводим первую строку
elements1 = (input('введите элементы 1-го списка через запятую: '))

# Вводим вторую строку
elements2 = (input('введите элементы 2-го списка через запятую: '))

# Переводим строки в список
elist1 = elements1.split(',')
elist2 = elements2.split(',')

# с помощью 'set'
unique = (set(elist1) - set(elist2))
print(unique)

# С помощью цикла
# Создаем новый список
add_list = []

# Проверяем, НЕТ ли переменной во втором списке,
# Если условие верное, добавляем в  новый список
for num in elist1:
    if num not in elist2:
        add_list.append(num)

print(add_list)
