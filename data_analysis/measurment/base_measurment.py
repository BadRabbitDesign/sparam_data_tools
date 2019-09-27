import abc


class BaseMeasurmentResult(abc.ABC):
    def __init__(self,description):
        self.description=description

    @abc.abstractclassmethod
    def get_type(self):
        pass
