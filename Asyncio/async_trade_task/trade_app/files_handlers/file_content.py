from datetime import date

from .file_parser import FilesParser


def get_date(filename: str) -> date:
    """Извлекает дату из имени файла.

    :param filename: Имя файла в формате 'oil_xls_20231201162000.xls'.
    :return: Объект даты, извлеченный из имени файла.
    """
    extract_bulletin_date = filename.split('_')[-1][:8]
    bulletin_date = (
        extract_bulletin_date[:4]
        + '-'
        + extract_bulletin_date[4:6]
        + '-'
        + extract_bulletin_date[6:8]
    )
    return date.fromisoformat(bulletin_date)


async def files_parse() -> dict:
    """Асинхронно парсит файлы и добавляет информацию о датах.

    :return: Словарь, где ключ - имя файла, а значение - список словарей,
    где каждый словарь содержит информацию о строке из файла, включая дату.
    """
    files_parser = FilesParser()
    info = await files_parser.read_files()
    for file, content in info.items():
        bulletin_date = get_date(file)
        for cell in content:
            cell['date'] = bulletin_date
            cell['created_on'] = date.today()
            cell['updated_on'] = date.today()

    return info
