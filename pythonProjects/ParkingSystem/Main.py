import tkinter as tk
from tkinter import messagebox


class NodoEstacionamiento:
    def __init__(self, lugar, placa=None):
        self.lugar = lugar
        self.placa = placa
        self.izquierda = None
        self.derecha = None


class ArbolEstacionamiento:
    def __init__(self):
        self.raiz = None

    def agregar(self, lugar, placa):
        if self.raiz is None:
            self.raiz = NodoEstacionamiento(lugar, placa)
        else:
            self._agregar_recursivo(self.raiz, lugar, placa)

    def _agregar_recursivo(self, nodo, lugar, placa):
        if lugar < nodo.lugar:
            if nodo.izquierda is None:
                nodo.izquierda = NodoEstacionamiento(lugar, placa)
            else:
                self._agregar_recursivo(nodo.izquierda, lugar, placa)
        elif lugar > nodo.lugar:
            if nodo.derecha is None:
                nodo.derecha = NodoEstacionamiento(lugar, placa)
            else:
                self._agregar_recursivo(nodo.derecha, lugar, placa)
        else:
            nodo.placa = placa  # Actualizar si el lugar ya existe

    def buscar_por_placa(self, placa):
        return self._buscar_por_placa_recursivo(self.raiz, placa)

    def _buscar_por_placa_recursivo(self, nodo, placa):
        if nodo is None:
            return None
        if nodo.placa == placa:
            return nodo.lugar
        izquierda = self._buscar_por_placa_recursivo(nodo.izquierda, placa)
        if izquierda is not None:
            return izquierda
        return self._buscar_por_placa_recursivo(nodo.derecha, placa)

    def buscar_por_lugar(self, lugar):
        return self._buscar_por_lugar_recursivo(self.raiz, lugar)

    def _buscar_por_lugar_recursivo(self, nodo, lugar):
        if nodo is None:
            return None
        if nodo.lugar == lugar:
            return nodo.placa
        elif lugar < nodo.lugar:
            return self._buscar_por_lugar_recursivo(nodo.izquierda, lugar)
        else:
            return self._buscar_por_lugar_recursivo(nodo.derecha, lugar)


# Interfaz gráfica
class EstacionamientoGUI:
    def __init__(self, root, arbol):
        self.arbol = arbol
        self.root = root
        self.root.title("Sistema de Estacionamiento Inteligente")

        # Widgets de ingreso de placa
        tk.Label(root, text="Placa del Vehículo:").grid(row=0, column=0)
        self.placa_entry = tk.Entry(root)
        self.placa_entry.grid(row=0, column=1)

        # Widgets de lugar de estacionamiento
        tk.Label(root, text="Lugar de Estacionamiento:").grid(row=1, column=0)
        self.lugar_entry = tk.Entry(root)
        self.lugar_entry.grid(row=1, column=1)

        # Botones para acciones
        tk.Button(root, text="Aparcar", command=self.aparcar).grid(row=2, column=0)
        tk.Button(root, text="Buscar", command=self.buscar_vehiculo).grid(row=2, column=1)
        tk.Button(root, text="Verificar Lugar", command=self.verificar_lugar).grid(row=3, column=0)

        # Canvas para dibujar el árbol
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Actualizar Vista", command=self.actualizar_vista).grid(row=5, column=0, columnspan=2)

    def aparcar(self):
        placa = self.placa_entry.get().strip()
        lugar = int(self.lugar_entry.get().strip())

        if self.arbol.buscar_por_lugar(lugar):
            messagebox.showerror("Error", f"El lugar {lugar} ya está ocupado.")
        else:
            self.arbol.agregar(lugar, placa)
            messagebox.showinfo("Éxito", f"Vehículo con placa {placa} aparcado en el lugar {lugar}.")

    def buscar_vehiculo(self):
        placa = self.placa_entry.get().strip()
        lugar = self.arbol.buscar_por_placa(placa)

        if lugar is not None:
            messagebox.showinfo("Resultado de Búsqueda", f"Vehículo con placa {placa} está en el lugar {lugar}.")
        else:
            messagebox.showerror("Error", "Vehículo no encontrado.")

    def verificar_lugar(self):
        lugar = int(self.lugar_entry.get().strip())
        placa = self.arbol.buscar_por_lugar(lugar)

        if placa is not None:
            messagebox.showinfo("Lugar Ocupado", f"El lugar {lugar} está ocupado por el vehículo con placa {placa}.")
        else:
            messagebox.showinfo("Lugar Disponible", f"El lugar {lugar} está disponible.")

    def actualizar_vista(self):
        self.canvas.delete("all")
        if self.arbol.raiz:
            self._dibujar_nodo(self.arbol.raiz, 400, 20, 200)

    def _dibujar_nodo(self, nodo, x, y, offset):
        if nodo is not None:
            # Dibujar el nodo como un círculo
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            text = f"{nodo.lugar}\n{nodo.placa if nodo.placa else 'Libre'}"
            self.canvas.create_text(x, y, text=text)

            # Líneas y nodos hijos
            if nodo.izquierda:
                self.canvas.create_line(x, y, x - offset, y + 60)
                self._dibujar_nodo(nodo.izquierda, x - offset, y + 60, offset // 2)
            if nodo.derecha:
                self.canvas.create_line(x, y, x + offset, y + 60)
                self._dibujar_nodo(nodo.derecha, x + offset, y + 60, offset // 2)


# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    arbol = ArbolEstacionamiento()
    app = EstacionamientoGUI(root, arbol)
    root.mainloop()
