import unittest

from src.modelo.persona_natural import PersonaNatural


class TestPersonaNatural(unittest.TestCase):

    def test_calcular_impuesto_persona_natural(self):
        persona = PersonaNatural(
            "Juan Pérez",
            "123",
            50000,
            0.10
        )

        resultado = persona.calcular_impuesto()

        self.assertEqual(resultado, 5000.0)


if __name__ == "__main__":
    unittest.main()