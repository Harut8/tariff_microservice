from models.user_model.user_model import UserRegistration
from repository.core.core import DbConnection, fetch_row_transaction, insert_row_transaction, fetch_transaction
from dataclasses import dataclass
from repository.tariff_db_manager.tariff_db_interface import TariffDbInterface
from asyncpg import Record


@dataclass
class TariffDbManager(TariffDbInterface):

    @staticmethod
    async def get_tarifes_for_view() -> list[Record]:
        _tariff_info = await fetch_transaction("""SELECT * from get_tarifes_for_view()""")
        return _tariff_info

    @staticmethod
    async def get_tariff_details(tariff_id):
        _tariff_details = await fetch_transaction(
            """select * from get_tarif_details($1)""",
            tariff_id)
        print(_tariff_details)
        return _tariff_details
