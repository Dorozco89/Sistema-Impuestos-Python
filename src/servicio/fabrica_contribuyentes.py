from typing import List

from src.modelo.contribuyente import Contribuyente
from src.modelo.persona_natural import PersonaNatural
from src.modelo.empresa import Empresa
from src.modelo.trabajador_independiente import TrabajadorIndependiente


class FabricaContribuyentes:

    @staticmethod
    def crear_contribuyente(tipo: str, datos: List[str]) -> Contribuyente:

        if tipo == "PERSONA":
            return PersonaNatural(
                datos[0],
                datos[1],
                float(datos[2]),
                float(datos[3])
            )

        elif tipo == "EMPRESA":
            return Empresa(
                datos[0],
                datos[1],
                float(datos[2]),
                float(datos[3]),
                float(datos[4])
            )

        elif tipo == "INDEPENDIENTE":
            return TrabajadorIndependiente(
                datos[0],
                datos[1],
                float(datos[2]),
                float(datos[3])
            )

        else:
            raise ValueError(f"Tipo de contribuyente desconocido: {tipo}")