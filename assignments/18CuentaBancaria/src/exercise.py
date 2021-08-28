def main():
    # escribe tu código abajo de esta línea
    mes = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el numero de cheques: "))
    saldo = mes + ingresos - ((egresos) + (cheques * 13))
    total = saldo * 0.925

    print("saldo final de la cuenta:", total)



if __name__ == '__main__':
    main()
