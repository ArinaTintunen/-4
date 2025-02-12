class SocialNetwork:
    """
    Базовый класс для социальных сетей.
    """

    def __init__(self, name: str, launch_year: int) -> None:
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param launch_year: Год запуска социальной сети.
        """
        self._name = name  # Непубличный атрибут для названия сети
        self._launch_year = launch_year  # Непубличный атрибут для года запуска

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        :return: Строка с названием и годом запуска.
        """
        return f"{self._name}, launched in {self._launch_year}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        :return: Строка с информацией о социальной сети в формате для отладки.
        """
        return f"SocialNetwork(name={self._name!r}, launch_year={self._launch_year!r})"

    def get_age(self) -> int:
        """
        Возвращает возраст социальной сети в годах.

        :return: Возраст социальной сети.
        """
        current_year = 2023  # Можно заменить на динамическое получение текущего года
        return current_year - self._launch_year


class VK(SocialNetwork):
    """
    Класс для социальной сети ВКонтакте, наследует от SocialNetwork.
    """

    def __init__(self, launch_year: int, user_count: int) -> None:
        """
        Инициализация ВКонтакте.

        :param launch_year: Год запуска ВКонтакте.
        :param user_count: Количество пользователей ВКонтакте.
        """
        super().__init__("VK", launch_year)  # Вызов конструктора базового класса
        self._user_count = user_count  # Непубличный атрибут для количества пользователей

    def __str__(self) -> str:
        """
        Возвращает строковое представление ВКонтакте.

        :return: Строка с названием, годом запуска и количеством пользователей.
        """
        return f"{super().__str__()} with {self._user_count} users"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки ВКонтакте.

        :return: Строка с информацией о ВКонтакте в формате для отладки.
        """
        return f"VK(launch_year={self._launch_year!r}, user_count={self._user_count!r})"

    def get_popularity_index(self) -> float:
        """
        Возвращает индекс популярности ВКонтакте.

        Индекс рассчитывается на основе количества пользователей и возраста сети.

        :return: Индекс популярности.
        """
        return self._user_count / self.get_age()  # Простой расчет индекса популярности


class Facebook(SocialNetwork):
    """
    Класс для социальной сети Facebook, наследует от SocialNetwork.
    """

    def __init__(self, launch_year: int, user_count: int, ad_revenue: float) -> None:
        """
        Инициализация Facebook.

        :param launch_year: Год запуска Facebook.
        :param user_count: Количество пользователей Facebook.
        :param ad_revenue: Годовой доход от рекламы Facebook.
        """
        super().__init__("Facebook", launch_year)  # Вызов конструктора базового класса
        self._user_count = user_count  # Непубличный атрибут для количества пользователей
        self._ad_revenue = ad_revenue  # Непубличный атрибут для дохода от рекламы

    def __str__(self) -> str:
        """
        Возвращает строковое представление Facebook.

        :return: Строка с названием, годом запуска, количеством пользователей и доходом от рекламы.
        """
        return f"{super().__str__()} with {self._user_count} users and ${self._ad_revenue} revenue"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки Facebook.

:return: Строка с информацией о Facebook в формате для отладки.
        """
        return f"Facebook(launch_year={self._launch_year!r}, user_count={self._user_count!r}, ad_revenue={self._ad_revenue!r})"

    def get_ad_revenue_per_user(self) -> float:
        """
        Возвращает доход от рекламы на пользователя.

        Метод перегружен для добавления специфической информации о доходе от рекламы.

        :return: Доход от рекламы на пользователя.
        """
        if self._user_count == 0:
            return 0.0  # Защита от деления на ноль
        return self._ad_revenue / self._user_count  # Расчет дохода на пользователя


if __name__ == "__main__":
    vk = VK(2006, 100000000)
    facebook = Facebook(2004, 2900000000, 11700000000)

    print(vk)
    print(repr(vk))
    print(f"VK popularity index: {vk.get_popularity_index()}")

    print(facebook)
    print(repr(facebook))
    print(f"Facebook ad revenue per user: {facebook.get_ad_revenue_per_user()}")