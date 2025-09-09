nombres = ['SOFíA', 'DIEGO', 'MARICeLA', 'JUAN ramón', "teSt"]

nombres_propios = []

contador = 0

for nombre in nombres:

    # nombres_propios.append(nombre.title())
    
    # if contador < len(nombres)-1: 
        
    #     print(nombre.title(), end=', ')
    #     contador += 1

    # else:

    #     print(nombre.title())
    nombres_propios.append(nombre.title())


print(nombres_propios)

with open("prueba_1.txt", "w", encoding="utf-8") as f:

    f.write(", ".join(nombres_propios))

# print(nombres_propios)

# print(len(nombres)-1)