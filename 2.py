a = int(input("Введите певрое число: "))
b = int(input("Введите второе число: "))

def Summary(a, b):
    if (b==0):
        return a
    return Summary(a+1, b-1)

print("Сумма чисел равна: ", Summary(a, b))
