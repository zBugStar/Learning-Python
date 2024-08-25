# Main.py
import LibroClass
import BibliotecaClass

biblioteca = BibliotecaClass.Biblioteca()
programaOn = True

while programaOn:

    print("Bienvenido a la Biblioteca Digital")
    print("¿Que desea hacer?")
    print("1. Agregar Libro")
    print("2. Consultar Libros")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Salir")

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:

        titulo = input("Digite el titulo del libro: ")
        autor = input("Digite el autor del libro: ")
        libro = LibroClass.Libro(titulo, autor, True)
        biblioteca.agregarLibro(libro)
        print("Libro agregado exitosamente")
        print("\n")

    elif opcion == 2:

        nombreLibro = input("Digite el nombre del libro que desea consultar: ")
        nombreAutor = input("Digite el autor del libro: ")
        print("Libros disponibles:")
        biblioteca.consultarLibro(nombreLibro, nombreAutor)
        print("\n")

    elif opcion == 3:

        titulo = input("Digite el titulo del libro que desea prestar: ")
        libro = LibroClass.Libro(titulo, "", True)
        biblioteca.prestarLibro(libro)
        print("\n")

    elif opcion == 4:

        titulo = input("Digite el titulo del libro que desea devolver: ")
        libro = LibroClass.Libro(titulo, "", True)
        biblioteca.devolverLibro(libro)
        print("\n")

    elif opcion == 5:

        programaOn = False
        print("Gracias por usar la Biblioteca Digital")

    else:
        print("Opcion invalida")
        print("\n")
