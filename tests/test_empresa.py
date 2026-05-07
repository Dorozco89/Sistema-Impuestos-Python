import unittest

from src.modelo.empresa import Empresa


class TestEmpresa(unittest.TestCase):

    def test_calcular_impuesto_empresa(self):

        empresa = Empresa(
            "TechCorp",
            "900123",
            100000,
            60000,
            0.30
        )

        resultado = empresa.calcular_impuesto()

        self.assertEqual(resultado, 12000.0)


if __name__ == "__main__":
    unittest.main()