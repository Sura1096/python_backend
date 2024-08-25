from utils.unitofwork import IUnitOfWork


class TradingService:
    def __init__(self, uow: IUnitOfWork) -> None:
        self.uow = uow

    async def add_info(self, data: dict) -> None:
        async with self.uow:
            await self.uow.trading.add_trading_info(data)
            await self.uow.commit()
