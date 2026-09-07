print("Виберіть")


print("1 - Додавання, 2 - Віднімання, 3 - множення")

Vibir = input("Введіть номер: ")


num1 = input("Введіть перше число: ")

num2 = input("Введіть друге число: ")



if Vibir == "1":
    print("Результат: ", float(num1) + float(num2))

elif Vibir == "2":
    print("Результат: ", float(num1) - float(num2))

elif Vibir == "3":
    print("Результат: ", float(num1) * float(num2))

else:
    print("Невірний вибір")
    print("Спробуйте ще раз")
