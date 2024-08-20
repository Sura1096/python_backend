from оbj_list import ObjList


class LinkedList:
    def __init__(self):
        self.head = None  # Ссылка на первый объект связанного списка
        self.tail = None  # Ссылка на последний объект связанного списка

    def add_obj(self, obj: ObjList) -> None:
        """
        Добавляет новый объект obj класса ObjList в конец связанного списка.

        :param obj: Объект obj класса ObjList
        :return: None
        """
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self) -> None:
        """
        Удаляет последний объект связанного списка.

        :return: None
        """
        if not self.head:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self) -> list:
        """
        Возвращает список строк локального свойства __data всех объектов связанного списка.

        :return: Список значений объектов связанного списка
        """
        linked_list = []
        cur_node = self.head
        while cur_node:
            linked_list.append(cur_node.get_data())
            cur_node = cur_node.get_next()
        return linked_list
