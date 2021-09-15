def equivalente(num1, num2, num3):
    if (num1 + num2 == num3) or (num1 + num3 == num2) or (num3 + num2 == num1):
        print("Soma de dois e o terceiro valor")
    else:
        print("Soma de dois NÃO é o terceiro valor")

equivalente(3,1,2)

