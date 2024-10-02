from datetime import date

from pydantic import BaseModel, Field


class LastTradeRequest(BaseModel):
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)


class LastTradeResponse(BaseModel):
    date: date


class TradeDynamicsRequest(BaseModel):
    start_date: date
    end_date: date
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None


class TradeResultsRequest(BaseModel):
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)


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


class TradeDb(BaseModel):
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


class TradeEndpoint(BaseModel):
    data: list[TradeResponse]


class LastTradeDatesEndpoint(BaseModel):
    data: list[LastTradeResponse]
