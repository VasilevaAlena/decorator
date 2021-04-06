import datetime


def decorator_logger(old_function):
    def writing_file(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('decoratorlogger.txt', 'w', encoding='utf-8') as file:
            file.write(
                f'Дата и время вызова функции: {datetime.datetime.now()}\n'
                f'Имя функции: {old_function.__name__}\n'
                f'Аргументы: {args, kwargs}\n'
                f'Результат: {result}\n'
            )
        return result
    return writing_file


@decorator_logger
def multiplication_function(a, b):
    return a * b


if __name__ == '__main__':
    multiplication_function(2, b=5)