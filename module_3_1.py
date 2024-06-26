calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    lis_ = []
    lis_.append(len(string))
    lis_.append((string.upper()))
    lis_.append((string.lower()))
    print(lis_)
    count_calls()

def is_contains(string, list_to_search):
    ser = []
    for search in list_to_search:
        ser.append(search.lower())
    if string.lower() in ser:
        print(True)
    else:
        print(False)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycle', 'cyclic'])
print(calls)
