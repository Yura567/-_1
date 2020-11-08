a = float(input("Введіть перше число >>"))
b = float(input("Введіть друге число >>"))
operation = input("Введіть арифметичний знак")

resultat = None
if operation == "+":
    resultat = a + b
elif operation == "-":
    resultat = a - b
elif operation == "*":
    resultat = a * b
elif operation == "/":
    resultat = a / b
else:
    print("Не зрозумілий знак. Операцію виконати неможливо")
if resultat is not None:
    print(resultat)