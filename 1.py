A = int(input("Введите число: "))
B = int(input("Введите степень: "))

def power (A, B) :
    if (B == 1) or (A == 1):
        return A
    if (B != 1):
        return (A * power(A, B-1))

print("А в степени В равно: ", power(A, B))

