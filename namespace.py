
def test_function():

    def  inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
# inner_function() - При вызове inner_function, программа ругается, что не видит функцию вне функции test_function.
# функция inner_function() - логальная функция, она не является глобальной функцией