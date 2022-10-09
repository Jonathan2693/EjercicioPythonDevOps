print('Cajero Automático')
print('*******************************')

salir = True
saldo = int(1000)
historico = ""
contrasenia = '1235'
intentos = 3

while(intentos>0):
    try:
        pinEntrada = input('Ingrese Pin para utilizar el cajero automático : ')
        if pinEntrada!=contrasenia:
            print('El pin ingresado no es correcto')
            intentos -= 1
        else:
            print('\nBienvenido Jonathan Quino\n')
            intentos = 0
            salir = False
    except ValueError:
        print('El pin ingresado no es valido')
        intentos -= 1
        salir = True


while(salir==False):
    print('1. Consultar saldo')
    print('2. Retirar efectivo')
    print('3. Histórico de movimientos')
    print('4. Salir\n')
    try:
        opcion = int(input('Teclea el número de la operacion que deseas: '))
    except ValueError:
        print('La opcion ingresada no es valida')
        continue
    if opcion==1:
        print(f"El saldo actual es {saldo}")
        historico += 'Ha consultado su saldo (opción 1)\n'
    elif opcion==2:
        if saldo!=0:
            try:
                saldoRetirar = int(input('Ingresa la cantidad a retirar: '))
                if (saldo - saldoRetirar)<0:
                    print('El saldo es insuficiente para retirarlo')
                else:
                    saldo = saldo - saldoRetirar
                    print(f"Se ha retirado {saldoRetirar} mxn de la cuenta")
                historico += 'Ha elegido retirar de su cuenta (opción 2)\n'
            except ValueError:
                print('La cantidad ingresada no es valida')
                continue
        else:
            print('El saldo es 0, ya no puede retirarse dinero')
    elif opcion==3:
        print('Este es el histórico de movimientos :')
        print(f"{historico}")
    elif opcion==4:
        print('Saliendo de la aplicación...')
        salir = True
    


