def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el numero de palabras: "))
    pagina = palabras // 475
    total = pagina + 1
    costo = (total) * (60 * .9)
    print("El costo de la publicacion es:", costo)


if __name__ == '__main__':
    main()
