import asyncio
from external_services.parser import WebParser
from files_handlers.storage import FilesSaver
from files_handlers.files_content import files_parse
from utils.unitofwork import UnitOfWork
from services.trading_service import TradingService


def save_bulletin_files():
    parse_urls = WebParser()
    url_dict = parse_urls._get_all_url()

    files_saver = FilesSaver(url_dict)
    files_saver.save_files()


async def main():
    bulletins_info = files_parse()
    async with UnitOfWork() as uow:
        trading_service = TradingService(uow)
        for file, content in bulletins_info.items():
            for cell in content:
                await trading_service.add_info(cell)


if __name__ == '__main__':
    asyncio.run(main())
