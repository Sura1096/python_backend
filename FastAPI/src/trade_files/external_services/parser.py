import asyncio

import aiohttp

from src.schemas.files import FileContentFromUrl


class WebParser:
    def __init__(self) -> None:
        """Инициализирует объект WebParser с начальным URL."""
        self.url = 'https://spimex.com/upload/reports/oil_xls/oil_xls_202312'

    async def get_files(self) -> FileContentFromUrl:
        """Асинхронно получает и возвращает XLS-файлы с сайта spimex.com.

        :return: Словарь, содержащий имена файлов и их содержимое.
        """
        urls = self.__generate_urls(self.url)
        bulletins = await self.__get_bulletins_from_urls(urls)
        return self.__get_xls_files_dict(bulletins)

    @staticmethod
    def __generate_urls(start_url: str) -> list[str]:
        """Генерирует список URL для загрузки XLS-файлов с сайта spimex.com.

        :param start_url: Начальный URL для генерации.
        :return: Список сгенерированных URL.
        """
        urls = []
        for date in range(1, 32):
            full_url = (
                f'{start_url}0{date}162000.xls'
                if len(str(date)) < 2
                else f'{start_url}{date}162000.xls'
            )
            urls.append(full_url)
        return urls

    async def __get_bulletins_from_urls(self, urls: list[str]) -> list:
        """Асинхронно загружает содержимое файлов по списку URL.

        :param urls: Список URL для загрузки файлов.
        :return: Список словарей, содержащих имя файла и его содержимое.
        """
        async with aiohttp.ClientSession() as session:
            files = [
                asyncio.create_task(self.__get_file_content(url, session))
                for url in urls
            ]
            return await asyncio.gather(*files)

    @staticmethod
    async def __get_file_content(
        url: str,
        session: aiohttp.ClientSession,
    ) -> FileContentFromUrl:
        """Асинхронно загружает содержимое файла по указанному URL.

        :param url: URL для загрузки файла.
        :param session: Сессия aiohttp для выполнения запроса.
        :return: Словарь, содержащий имя файла и его содержимое.
        Если запрос не удался, возвращает пустой словарь.
        """
        result = {}
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    file_name = url.split('/')[-1]
                    file_content = await response.read()
                    result = {file_name: file_content}
        except aiohttp.ClientConnectorError:
            result = {}
        return FileContentFromUrl(result)

    @staticmethod
    def __get_xls_files_dict(bulletins: list) -> FileContentFromUrl:
        """Формирует единый словарь из списка ответов с файлами.

        :param bulletins: Список словарей, содержащих имена файлов и их содержимое.
        :return: Словарь, содержащий все файлы и их содержимое.
        """
        xls_files = {}
        for bulletin in bulletins:
            xls_files.update(bulletin.files)
        return FileContentFromUrl(xls_files)
