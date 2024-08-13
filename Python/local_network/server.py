from data import Data


class Server:
    ip_counter = 0  # Счетчик IP-адреса

    def __init__(self):
        self.buffer: list[Data] = []  # Список принятых пакетов (объекты класса Data)
        self.ip = self.generate_ip()  # IP-адрес текущего сервера
        self.router = None  # Присвоение роутера к текущему серверу при подключении сервера к роутеру

    @classmethod
    def generate_ip(cls) -> int:
        """
        Возвращает новый сгенерированный IP-адрес при создании экземпляра класса Server.

        :return: Новый IP-адрес
        """
        cls.ip_counter += 1
        return cls.ip_counter

    def send_data(self, data: Data) -> None:
        """
        Отправляет информационный пакет data с указанным IP-адресом получателя роутеру
        (пакет сохраняется в буфере роутера).

        :param data: Объект класса Data
        :return: None
        """
        if self.router:
            self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        """
        Возвращает список принятых пакетов и очищает буфер сервера.

        :return: Список принятых пакетов сервера
        """
        data = self.buffer[:]
        self.buffer = []
        return data

    def get_ip(self) -> int:
        """
        Возвращает свой IP-адрес.

        :return: IP-адрес
        """
        return self.ip
