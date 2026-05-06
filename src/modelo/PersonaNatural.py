from src.modelo.contribuyente import Contribuyente


class PersonaNatural(Contribuyente):


    def __init__(
        self,
        nombre: str,
        identificacion: str,
        ingresos_anuales: float,
        porcentaje_impuesto: float
    ) -> None:
        
        super().__init__(nombre, identificacion)
        self._ingresos_anuales = ingresos_anuales
        self._porcentaje_impuesto = porcentaje_impuesto

    def calcular_impuesto(self) -> float:
         
        return self._ingresos_anuales * self._porcentaje_impuesto

    def obtener_descripcion(self) -> str:
         
        return (
            f"Persona Natural | {super().obtener_descripcion()} | "
            f"Ingresos: {self._ingresos_anuales}"
        )


    def get_ingresos_anuales(self) -> float:
        return self._ingresos_anuales

    def get_porcentaje_impuesto(self) -> float:
        return self._porcentaje_impuesto