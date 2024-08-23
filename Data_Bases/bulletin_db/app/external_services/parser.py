from urllib.request import urlopen
import urllib.error


class WebParser:
    def __init__(self):
        """
        Инициализирует объект WebParser с начальным URL.
        """
        self.url = 'https://spimex.com/upload/reports/oil_xls/oil_xls_202312'

    @staticmethod
    def __generate_urls(start_url):
        """
        Генерирует список URL для загрузки XLS-файлов с сайта spimex.com.

        Args:
            start_url (str): Начальный URL для генерации.

        Returns:
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

    def _get_all_url(self) -> dict:
        """
        Возвращает словарь валидных URL для скачивания XLS-файлов с сайта spimex.com.

        Returns:
            dict: Словарь, где ключ - имя файла, а значение - содержимое файла.
        """
        urls = self.__generate_urls(self.url)
        xls_files = {}

        for url in urls:
            try:
                url = urlopen(url)
                file_name = url.split('/')[-1]
                xls_files[file_name] = url.read()
            except urllib.error.HTTPError:
                continue

        return xls_files
