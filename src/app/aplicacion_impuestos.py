from typing import List

from src.modelo.contribuyente import Contribuyente
from src.modelo.persona_natural import PersonaNatural
from src.modelo.empresa import Empresa
from src.modelo.trabajador_independiente import TrabajadorIndependiente
from src.servicio.gestor_archivos import GestorArchivos


class AplicacionImpuestos:
     

    def __init__(self) -> None:
        self._contribuyentes: List[Contribuyente] = []
        self._gestor_archivos = GestorArchivos()

    def inicializar_datos(self) -> None:
        
        self._contribuyentes.append(
            PersonaNatural("Juan Pérez", "123", 50000, 0.1)
        )

        self._contribuyentes.append(
            Empresa("TechCorp", "900123", 100000, 60000, 0.3)
        )

        self._contribuyentes.append(
            TrabajadorIndependiente("Carlos Ruiz", "456", 40000, 0.15)
        )

    def mostrar_impuestos(self) -> None:
         
        print("\n=== CÁLCULO DE IMPUESTOS ===")

        for contribuyente in self._contribuyentes:
            print(contribuyente.obtener_descripcion())
            print(f"Impuesto: {contribuyente.calcular_impuesto()}")
            print("--------------------------------------")

    def guardar_datos(self, ruta: str) -> None:
         
        try:
            self._gestor_archivos.guardar_objetos(ruta, self._contribuyentes)
            print("\nDatos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self, ruta: str) -> None:
        
        try:
            self._contribuyentes = self._gestor_archivos.leer_objetos(ruta)
            print("\nDatos cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar datos: {e}")

    def ejecutar(self) -> None:
        ruta = "data/contribuyentes.txt"

        # Inicializar datos
        self.inicializar_datos()

        # Mostrar datos originales
        print("=== DATOS ORIGINALES ===")
        self.mostrar_impuestos()

        # Guardar en archivo
        self.guardar_datos(ruta)

        # Cargar desde archivo
        self.cargar_datos(ruta)

        # Mostrar datos cargados
        print("\n=== DATOS RECUPERADOS ===")
        self.mostrar_impuestos()

if __name__ == "__main__":
    app = AplicacionImpuestos()
    app.ejecutar()