import asyncio

import aiohttp


class WebParser:
    def __init__(self) -> None:
        """Инициализирует объект WebParser с начальным URL."""
        self.url = 'https://spimex.com/upload/reports/oil_xls/oil_xls_202312'

    async def get_files(self) -> dict:
        urls = self.__generate_urls(self.url)
        bulletins = await self.__get_bulletins_from_urls(urls)
        return self.__get_xls_files_dict(bulletins)

    @staticmethod
    def __generate_urls(start_url: str) -> list:
        """Генерирует список URL для загрузки XLS-файлов с сайта spimex.com.

        Args:
        ----
            start_url (str): Начальный URL для генерации.

        Returns:
        -------
            list: Список сгенерированных URL.

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

    async def __get_bulletins_from_urls(self, urls: list) -> list:
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
    ) -> dict:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    file_name = url.split('/')[-1]
                    file_content = await response.read()
                    return {file_name: file_content}
                return {}
        except aiohttp.ClientConnectorError:
            return {}

    @staticmethod
    def __get_xls_files_dict(responses) -> dict:
        xls_files = {}
        for response in responses:
            xls_files.update(response)
        return xls_files
