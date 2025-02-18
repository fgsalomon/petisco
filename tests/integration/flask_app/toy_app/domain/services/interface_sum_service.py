from abc import ABCMeta, abstractmethod
from typing import Dict

from meiga import Result, Error, NotImplementedMethodError

from petisco.application.service import Service


class ISumService(Service):
    __metaclass__ = ABCMeta

    def info(self) -> Dict:
        return {"name": self.__class__.__name__}

    @abstractmethod
    def execute(self, value1: int, value2: int) -> Result[int, Error]:
        raise NotImplementedMethodError
