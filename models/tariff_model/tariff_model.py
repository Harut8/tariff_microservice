import uuid
from enum import Enum
from typing import Union
from pydantic import BaseModel, validator, Field



class TarifDetails(BaseModel):
    tarif_id: str = None


class Language(Enum):
    ru = 'ru'
    en = 'en'
    hy = 'hy'


class InnerModelForTarif(BaseModel):
    """MODEL FOR INNER  CONTENT OF TARIF"""
    cassa_names: str = None
    cassa_counts: int = None
    cassa_prices: int = None
    cassa_inf_prices: int = None
    manager_names: str = None
    manager_counts: int = None
    manager_prices: int = None
    manager_inf_prices: int = None
    web_names: str = None
    web_counts: int = None
    web_prices: int = None
    web_inf_prices: int = None
    mobile_cassa_names: str = None
    mobile_cassa_counts: int = None
    mobile_prices: int = None
    mobile_inf_prices: int = None
    tarifes_others: list[str] = None


class TarifModelForView(BaseModel):
    """MODEL FOR TARIFES VIEW"""
    tarif_id: Union[str, uuid.UUID]
    tarif_names: str = None
    tarif_month_prices: int = None
    inner_content: InnerModelForTarif = None

    @validator('tarif_month_prices')
    def tarif_month_prices_check(cls, month_prices):
        if month_prices <= 0:
            return "FREE"
        return month_prices


class PersonalTarifForCreating(BaseModel):
    cass_stantion_price: int | None = Field(gt=0)
    mobile_cass_price: int | None = Field(gt=0)
    mobile_manager_price: int | None = Field(gt=0)
    web_manager_price: int | None = Field(gt=0)
    cass_stantion_count: int | None = Field(gt=-1)
    mobile_cass_count: int | None = Field(gt=-1)
    mobile_manager_count: int | None = Field(gt=-1)
    web_manager_count: int | None = Field(gt=-1)

    tarif_month: int | None = 1
