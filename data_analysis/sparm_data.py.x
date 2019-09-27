import numpy as np


class sparam_data_error():
    def __init__(self, message, *args):
        self.message = message
        super(sparam_data_error, self).__init__(message, *args)




class sparm_trace():
    def __init__(self,frequency_points,sparam_points,sparam_type='RI',sparam_meas='S11'):
        if len(frequency_points)!=len(sparam_points):
            raise sparam_data_error("data length are not equal")
        if sparam_type == "RI":
            self.freq=np.array([frequency_points])
            self.data=np.array([sparam_points])
        else:
            raise sparam_data_error("unsupported data type")


    @property
    def fmin(self):
        return self.freq[0] 

    @property
    def fmax(self):
        return self.freq[-1] 

    @property
    def FREQ(self):
        return self.freq

    @property
    def as_RI(self):
        return self.data

   




class result_set():
    
    def __init__(self):
        self.results={}

    def add_result(self,data,key,desc):