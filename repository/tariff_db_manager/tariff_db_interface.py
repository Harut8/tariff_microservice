from abc import abstractmethod, ABCMeta

from asyncpg import Record


class TariffDbInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    async def get_tarifes_for_view() -> list[Record]:
        ...

