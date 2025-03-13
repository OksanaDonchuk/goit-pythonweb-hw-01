from abc import ABC, abstractmethod
import logging
from typing import Type

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    """
    Абстрактний базовий клас для транспортних засобів.
    """

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """Абстрактний метод запуску двигуна."""
        pass


class Car(Vehicle):
    """
    Клас автомобіля, що успадковує Vehicle.
    """

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    """
    Клас мотоцикла, що успадковує Vehicle.
    """

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    """
    Абстрактна фабрика для створення транспортних засобів.
    """

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    """
    Фабрика для створення транспортних засобів зі специфікацією для США (US Spec).
    """

    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    """
    Фабрика для створення транспортних засобів зі специфікацією для ЄС (EU Spec).
    """

    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


if __name__ == "__main__":
    # Створення фабрики для США
    us_factory: Type[VehicleFactory] = USVehicleFactory()
    us_car: Car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle: Motorcycle = us_factory.create_motorcycle(
        "Harley-Davidson", "Sportster"
    )

    # Запуск двигунів
    us_car.start_engine()
    us_motorcycle.start_engine()

    # Створення фабрики для ЄС
    eu_factory: Type[VehicleFactory] = EUVehicleFactory()
    eu_car: Car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("BMW", "R1250")

    # Запуск двигунів
    eu_car.start_engine()
    eu_motorcycle.start_engine()
