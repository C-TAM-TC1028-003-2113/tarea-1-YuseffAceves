def main():
    # escribe tu código abajo de esta línea
    nuevo = int(input("Dame la cantidad de juegos nuevos: "))
    usado = int(input("Dame la cantidad de juegos usados: "))
    total = (nuevo * 1000) + (usado * 350)
    print("total:", total)


if __name__ == '__main__':
    main()
