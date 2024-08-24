# BibliotecaClass.py
import LibroClass


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def prestarLibro(self, libro):
        for libroEnBiblioteca in self.libros:
            if libroEnBiblioteca.titulo == libro.titulo:
                if libroEnBiblioteca.disponible:
                    libroEnBiblioteca.disponible = False
                    print("Libro prestado")
                else:
                    print("El libro no esta disponible")
                return

    def devolverLibro(self, libro):
        for libroEnBiblioteca in self.libros:
            if libroEnBiblioteca.titulo == libro.titulo:
                libroEnBiblioteca.disponible = True
                print("El libro ya esta en la biblioteca")
                return

    def consultarLibro(self, nombreLibro, nombreAutor):
        for libro in self.libros:
            if libro.titulo in nombreLibro or libro.autor in nombreAutor:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Disponible: {libro.disponible}")
