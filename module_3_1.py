calls = 0
def count_calls(): # функция счётчик
    global calls
    calls += 1     # при вызове добавляет 1 к счётчику

def string_info(string):             # функция с параметром строки, ниже создаём список
    lis_ = []                        
    lis_.append(len(string))         # добавляем в список длинну строки
    lis_.append((string.upper()))    # добавляем строку в верхнем регистре
    lis_.append((string.lower()))    # добавляем строку в нижнем регистре
    print(lis_)                      # печатаем список
    count_calls()                    # вызываем функцию счётчик

def is_contains(string, list_to_search):    # функция с параметром строки и списка
    ser = []                                
    for search in list_to_search:           
        ser.append(search.lower())          # с помощью цикла добавляем в ser[] принимаемый список, в нижнем регистре, чтоб исключить ошибки
    if string.lower() in ser:               # делаем проверку на наличие строки в списке
        print(True)                         
    else:
        print(False)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycle', 'cyclic'])
print(calls)
