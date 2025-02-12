class Guitar:
    """Базовый класс для гитар."""

    def __init__(self, brand: str, model: str, strings: int, price: float) -> None:
        """
        Инициализация гитары.

        :param brand: Бренд гитары.
        :param model: Модель гитары.
        :param strings: Количество струн на гитаре.
        :param price: Цена гитары.
        """
        self.__brand = brand  # Относится только к брендам гитар
        self.__model = model  # Относится только к моделям гитар
        self.__strings = strings  # Из струнных инструментов только гитары
        self.__price = price  # У каждой гитары своя цена закупки

    def __str__(self) -> str:
        """Возвращает строковое представление гитары."""
        return f"{self.__brand} {self.__model} - {self.__strings} strings, ${self.__price:.2f}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление гитары."""
        return f"Guitar(brand='{self.__brand}', model='{self.__model}', strings={self.__strings}, price={self.__price})"

    def tune_standard(self) -> str:
        """Настроить гитару в стандартный строй"

        :return: Названия нот с первой по шестую струну через пробел
        """
        return "E B G D A E"

    def play(self) -> str:
        """Сыграть. Возвращает звук, который издает гитара.

        :return: Строка с описанием звука.
        """
        return "Звук объемный и льющийся!"


class ElectricGuitar(Guitar):
    """Класс для электрогитар, унаследованный от Guitar."""

    def __init__(self, brand: str, model: str, strings: int, price: float, pickup_type: str) -> None:
        """
        Инициализация электрогитары.

        :param brand: Бренд электрогитары.
        :param model: Модель электрогитары.
        :param strings: Количество струн на электрогитаре.
        :param price: Цена электрогитары.
        :param pickup_type: Тип звукоснимателя электрогитары.
        """
        super().__init__(brand, model, strings, price)
        self.__pickup_type = pickup_type  # Относится только к электрогитарам

    def __str__(self) -> str:
        """Возвращает строковое представление электрогитары, включая тип звукоснимателя."""
        return f"{super().__str__()} | Pickup Type: {self.__pickup_type}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление электрогитары."""
        return f"ElectricGuitar(brand='{self._Guitar__brand}', model='{self._Guitar__model}', strings={self._Guitar__strings}, price={self._Guitar__price}, pickup_type='{self.__pickup_type}')"

    def play(self) -> str:
        """Переопределяет метод play, чтобы вернуть звук электрогитары.

        Переопределение осуществляется, чтобы отразить уникальное звучание электрогитары, которое отличается от акустической.

        :return: Строка с описанием звука электрогитары.
        """
        return "Звук чистый, стеклянный, глухой без усилителя... НО С ПЕРЕГРУЗОМ РРРЫЧИТ!!!!"


# Пример использования классов
if __name__ == "__main__":
    acoustic_guitar = Guitar("Yamaha", "FG800", 6, 399.99)
    print(acoustic_guitar)  # Выводит подробности об акустической гитаре
    print(repr(acoustic_guitar))  # Выводит формальное представление
    print(acoustic_guitar.tune_standard()) # Настроим гитару
    print(acoustic_guitar.play()) # Проверим звучание

    electric_guitar = ElectricGuitar("Fender", "Stratocaster", 6, 899.99, "Single-coil")
    print(electric_guitar)  # Выводит подробности об электрогитаре
    print(repr(electric_guitar))  # Выводит формальное представление
    print(acoustic_guitar.tune_standard()) # Настроим гитару
    print(electric_guitar.play())  # Выводит подробности об электрогитаре
