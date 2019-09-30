from . import freq_meas
import numpy as np

class sparam_data_error(BaseException):
    def __init__(self, message, *args):
        self.message = message
        super(sparam_data_error, self).__init__(message, *args)



class FreqSpramRes(freq_meas.FreqMeasResult):

    def __init__(self, freq,data,sparam_format,**kwargs):

        description=kwargs.get("description",None)
        sparam_meas=kwargs.get("sparam_meas",None)

        super().__init__(freq,data,description)
        if len(freq)!=len(data):
            raise sparam_data_error("data length are not equal")
        if sparam_format == "RI":
            self.freq=freq_meas.FreqMeasResult.to_numpy(freq)
            self.data=freq_meas.FreqMeasResult.to_numpy(data)
        else:
            raise sparam_data_error("unsupported data type")

        self.sparam_meas=sparam_meas

    @property
    def as_db(self):
        db = 20.0*np.log10(np.abs(self.data))
        return db

    @property
    def phase_rads(self):
        ph = np.angle(self.data)
        return ph

    @property
    def phase_deg(self):
        ph = np.angle(self.data,True)
        return ph

