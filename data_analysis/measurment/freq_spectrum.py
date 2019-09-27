from data_analysis.measurment import freq_meas


class FreqSpectrumRes(freq_meas.FreqMeasResult):

    def __init__(self, freq,data,description):
        super(FreqSpectrumRes,self).__init__( freq,data,description)

   
    def get_type(self):
        pass