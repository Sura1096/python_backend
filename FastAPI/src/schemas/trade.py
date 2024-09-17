from datetime import date

from pydantic import BaseModel


class LastTradeResponse(BaseModel):
    trade_date: date


class TradeDynamicsRequest(BaseModel):
    start_date: date
    end_date: date
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None


class TradeResultsRequest(BaseModel):
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None


class TradeResponse(BaseModel):
    id: int
    exchange_product_id: str
    exchange_product_name: str
    oil_id: str
    delivery_basis_id: str
    delivery_basis_name: str
    delivery_type_id: str
    volume: int
    total: int
    count: int
    date: date
    created_on: date
    updated_on: date
