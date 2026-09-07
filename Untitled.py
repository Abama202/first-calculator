print("Виберіть")
print("1 - Додавання, 2-Віднімання, 3 - множення")

Vibir = input("Введіть номер: ")

N1 = input("Введіть перше число: ")
N2 = input("Введіть друге число: ")

if Vibir == "1":
    print("Результат: ", int(N1) + int(N2))
elif Vibir == "2":
    print("Результат: ", int(N1) - int(N2))
elif Vibir == "3":
    print("Результат: ", int(N1) * int(N2))
else:
    print("Невірний вибір")
