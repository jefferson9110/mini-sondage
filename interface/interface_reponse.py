from abc import ABC, abstractmethod

class IResponseRepository(ABC):

    @abstractmethod
    def get_by_id(self, response_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_survey(self, survey_id: int):
        pass