from datetime import datetime

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
        historico += f"{datetime.now()} - Accion : Ha consultado su saldo - Saldo Actual = {saldo}mxn\n"
        print(' 1. Regresar al menú principal')
        print(' 2. Salir')
        try:
            opcion = int(input('Eliga una opcion para continuar: '))
            if opcion==1:
                continue
            elif opcion==2:
                salir = True
                print('Saliendo de la aplicacion')
        except ValueError:
            print('La opcion ingresada no es válida')
            continue
    elif opcion==2:
        if saldo!=0:
            try:
                print(' 1. Regresar al menú principal')
                print(' 2. Salir')
                saldoRetirar = int(input('ó Ingresa la cantidad a retirar: '))
                if saldoRetirar==1:
                    continue
                elif saldoRetirar==2:
                    salir = True
                elif (saldoRetirar!=1) & (saldoRetirar!=2) & ((saldo - saldoRetirar)<0):
                    print('El saldo es insuficiente para retirarlo')
                else:
                    saldo = saldo - saldoRetirar
                    if saldo==0:
                        print('El saldo actual ya es 0, no podra retirar nuevamente')
                    print(f"Se ha retirado {saldoRetirar} mxn de la cuenta")
                historico += f"{datetime.now()} - Accion : Ha retirado dinero - Saldo Actual= {saldo}mxn\n"
            except ValueError:
                print('La valor ingresado no es valido')
                continue
        else:
            print('El saldo es 0, ya no puede retirarse dinero')
    elif opcion==3:
        print('Este es el histórico de movimientos :')
        print(f"{historico}")
        try:
            print(' 1. Regresar al menú principal')
            print(' 2. Salir')
            opcion = int(input('Ingrese la opción deseada: '))
            if opcion==2:
                salir = False
            else:
                continue
        except ValueError:
                print('La valor ingresado no es valido')
                continue
    elif opcion==4:
        print('Saliendo de la aplicación...')
        salir = True
    


