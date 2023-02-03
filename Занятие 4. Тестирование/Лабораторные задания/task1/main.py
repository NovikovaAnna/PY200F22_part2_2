from typing import Union


class AudiCar:
    """ Базовый класс автомобили. """
    counter = 0
    def __init__(self,brand: str, color:str, model: str, age: Union[int, float],):
        self._brand = brand
        self.is_valid_brand(self.brand)
        self._color = color
        self.model = model
        self.age = age
        self.count()

    #@staticmethod
    #def count():
        #AudiCar.counter += 1

    @classmethod
    def count(cls):
        cls.counter += 1

    @property
    def brand(self) -> str:
        return self._brand

    @classmethod
    def is_valid_brand(cls, brand:str):
        if not isinstance(brand,str):
            raise TypeError("Марка автомобиля может быть только типа str")
        cls._brand = brand
        return "Марка автомобиля валидна"

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self,value):
        if not isinstance(value,str):
            raise TypeError("Цвет автомобиля может быть только типа str")
        self._color = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self,value):
        if not isinstance(value,str):
            raise TypeError("Модель автомобиля может быть только типа str")
        self._model = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError("Возраст может быть только положительным числом")
        if value <= 0:
            raise ValueError("Возраст может быть только положительным числом")
        self._age = float(value)

    def __str__(self) -> str:
        return f"Автомобиль {self.brand}. Цвет {self.color}, Модель {self.model}, Возраст {self.age}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.brand!r}, color={self.color!r}, model={self.model!r}, age={self.age!r})"


class InternalCombustionEngineAudiCar(AudiCar):

    def __init__(self, brand: str, color: str, model: str, age: Union[int, float], consumption: float):
        super().__init__(brand, color, model, age)
        self.consumption = consumption

    def __str__(self) -> str:
        return f"{super().__str__()}, Расход топлива: {self.consumption}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, color={self.color!r}, model={self.model!r}, age={self.age!r}, consumption={self.consumption!r})"

    @property
    def consumption(self) -> float:
        return self._consumption

    @consumption.setter
    def consumption(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError("Расход топлива может быть только положительным числом")
        if value <= 0:
            raise ValueError("Расход топлива может быть только положительным числом")
        self._consumption = float(value)


class ElectricAudiCar(AudiCar):
    def __init__(self, brand: str, color: str, model: str, age: Union[int, float],  charging: float):
        super().__init__(brand, color, model, age)
        self.charging = charging

    def __str__(self) -> str:
        return f"{super().__str__()}, Время зарядки: {self.charging}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, color={self.color!r}, model={self.model!r}, age={self.age!r}, charging={self.charging!r})"

    @property
    def charging(self) -> float:
        return self._charging

    @charging.setter
    def charging(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность зарядки автомобиля может быть только положительным числом")
        if value <= 0:
            raise ValueError("Продолжительность зарядки автомобиля может быть только положительным числом")
        self._charging = float(value)


if __name__ == "__main__":
    a = InternalCombustionEngineAudiCar("Audi", "Красный",'Q3',2, 220)
    b = ElectricAudiCar('Audi', 'Красный','Q3', 0.7, 30)
    print(a)
    print(b)
    print(a.__repr__())
    print(a.__str__())
    print(a)
    print(b)
    car1 = AudiCar("Audi", "Серый", "Q3", 11)
    print(car1)










