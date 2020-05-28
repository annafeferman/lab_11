f = open('f.txt', 'r', encoding='utf-8')  # открываем файл ф для чтения
g = open('g.txt', 'r+', encoding='utf-8')  # открываем g для письма
for row in f:
    if len(row) > 30:  # проходимся по рядам циклом, проверяя длинну
        g.write(row)  # при выполнении условия записываем нужную строку в файл g
    else:
        continue

print(g.read())  # выводим результат
g.close()  # очищаем и закрываем файл
