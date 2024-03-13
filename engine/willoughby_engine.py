from abc import ABC, abstractmethod
from car import Car

class WilloughbyEngine(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def engine_should_be_serviced(self):
        pass

    def needs_service(self):
        return self.engine_should_be_serviced()

class ConcreteWilloughbyEngine(WilloughbyEngine, Car):
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
