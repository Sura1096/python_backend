import asyncio

from src.api.services.trade_service import TradeService
from src.trade_files.external_services.parser import WebParser
from src.trade_files.files_handlers.file_content import files_parse
from src.trade_files.files_handlers.storage import FilesSaver
from src.utils.unit_of_work import UnitOfWork


async def save_bulletin_files() -> None:
    """Асинхронно загружает XLS-файлы с сайта и сохраняет их на диск.

    :return: None
    """
    parse_urls = WebParser()
    url_dict = await parse_urls.get_files()

    files_saver = FilesSaver(**url_dict.files)
    await files_saver.save_files()


async def save_into_db() -> None:
    """Асинхронно парсит сохраненные файлы и сохраняет их содержимое в базу данных.

    :return: None
    """
    bulletins_info = await files_parse()
    async with UnitOfWork() as uow:
        trading_service = TradeService(uow)
        for content in bulletins_info.files.values():
            for cell in content:
                await trading_service.add_one(**cell)


async def main() -> None:
    """Главная асинхронная функция для выполнения задач загрузки файлов и сохранения данных в базу.

    :return: None
    """
    save_files_task = asyncio.create_task(save_bulletin_files())
    save_info_into_db_task = asyncio.create_task(save_into_db())
    await asyncio.gather(save_files_task, save_info_into_db_task)


if __name__ == '__main__':
    asyncio.run(main())
