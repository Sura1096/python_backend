import asyncio

from external_services.parser import WebParser
from files_handlers.files_content import files_parse
from files_handlers.storage import FilesSaver
from services.trading_service import TradingService
from utils.unitofwork import UnitOfWork


def save_bulletin_files() -> None:
    """Загружает XLS-файлы с сайта и сохраняет их в папку "bulletins".

    Args:
    ----
        None

    """
    parse_urls = WebParser()
    url_dict = parse_urls._get_all_url()

    files_saver = FilesSaver(url_dict)
    files_saver.save_files()


async def main() -> None:
    """Основная функция, которая парсит файлы, извлекает информацию и сохраняет ее в базу данных.

    Args:
    ----
        None

    """
    bulletins_info = files_parse()
    async with UnitOfWork() as uow:
        trading_service = TradingService(uow)
        for content in bulletins_info.values():
            for cell in content:
                await trading_service.add_info(cell)


if __name__ == '__main__':
    asyncio.run(main())
