from typing import List

from src.modelo.persona_natural import PersonaNatural
from src.modelo.empresa import Empresa
from src.modelo.trabajador_independiente import TrabajadorIndependiente
from src.modelo.contribuyente import Contribuyente


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

                tipo = datos[0]

                if tipo == "PERSONA":
                    contribuyentes.append(
                        PersonaNatural(
                            datos[1],
                            datos[2],
                            float(datos[3]),
                            float(datos[4])
                        )
                    )

                elif tipo == "EMPRESA":
                    contribuyentes.append(
                        Empresa(
                            datos[1],
                            datos[2],
                            float(datos[3]),
                            float(datos[4]),
                            float(datos[5])
                        )
                    )

                elif tipo == "INDEPENDIENTE":
                    contribuyentes.append(
                        TrabajadorIndependiente(
                            datos[1],
                            datos[2],
                            float(datos[3]),
                            float(datos[4])
                        )
                    )

        return contribuyentes