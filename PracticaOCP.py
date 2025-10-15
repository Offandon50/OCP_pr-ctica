# calculadora_final.py
from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a: float, b: float) -> float:
        pass

class Suma(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a + b


class Resta(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a - b


class Multiplicacion(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a * b

class Division(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b

class Calculadora:
    def _init_(self):
        self.operaciones = {
            "sumar": Suma(),
            "restar": Resta(),
            "multiplicar": Multiplicacion(),
            "dividir": Division(),
        }

    def ejecutar(self, operacion: str, a: float, b: float) -> float:
        if operacion not in self.operaciones:
            raise ValueError(f"Operación inválida: {operacion}")
        return self.operaciones[operacion].ejecutar(a, b)

    def añadir_operacion(self, nombre, operacion):
        # Nuevas operaciones
        self.operaciones[nombre] = operacion

class Potencia(Operacion):
    def ejecutar(self, a: float, b: float) -> float:
        return a ** b