from src.modelo.contribuyente import Contribuyente


class Empresa(Contribuyente):
    

    def __init__(
        self,
        nombre: str,
        identificacion: str,
        ingresos: float,
        gastos: float,
        tasa_impuesto: float
    ) -> None:
        
        super().__init__(nombre, identificacion)
        self._ingresos = ingresos
        self._gastos = gastos
        self._tasa_impuesto = tasa_impuesto

    def calcular_impuesto(self) -> float:
         
        utilidad = self._ingresos - self._gastos

        if utilidad <= 0:
            return 0.0

        return utilidad * self._tasa_impuesto

    def obtener_descripcion(self) -> str:
        
        return (
            f"Empresa | {super().obtener_descripcion()} | "
            f"Ingresos: {self._ingresos} | Gastos: {self._gastos}"
        )


    def get_ingresos(self) -> float:
        return self._ingresos

    def get_gastos(self) -> float:
        return self._gastos

    def get_tasa_impuesto(self) -> float:
        return self._tasa_impuesto