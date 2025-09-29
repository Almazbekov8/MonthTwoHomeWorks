from datetime import datetime as dt

func_time = dt.now()

def printer_time(func):
    def wrapper(*args, **kwargs):
        print(f"Время вызова функции {func_time.strftime('%H:%M:%S')}, {func.strftime("%d/%m/%Y")}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@printer_time
def print_hello_world():
    print("Hello World!")