data_structure = [                                          # наше множество (издевательство)
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate(elems, summ=0):                               # создаём функцию с аргументами elem(отвечает за каждое перебраное значение) и сумма - summ
    if isinstance(elems, int):                              # суммируем числа
        summ += elems
    elif isinstance(elems, str):                            # преобразуем строки в числа по их длинне
        summ = calculate(len(elems), summ)
    elif isinstance(elems, set):                            # перебираем множества
        for i in elems:
            summ = calculate(i, summ)
    elif isinstance(elems, list):                           # перебирем списки
        for k in elems:
            summ = calculate(k, summ)
    elif isinstance(elems, dict):                           # перебирем словари
        for key, value in elems.items():
            summ = calculate(key, summ)
            summ = calculate(value, summ)
    elif isinstance(elems, tuple):                          # перебирем кортежи
        for j in elems:
            summ = calculate(j, summ)

    return summ






summ = calculate(data_structure)
print("Сумма - ", summ)                                     
