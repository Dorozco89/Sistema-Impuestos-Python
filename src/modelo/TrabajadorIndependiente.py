from src.modelo.contribuyente import Contribuyente


class TrabajadorIndependiente(Contribuyente):
     

    def __init__(
        self,
        nombre: str,
        identificacion: str,
        ingresos: float,
        tarifa_impuesto: float
    ) -> None:
         
        super().__init__(nombre, identificacion)
        self._ingresos = ingresos
        self._tarifa_impuesto = tarifa_impuesto

    def calcular_impuesto(self) -> float:
         
        if self._ingresos <= 0:
            return 0.0

        return self._ingresos * self._tarifa_impuesto

    def obtener_descripcion(self) -> str:
         
        return (
            f"Trabajador Independiente | {super().obtener_descripcion()} | "
            f"Ingresos: {self._ingresos}"
        )


    def get_ingresos(self) -> float:
        return self._ingresos

    def get_tarifa_impuesto(self) -> float:
        return self._tarifa_impuesto