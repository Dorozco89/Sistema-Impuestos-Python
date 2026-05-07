from typing import List

from src.modelo.contribuyente import Contribuyente
from src.modelo.persona_natural import PersonaNatural
from src.modelo.empresa import Empresa
from src.modelo.trabajador_independiente import TrabajadorIndependiente
from src.servicio.fabrica_contribuyentes import FabricaContribuyentes


class GestorArchivos:

    def guardar_objetos(self, ruta: str, contribuyentes: List[Contribuyente]) -> None:
        with open(ruta, "w", encoding="utf-8") as archivo:
            for contribuyente in contribuyentes:

                if isinstance(contribuyente, PersonaNatural):
                    linea = (
                        f"PERSONA;"
                        f"{contribuyente.get_nombre()};"
                        f"{contribuyente.get_identificacion()};"
                        f"{contribuyente.get_ingresos_anuales()};"
                        f"{contribuyente.get_porcentaje_impuesto()}"
                    )

                elif isinstance(contribuyente, Empresa):
                    linea = (
                        f"EMPRESA;"
                        f"{contribuyente.get_nombre()};"
                        f"{contribuyente.get_identificacion()};"
                        f"{contribuyente.get_ingresos()};"
                        f"{contribuyente.get_gastos()};"
                        f"{contribuyente.get_tasa_impuesto()}"
                    )

                elif isinstance(contribuyente, TrabajadorIndependiente):
                    linea = (
                        f"INDEPENDIENTE;"
                        f"{contribuyente.get_nombre()};"
                        f"{contribuyente.get_identificacion()};"
                        f"{contribuyente.get_ingresos()};"
                        f"{contribuyente.get_tarifa_impuesto()}"
                    )

                else:
                    continue

                archivo.write(linea + "\n")

    def leer_objetos(self, ruta: str) -> List[Contribuyente]:
        contribuyentes: List[Contribuyente] = []

        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if not datos or len(datos) < 2:
                    continue

                tipo = datos[0]
                valores = datos[1:]

                try:
                    contribuyente = FabricaContribuyentes.crear_contribuyente(tipo, valores)
                    contribuyentes.append(contribuyente)
                except ValueError as e:
                    print(f"Error al procesar línea: {linea.strip()} -> {e}")

        return contribuyentes