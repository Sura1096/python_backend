import os
import xlrd


class FilesParser:
    def __init__(self):
        self.file_content = {}
        self.file_name = 'oil_xls_202312'

    def read_files(self):
        files_list = self.__get_files_name_list()

        for file_name in files_list:
            path = os.path.join('bulletins', file_name)
            try:
                content = xlrd.open_workbook(path).sheet_by_index(0)
                start_row = self.__get_start_row(content)
                parsed_file_info = self.__parse_file(start_row, content)
                self.file_content[file_name] = parsed_file_info
            except FileNotFoundError:
                continue
        return self.file_content

    def __get_files_name_list(self):
        files_name_list = []
        for date in range(1, 32):
            full_file_name = (
                f'{self.file_name}0{date}162000.xls'
                if len(str(date)) < 2
                else f'{self.file_name}{date}162000.xls'
            )
            files_name_list.append(full_file_name)
        return files_name_list

    def __get_start_row(self, sheet) -> int:
        start_row = None
        for row_idx in range(sheet.nrows):
            row_values = sheet.row_values(row_idx)
            if "Единица измерения: Метрическая тонна" in row_values:
                start_row = row_idx + 2  # Начинаем со строки после заголовка
                break

        # Проверяем, нашли ли таблицу
        if start_row is None:
            raise ValueError(
                "Таблица с 'Единица измерения: Метрическая тонна' не найдена."
            )
        return start_row

    def __parse_file(self, start_row: int, sheet):
        data = []

        for row_idx in range(start_row, sheet.nrows):
            row_values = sheet.row_values(row_idx)

            # Прерываем итерацию, если достигли конца таблицы
            if all(value == '' for value in row_values):
                break

            # Извлекаем нужные колонки
            contracts_count_str = row_values[14]  # "Количество Договоров, шт."
            if contracts_count_str and contracts_count_str.isdigit():
                contracts_count = int(contracts_count_str)
                if contracts_count > 0:
                    extracted_row = {
                        "Код Инструмента": row_values[1],
                        "Наименование Инструмента": row_values[2],
                        "Базис поставки": row_values[3],
                        "Объем Договоров в единицах измерения": row_values[4],
                        "Объем Договоров, руб.": row_values[5],
                        "Количество Договоров, шт.": contracts_count,
                    }
                    data.append(extracted_row)
        return data
