palabra_secreta = 'perro'
intentos = 6
lista_de_intentos = []
palabra = ''

while palabra != palabra_secreta:
    palabra = input('ingrese una palabra de 5 letras: ')
    intentos = intentos - 1
    if intentos == 0:
        print(f'haz perdido, la palabra secreta era, "{palabra_secreta}"')
        break
    lista_de_intentos.clear()

    if len(palabra) == 5:
        for i in range(len(palabra_secreta)):
                    if palabra.lower()[i] == palabra_secreta[i]:
                        lista_de_intentos.append('🟩' + ' ' + palabra[i])
                    elif palabra.lower()[i] in palabra_secreta:
                        lista_de_intentos.append('🟨' + ' ' + palabra[i])
                    else:
                        lista_de_intentos.append('⬜️' + ' ' + palabra[i])

    else:
        print('la palabra debe tener 5 letras, intente de nuevo')

    print(lista_de_intentos)

    if palabra.lower() != palabra_secreta:
        print(f'te quedan {intentos} intentos')
    if palabra.lower() == palabra_secreta:
        print(' ')
        print('Haz ganado!')