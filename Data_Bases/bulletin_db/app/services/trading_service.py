from utils.unitofwork import IUnitOfWork


class TradingService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_info(self, data: dict):
        async with self.uow:
            await self.uow.trading.add_trading_info(data)
            await self.uow.commit()
