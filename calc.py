def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль!"


def main():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    op = input("Операция (+, -, *, /): ")

    if op == '+':
        print(add(a, b))
    elif op == '-':
        print(subtract(a, b))
    elif op == '*':
        print(multiply(a, b))
    elif op == '/':
        print(divide(a, b))
    else:
        print("Неизвестная операция")


if __name__ == "__main__":
    main()

