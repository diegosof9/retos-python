# test
resultado = 0

while resultado == 0:

    num1, num2, suma = '', '', 0
    
    while num1 in ('0','') or num2 in ('0','') or not num1.isdigit() or not num2.isdigit():
    
        num1 = input("\nIngresa el número dividendo: ")
        num2 = input("Ingresa el número divisor: ")

        if num1 in ('0','') or num2 in ('0','') or not num1.isdigit() or not num2.isdigit():
            print("\n<<<<<<<<Ingresaste un cero (0), algún carácter no permitido o no ingresaste alguno de los datos solicitados.\
            \nPor favor verifica tus respuestas y vuelve a intentarlo.>>>>>>>>")
             
    num1 = int(num1)
    num2 = int(num2)

    """ Código que realiza el proceso de calcular el resultado de la división de dos números, 
    sin utilizar los símbolos de división(/) o de multiplicación(*). """
    while suma < num1:
        suma += num2
        if suma <= num1:
            resultado += 1
        # print(test)
    
    if resultado == 0:
        print("El resultado es cero (0), ingresa otros dos números.")

print()
print(resultado)
print(num1//num2)