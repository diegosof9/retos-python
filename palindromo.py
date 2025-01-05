ingresar_palabra = True

while ingresar_palabra:

    si_no_ingresar_palabra = ""
    palabra= "" 

    while palabra == "":
        palabra = input("Ingresa una palabra: ")
        if palabra == "":
            print(f"\nDebes ingresar una palabra, inténtalo de nuevo.\n")

    print(palabra)

    # reversa = palabra[::-1]
    palabra_reversa = ""

    for letra in palabra:
        palabra_reversa = letra + palabra_reversa

    if palabra_reversa == palabra:
        print(f"La palabra {palabra}, es palíndromo.")

    else:
        print(f"La palabra {palabra}, no es palíndromo.")


    while si_no_ingresar_palabra == "" or si_no_ingresar_palabra not in('Y','N'):

        si_no_ingresar_palabra = input(f"\n¿Deseas ingresar otra palabra?: Y(yes)-N(no): ").upper()

        if si_no_ingresar_palabra  == "":
            print(f"Debes elegir una opción, inténtalo de nuevo.")
        
        elif si_no_ingresar_palabra not in('Y','N'):
            print(f"No hay opciones para la letra elegida, inténtelo de nuevo.")

    print()

    if si_no_ingresar_palabra == 'N':
        ingresar_palabra = False
        print("Adiós, vuelve pronto!!!")

# print(palabra_reversa)
# print(reversa)    