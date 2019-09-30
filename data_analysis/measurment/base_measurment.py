import abc


class BaseMeasurmentResult(abc.ABC):
    def __init__(self,description):
        self.description=description

    @classmethod
    def get_type(cls):
        return cls.__name__
