from abc import ABC, abstractmethod


class Contribuyente(ABC):
     
    def __init__(self, nombre: str, identificacion: str) -> None:
         
        self._nombre = nombre
        self._identificacion = identificacion

    def obtener_descripcion(self) -> str:
         
        return f"Nombre: {self._nombre} | ID: {self._identificacion}"

    @abstractmethod
    def calcular_impuesto(self) -> float:
        
        pass


    def get_nombre(self) -> str:
        return self._nombre

    def get_identificacion(self) -> str:
        return self._identificacion


    def __str__(self) -> str:
        return self.obtener_descripcion()