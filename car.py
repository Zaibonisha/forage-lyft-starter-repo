from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def getService(self):
        pass

class CapuletEngine(Engine):
    def getService(self):
        return "CapuletEngine service criteria"

class WilloughbyEngine(Engine):
    def getService(self):
        return "WilloughbyEngine service criteria"

class SternmanEngine(Engine):
    def getService(self):
        return "SternmanEngine service criteria"

class Battery(ABC):
    @abstractmethod
    def getService(self):
        pass

class SpindlerBattery(Battery):
    def getService(self):
        return "SpindlerBattery service criteria"

class NubbinBattery(Battery):
    def getService(self):
        return "NubbinBattery service criteria"

class Car(ABC):
    def __init__(self, model, engine, battery, last_service_date):
        self.model = model
        self.engine = engine
        self.battery = battery
        self.last_service_date = last_service_date

    def needs_service(self):
        return Service.checkService(self)

class Service:
    @staticmethod
    def checkService(car):
        if isinstance(car.engine, Engine) and isinstance(car.battery, Battery):
            engine_service_criteria = car.engine.getService()
            battery_service_criteria = car.battery.getService()
            return f"Car {car.model} needs service according to {engine_service_criteria} and {battery_service_criteria}"
        else:
            raise ValueError("Invalid car object passed to checkService")
