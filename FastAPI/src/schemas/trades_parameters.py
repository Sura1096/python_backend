from dataclasses import dataclass


@dataclass
class LastTradingDatesParams:
    limit: int
    offset: int


@dataclass
class DynamicsParams:
    start_date: str
    end_date: str
    limit: int
    offset: int
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None


@dataclass
class TradingResultsParams:
    limit: int
    offset: int
    oil_id: str | None = None
    delivery_basis_id: str | None = None
    delivery_type_id: str | None = None
