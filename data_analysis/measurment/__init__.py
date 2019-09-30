
from . import freq_sparam 
from . import freq_spectrum
from enum import Enum


class MeasurmentResultType(Enum):
    SIMPLE = 1
    TIME = 2
    SPRAM = 3
    SPECTRUM = 4

reistered_meas_type_dict={
    MeasurmentResultType.SPRAM:freq_sparam.FreqSpramRes,
    MeasurmentResultType.SPECTRUM:freq_spectrum.FreqSpectrumRes
}

def Measurment_factory(meas_type,description):
    _class = reistered_meas_type_dict.get(meas_type,None)
    return _class
