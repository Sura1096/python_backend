from server import Server
from data import Data


class Router:
    def __init__(self):
        self.servers = {}  # Словарь для хранения подключенных серверов
        self.buffer: list[Data] = []  # Список для хранения принятых от серверов пакетов (объектов класса Data)

    def link(self, server: Server) -> None:
        """
        Присоединяет сервер к роутеру.

        :param server: Объект класса Server
        :return: None
        """
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server: Server) -> None:
        """
        Отсоединяет сервер от роутера.

        :param server: Объект класса Server
        :return:
        """
        if server.get_ip() in self.servers:
            del self.servers[server.get_ip()]
            server.router = None

    def send_data(self) -> None:
        """
        Отправляет все пакеты из буфера роутера соответствующим серверам
        (после отправки буфер очищается)

        :return: None
        """
        for data in self.buffer:
            self.servers[data.ip].buffer.append(data)
        self.buffer = []
