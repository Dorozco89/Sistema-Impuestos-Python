import unittest

from src.modelo.trabajador_independiente import TrabajadorIndependiente


class TestTrabajadorIndependiente(unittest.TestCase):

    def test_calcular_impuesto_trabajador_independiente(self):

        trabajador = TrabajadorIndependiente(
            "Carlos Ruiz",
            "456",
            40000,
            0.15
        )

        resultado = trabajador.calcular_impuesto()

        self.assertEqual(resultado, 6000.0)


if __name__ == "__main__":
    unittest.main()