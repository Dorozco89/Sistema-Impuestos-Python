from abc import ABC, abstractmethod


class CalculadoraImpuesto(ABC):
     
    @abstractmethod
    def calcular_impuesto(self) -> float:
         
        pass