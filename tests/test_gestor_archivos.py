import os
import unittest

from src.modelo.persona_natural import PersonaNatural
from src.modelo.empresa import Empresa
from src.modelo.trabajador_independiente import TrabajadorIndependiente
from src.servicio.gestor_archivos import GestorArchivos


class TestGestorArchivos(unittest.TestCase):

    def test_guardar_y_leer_objetos(self):

        ruta = "data/test_contribuyentes.txt"

        contribuyentes = [
            PersonaNatural("Juan Pérez", "123", 50000, 0.10),
            Empresa("TechCorp", "900123", 100000, 60000, 0.30),
            TrabajadorIndependiente("Carlos Ruiz", "456", 40000, 0.15)
        ]

        gestor = GestorArchivos()

        gestor.guardar_objetos(ruta, contribuyentes)

        objetos_leidos = gestor.leer_objetos(ruta)

        self.assertEqual(len(objetos_leidos), 3)

        self.assertEqual(
            objetos_leidos[0].calcular_impuesto(),
            5000.0
        )

        self.assertEqual(
            objetos_leidos[1].calcular_impuesto(),
            12000.0
        )

        self.assertEqual(
            objetos_leidos[2].calcular_impuesto(),
            6000.0
        )

        if os.path.exists(ruta):
            os.remove(ruta)


if __name__ == "__main__":
    unittest.main()