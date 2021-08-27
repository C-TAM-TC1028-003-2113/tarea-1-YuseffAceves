def main():
    # escribe tu código abajo de esta línea
    mensajes = int(input("Dame el numero de mensajes: "))
    megas = float(input("Dame el numero de megas: "))
    minutos = int(input("Dame el numero de minutos: "))
    total = (mensajes * 0.80) + (megas * 0.80) + (minutos * 0.80)
    print("total:", total)


if __name__ == '__main__':
    main()
