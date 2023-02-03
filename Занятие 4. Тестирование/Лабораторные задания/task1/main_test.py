import unittest
from main import AudiCar, InternalCombustionEngineAudiCar
# импортируем то, что будем тестировать

class TestAudiCar(unittest.TestCase):
    def test_init(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(car.brand, "Audi")
        self.assertEqual(car.color, "red")
        self.assertEqual(car.model, "A3")
        self.assertEqual(car.age, 5)

    def test_is_valid_brand(self):
        self.assertRaises(TypeError, AudiCar.is_valid_brand, 123)
        self.assertEqual(AudiCar.is_valid_brand("Audi"), "Марка автомобиля валидна")

    def test_brand(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(car.brand, "Audi")
        self.assertRaises(AttributeError, setattr, car, 'brand', 123)

    def test_color(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(car.color, "red")
        car.color = "blue"
        self.assertEqual(car.color, "blue")
        self.assertRaises(TypeError, setattr, car, 'color', 123)

    def test_model(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(car.model, "A3")
        car.model = "A4"
        self.assertEqual(car.model, "A4")
        self.assertRaises(TypeError, setattr, car, 'model', 123)

    def test_age(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(car.age, 5.0)
        car.age = 5.5
        self.assertEqual(car.age, 5.5)
        self.assertRaises(TypeError, setattr, car, 'age', "five")
        self.assertRaises(ValueError, setattr, car, 'age', -5)

    def test_str(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(str(car), "Автомобиль Audi. Цвет red, Модель A3, Возраст 5")

    def test_repr(self):
        car = AudiCar("Audi", "red", "A3", 5.0)
        self.assertEqual(repr(car), "AudiCar(name='Audi', color='red', model='A3', age=5)")

if __name__ == '__main__':
    unittest.main()
