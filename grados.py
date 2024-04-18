temperatura = float(input("Ingrese temperatura a convertir: "))
eslcala = input ("Es Fahrenheit(F) o Celsius(C)?: ").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)
else:
    print("Escala incorrecta")
