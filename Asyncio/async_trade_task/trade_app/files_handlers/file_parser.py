import asyncio
import os

import aiofiles
import xlrd


class FilesParser:
    def __init__(self) -> None:
        """Класс для парсинга XLS-файлов."""
        self.file_content = {}
        self.file_name = 'oil_xls_202312'

    async def read_files(self) -> dict:
        """Асинхронно читает и парсит несколько XLS-файлов.

        :return: Словарь, содержащий имена файлов и их распарсенное содержимое.
        """
        files_list = self.__get_files_name_list(self.file_name)
        tasks = [
            asyncio.create_task(self.__read_single_file(file_name))
            for file_name in files_list
        ]
        results = await asyncio.gather(*tasks)
        for file_name, content in results:
            if content:
                self.file_content[file_name] = content
        return self.file_content

    async def __read_single_file(self, file_name: str) -> tuple:
        """Асинхронно читает и парсит один XLS-файл.

        :param file_name: Имя файла для чтения и парсинга.
        :return: Кортеж, содержащий имя файла и его распарсенное содержимое.
        Если файл не найден, возвращается (file_name, None).
        """
        path = os.path.join('bulletins', file_name)
        try:
            async with aiofiles.open(path, mode='rb') as file:
                content = await file.read()
            sheet = xlrd.open_workbook(file_contents=content).sheet_by_index(0)

            start_row = self.__get_start_row(sheet)
            end_row = self.__get_end_row(sheet)

            parsed_file_info = self.__parse_file(start_row, end_row, sheet)
            return file_name, parsed_file_info
        except FileNotFoundError:
            return file_name, None

    @staticmethod
    def __get_files_name_list(start_file_name: str) -> list:
        """Генерирует список имен файлов.

        :param start_file_name: Начало имени файла.
        :return: Список имен файлов.
        """
        files_name_list = []
        for date in range(1, 32):
            full_file_name = (
                f'{start_file_name}0{date}162000.xls'
                if len(str(date)) < 2
                else f'{start_file_name}{date}162000.xls'
            )
            files_name_list.append(full_file_name)
        return files_name_list

    @staticmethod
    def __get_start_row(sheet: xlrd.sheet.Sheet) -> int:
        """Находит номер строки, с которой начинается таблица данных.

        :param sheet: Лист Excel.
        :return: Номер строки, с которой начинается таблица данных.
        """
        start_row = None
        for row_idx in range(sheet.nrows):
            row_values = sheet.row_values(row_idx)
            if 'Единица измерения: Метрическая тонна' in row_values:
                start_row = row_idx + 2  # Начинаем со строки после заголовка
                break

        # Проверяем, нашли ли таблицу
        if start_row is None:
            msg = "Таблица с 'Единица измерения: Метрическая тонна' не найдена."
            raise ValueError(msg)
        return start_row

    @staticmethod
    def __get_end_row(sheet: xlrd.sheet.Sheet) -> int:
        """Находит номер строки, с которой заканчивается таблица данных.

        :param sheet: Лист Excel.
        :return: Номер строки, с которой заканчивается таблица данных.
        """
        end_row = None
        for row_idx in range(sheet.nrows):
            row_values = sheet.row_values(row_idx)
            if 'Итого:' in row_values:
                end_row = row_idx
                break
        return end_row

    @staticmethod
    def __parse_file(start_row: int, end_row: int, sheet: xlrd.sheet.Sheet) -> list:
        """Парсит данные из листа Excel.

        :param start_row: Номер строки, с которой начинается таблица данных.
        :param end_row: Номер строки, с которой заканчивается таблица данных.
        :param sheet: Лист Excel.
        :return: Список словарей, где каждый словарь содержит данные одной строки из таблицы.
        """
        data = []

        for row_idx in range(start_row, end_row):
            row_values = sheet.row_values(row_idx)

            contracts_count_str = row_values[14]  # "Количество Договоров, шт."
            if contracts_count_str and contracts_count_str.isdigit():
                contracts_count = int(contracts_count_str)
                if contracts_count > 0:
                    extracted_row = {
                        'exchange_product_id': row_values[1],
                        'exchange_product_name': row_values[2],
                        'oil_id': row_values[1][:4],
                        'delivery_basis_id': row_values[1][4:7],
                        'delivery_basis_name': row_values[3],
                        'delivery_type_id': row_values[1][-1],
                        'volume': int(row_values[4]) if row_values[4].isdigit() else 0,
                        'total': int(row_values[5]) if row_values[5].isdigit() else 0,
                        'count': contracts_count,
                    }
                    data.append(extracted_row)
        return data
