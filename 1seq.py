
# Пользователь вводит количество элементов будущего списка

count = int(input('введите количество элементов: '))
seq = [i for i in range(0, count)]

# По очереди формируются вопросы для ввода цифр по одной, каждый новый ответ добавляется в список ответов

answers = []
for i in seq:
    question = ('введите ' + str(i + 1) + ' элемент (целое число): ')
    print(question)
    answer = int(input())
    answers.append(answer)

# Полученный список ответов сортируется и выводится на экран

view = answers.sort()
print('Вывод:', answers)
