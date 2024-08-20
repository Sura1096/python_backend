class ObjList:
    def __init__(self, data: str):
        self.__next = None  # Ссылка на следующий объект связанного списка
        self.__prev = None  # Ссылка на предыдущий объект связанного списка
        self.__data = data  # Значение объекта

    def set_next(self, obj) -> None:
        """
        Изменяет приватное свойство __next на значение obj.

        :param obj: Новый объект связанного списка, на который необходимо изменить приватное свойство __next
        :return: None
        """
        self.__next = obj

    def set_prev(self, obj) -> None:
        """
        Изменяет приватное свойство __prev на значение obj.

        :param obj: Новый объект связанного списка, на который необходимо изменить приватное свойство __prev
        :return: None
        """
        self.__prev = obj

    def get_next(self):
        """
        Возвращает значение приватного свойства __next.

        :return: Значение приватного свойства __next
        """
        return self.__next

    def get_prev(self):
        """
        Возвращает значение приватного свойства __prev.

        :return: Значение приватного свойства __prev
        """
        return self.__prev

    def set_data(self, data: str) -> None:
        """
        Изменяет приватное свойство __data на значение data.

        :param data: Строка с данными
        :return: None
        """
        self.__data = data

    def get_data(self) -> str:
        """
        Возвращает значение приватного свойства __data.

        :return: Значение приватного свойства __data
        """
        return self.__data
