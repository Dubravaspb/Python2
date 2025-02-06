import doctest


class Car:
    def __init__(self, make: str, model: str, fuel_capacity: float):
        """
        Инициализация объекта "Автомобиль".

        :param make: Производитель автомобиля (например, Toyota, Ford).
        :param model: Модель автомобиля (например, Camry, Mustang).
        :param fuel_capacity: Объем бака в литрах. Должен быть положительным.

        :raises ValueError: Если объем бака <= 0.
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой.")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой.")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Объем бака должен быть положительным числом.")
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.current_fuel = 0.0  # Текущий уровень топлива в литрах

    def refuel(self, liters: float) -> None:
        """
        Заправляет автомобиль.

        :param liters: Количество заправляемого топлива. Должно быть положительным и не превышать свободный объем бака.
        :raises ValueError: Если количество топлива превышает свободный объем бака или отрицательно.
        """
        pass

    def drive(self, distance: float) -> float:
        """
        Уменьшает уровень топлива в зависимости от пройденного расстояния.

        :param distance: Расстояние в километрах. Должно быть положительным.
        :raises ValueError: Если топлива недостаточно для преодоления указанного расстояния.
        :return: Расстояние, которое удалось проехать.
        """
        pass

    def check_fuel_level(self) -> float:
        """
        Возвращает текущий уровень топлива в баке.

        :return: Уровень топлива в литрах.
        """
        pass


if __name__ == "__main__":
    doctest.testmod()


class Library:
    def __init__(self, name: str, address: str, capacity: int):
        """
        Инициализация объекта "Библиотека".

        :param name: Название библиотеки.
        :param address: Адрес библиотеки.
        :param capacity: Максимальное количество книг, которые могут храниться в библиотеке.

        :raises ValueError: Если вместимость <= 0.
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой.")
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом.")
        self.name = name
        self.address = address
        self.capacity = capacity
        self.books = []  # Список книг в библиотеке

    def add_book(self, book_title: str) -> None:
        """
        Добавляет книгу в библиотеку.

        :param book_title: Название книги.
        :raises ValueError: Если библиотека переполнена.
        """
        pass

    def lend_book(self, book_title: str) -> bool:
        """
        Выдаёт книгу посетителю.

        :param book_title: Название книги.
        :return: True, если книга выдана успешно, иначе False.
        """
        pass

    def list_books(self) -> list[str]:
        """
        Возвращает список доступных книг в библиотеке.

        :return: Список книг.
        """
        pass

if __name__ == "__main__":
    doctest.testmod()



class Website:
    def __init__(self, domain: str, daily_visitors: int, is_active: bool):
        """
        Инициализация объекта "Вебсайт".

        :param domain: Доменное имя вебсайта.
        :param daily_visitors: Количество посетителей в день. Должно быть неотрицательным.
        :param is_active: Флаг, активен ли вебсайт.

        :raises ValueError: Если количество посетителей отрицательное.
        """
        if not isinstance(domain, str):
            raise TypeError("Домен должен быть строкой.")
        if not isinstance(daily_visitors, int) or daily_visitors < 0:
            raise ValueError("Количество посетителей должно быть неотрицательным числом.")
        if not isinstance(is_active, bool):
            raise TypeError("Параметр is_active должен быть логическим значением.")
        self.domain = domain
        self.daily_visitors = daily_visitors
        self.is_active = is_active

    def toggle_active_status(self) -> None:
        """
        Изменяет статус активности вебсайта.
        """
        pass

    def update_daily_visitors(self, new_count: int) -> None:
        """
        Обновляет количество ежедневных посетителей.

        :param new_count: Новое количество посетителей. Должно быть неотрицательным.
        :raises ValueError: Если переданное значение отрицательное.
        """
        pass

    def get_website_statistics(self) -> dict:
        """
        Возвращает статистику вебсайта.

        :return: Словарь с данными о домене, посетителях и статусе.
        """
        pass



if __name__ == "__main__":
    doctest.testmod()
