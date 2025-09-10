from typing import Any


class Appliance:
    """
    Базовый класс для бытовой техники.
    """

    def __init__(self, brand: str, power: int) -> None:
        """
        Инициализация прибора.
        :param brand: Бренд прибора.
        :param power: Мощность прибора в ваттах.
        """
        self.brand = brand
        self._power = power  # Инкапсуляция: мощность не изменяется пользователем напрямую

    def __str__(self) -> str:
        return f"Бытовая техника {self.brand}, мощность {self._power} Вт"

    def __repr__(self) -> str:
        return f"Appliance(brand={self.brand!r}, power={self._power!r})"

    def turn_on(self) -> str:
        """
        Включение прибора.

        >>> appliance = Appliance("Generic", 1000)
        >>> appliance.turn_on()
        'Generic включен.'
        """
        return f"{self.brand} включен."


class WashingMachine(Appliance):
    """
    Дочерний класс для стиральных машин.
    """

    def __init__(self, brand: str, power: int, load_capacity: int) -> None:
        """
        Инициализация стиральной машины.
        :param brand: Бренд.
        :param power: Мощность в ваттах.
        :param load_capacity: Вместимость загрузки в килограммах.
        """
        super().__init__(brand, power)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        return f"Стиральная машина {self.brand}, мощность {self._power} Вт, загрузка {self.load_capacity} кг"

    def start_wash(self) -> str:
        """
        Запуск стирки.

        >>> wm = WashingMachine("Samsung", 2000, 7)
        >>> wm.start_wash()
        'Samsung: Стирка началась.'
        """
        return f"{self.brand}: Стирка началась."

    def turn_on(self) -> str:
        """
        Перегруженный метод включения.
        Причина: Стиральные машины требуют подготовки перед включением.

        >>> wm = WashingMachine("Samsung", 2000, 7)
        >>> wm.turn_on()
        'Samsung: Проверка загрузки... Готов к стирке!'
        """
        return f"{self.brand}: Проверка загрузки... Готов к стирке!"


class Refrigerator(Appliance):
    """
    Дочерний класс для холодильников.
    """

    def __init__(self, brand: str, power: int, volume: int) -> None:
        """
        Инициализация холодильника.
        :param brand: Бренд.
        :param power: Мощность в ваттах.
        :param volume: Объем холодильника в литрах.
        """
        super().__init__(brand, power)
        self.volume = volume

    def __str__(self) -> str:
        return f"Холодильник {self.brand}, мощность {self._power} Вт, объем {self.volume} л"

    def cool_down(self) -> str:
        """
        Запуск охлаждения.

        >>> fridge = Refrigerator("LG", 150, 300)
        >>> fridge.cool_down()
        'LG: Охлаждение запущено.'
        """
        return f"{self.brand}: Охлаждение запущено."


# Пример использования
wm = WashingMachine("Samsung", 2000, 7)
fridge = Refrigerator("LG", 150, 300)

print(wm)
print(wm.turn_on())
print(fridge)
print(fridge.turn_on())
