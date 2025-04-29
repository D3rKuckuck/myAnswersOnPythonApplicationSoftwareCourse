
class Tree:
    """
    Класс принимает информацию о дереве и ведет её учет.
    """
    def __init__(self, name: str, height: int, age: int, branches: int) -> None:
        """
        Функция инициализации.

        :param name: Количество отрезаемых веток.
        :param height: Высота дерева.
        :param age: Возраст дерева.
        :param branches: Кол-во ветвей дерева.
        :return: None.
        """
        self.name = name
        self.height = height
        self.age = age
        self.branches = branches
        self.tree_information = {str(name): {"Высота": height, "Возраст": age, "Ветки": branches}}
        if not isinstance(name, str) or not isinstance(height, int) or not isinstance(age, int) \
                or not isinstance(branches, int):
            raise TypeError(
                "Название дерева имеет тип str.\n"
                "Высота целое значение типа int в метрах.\n"
                "Возраст дерева имеет тип int.\n"
                "Кол-во веток должно иметь тип int.\n"
            )  # вызываем ошибку
        if height <= 0 or age <= 0:
            raise ValueError("Высота и возраст должны быть положительными числами")
        if branches < 0:
            raise ValueError("Кол-во веток не должно быть отрицательным")
        pass

    def cut(self, value: int) -> dict:
        """
        Обрезает указанное количество веток.

        :param value: Количество отрезаемых веток.
        :return: Обновленная информация о дереве (self.tree_information).

        Примеры:

        >>> tree = Tree("Дуб", 10, 5, 20)
        >>> tree.cut(5)
        Данные о дереве до обрезки веток
        {'Дуб': {'Высота': 10, 'Возраст': 5, 'Ветки': 20}}
        <BLANKLINE>
        Данные о дереве после обрезки веток
        {'Дуб': {'Высота': 10, 'Возраст': 5, 'Ветки': 15}}
        <BLANKLINE>
        {'Дуб': {'Высота': 10, 'Возраст': 5, 'Ветки': 15}}
        """
        if not isinstance(value, int):
            raise ValueError("Кол-во отрезаемых веток должно быть типа int.")
        if value > self.branches or value < 0:
            raise ValueError("Кол-во отрезаемых веток не может быть больше кол-ва имеющихся и не должно быть отрицательным.")
        print("Данные о дереве до обрезки веток")
        print(f"{self.tree_information}\n")
        print("Данные о дереве после обрезки веток")
        value = self.branches - value
        new_branches = {"Ветки": value}
        for sub in self.tree_information:
            for sub_sub in self.tree_information[sub]:
                if sub_sub in new_branches:
                    self.tree_information[sub][sub_sub] = new_branches[sub_sub]
        print(f"{self.tree_information}\n")
        return self.tree_information

    def print_info(self) -> None:
        """
        Функция выводит данные о дереве.

        :return: None
        Пример:

        >>> tree = Tree("Дуб", 10, 5, 20)
        >>> tree.print_info()
        Данные о дереве
        {'Дуб': {'Высота': 10, 'Возраст': 5, 'Ветки': 20}}
        <BLANKLINE>
        """
        print("Данные о дереве")
        print(f"{self.tree_information}\n")


class Guitar:
    """
    Класс принимает данные о гитаре и позволяе получить данные о сыгранных нотах
    """
    def __init__(self, construction: str, strings: int, voice: str) -> None:
        """
        Функция инициализации.

        :param construction: Конструкция "акустика"/"электро".
        :param strings: Кол-во струн (счёт ведется от нижней струны).
        :param voice: Диапазон звучания "тенор"/"баритон"/"бас".
        :return: None.
        """
        if not isinstance(construction, str) or not isinstance(strings, int) or not isinstance(voice, str):
            raise TypeError(
                "Конструкция указывается, как str\n"
                "Кол-во струн указывается, как int.\n"
                "Диапазон указывается, как str.\n"
            )  # вызываем ошибку
        if construction != "акустика" and construction != "электро":
            raise ValueError(
                '''Используйте для construction "акустика" или "электро"'''
            )  # вызываем ошибку
        if voice != "тенор" and voice != "баритон" and voice != "бас":
            raise ValueError(
                '''Используйте для voice "тенор", "баритон" или "бас"'''
            )  # вызываем ошибку
        if strings <= 0:
            raise ValueError(
                '''Должна быть хотябы одна струна'''
            )  # вызываем ошибку
        self.construction = construction
        self.strings = strings
        self.voice = voice
        self.information = {"Construction": construction, "strings": strings, "voice": voice}
        pass

    def play_on_fret(self, fret: int, string: int) -> None:
        """
        Функция выводит в терминал название сыгранной ноты.
        Пример:

        >>> nota = Guitar("акустика", 6, "тенор")
        >>> nota.play_on_fret(0,7)
        Traceback (most recent call last):
        ...
        ValueError: Номер струны должен быть больше нуля и не больше кол-ва струн,
                        а номер лада не может быть отрицательным


        :param fret: Номер лада".
        :param string: Номер струны".
        :return: None.
        """
        if not isinstance(fret, int) or not isinstance(string, int):
            raise TypeError(
                "Метод принимает только целые числа в качестве аргументов"
            )  # вызываем ошибку
        if string <= 0 or fret < 0 or string > self.strings:
            raise ValueError(
                '''Номер струны должен быть больше нуля и не больше кол-ва струн,
                а номер лада не может быть отрицательным'''
            )  # вызываем ошибку
        ...

    def chord(self, fret: int, string: int) -> None:
        """
        Функция выводит в терминал названия нот в power-аккорде от заданного лада и струны.
        Если струн недостаточно, для построения данного аккорда,
        то выводится соответствующее сообщение.
        :param fret: Номер лада".
        :param string: Номер струны".
        :return: None.
        """
        if not isinstance(fret, int) or not isinstance(string, int):
            raise TypeError(
                "Метод принимает только целые числа в качестве аргументов"
            )  # вызываем ошибку
        if string <= 0 or fret < 0 or string > self.strings:
            raise ValueError(
                '''Номер струны должен быть больше нуля и не больше кол-ва струн,
                а номер лада не может быть отрицательным'''
            )  # вызываем ошибку
        if string <= 2:
            raise ValueError("От данной с руны power-аккорд не построить, "
                             "возьмите струну выше, если есть возможность")
        ...


class Amplifier:
    """
    Класс принимает данные о об усилителе, соответствующие методы их изменяют.
    """
    def __init__(self, power: bool, selected_channel: int):
        """
        Функция инициализации.

        :param power: Состояние питания.
        :param selected_channel: Выбранный канал звучания, где 1 - clean, 2 - gain.
        :return: None.
        """
        if not isinstance(power, bool) or not isinstance(selected_channel, int):
            raise TypeError(
                "Параметр питания принимает значение типа bool."
                "Параметр канала принимает значения типа int."
            )  # вызываем ошибку
        if not 1 <= selected_channel <= 2:
            raise ValueError(
                "Используемые номера каналов: 1 или 2"
            )  # вызываем ошибку
        self.power = power
        self.selected_channel = selected_channel
        pass

    def on_off(self, power) -> None:
        """
        Откл/вкл питание усилителя.

        :param power: Состояние питания.
        :return: None.
        """
        if not isinstance(power, bool):
            raise TypeError(
                "Параметр питания принимает значение типа bool.")
        if self.power != power:
            self.power = power
        if self.power:
            print("Turned on!")
        else:
            print("Turned off!")

    def change_channel(self, selected_channel) -> None:
        """
        Смена канала.

        :param selected_channel: Номер необходимого канала.
        :return: None.
        """
        if not isinstance(selected_channel, int):
            raise TypeError(
                "Параметр канала принимает значения типа int."
            )  # вызываем ошибку
        if not 1 <= selected_channel <= 2:
            raise ValueError(
                "Используемые номера каналов: 1 или 2"
            )  # вызываем ошибку
        if self.selected_channel != selected_channel:
            self.selected_channel = selected_channel
        print("Selected chanel: "+str(self.selected_channel))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
