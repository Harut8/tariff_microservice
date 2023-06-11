from abc import abstractmethod, ABCMeta
from typing import Union
from models.user_model.user_model import UserInfo, UserRegistration


class TarifServiceInterface(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    async def get_tarifes_for_view(language):
        ...
