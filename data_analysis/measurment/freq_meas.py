from data_analysis.measurment import base_measurment
import numpy as np





class FreqMeasResult(base_measurment.BaseMeasurmentResult):

    class test_mask():
        
        def __init__(self,mask,test_criteria,description):
            self.mask=mask
            self.test_criteria=test_criteria
            self.description=description

            self.has_run=False
            self.passed=False
            self.passed_by_point=None


    def __init__(self, freq,data,description):
        super().__init__(description)
        self.freq= FreqMeasResult.to_numpy(freq)
        self.data= FreqMeasResult.to_numpy(data)
        self.test_masks={}
        pass


    @property
    def fmin(self):
        return self.freq[0]

    @property
    def fmax(self):
        return self.freq[-1]


    @staticmethod
    def to_numpy(data):
        _data=None
        if isinstance(data,list):
            types = [float,complex]
            for t in types:
                try:
                    _data=np.array(data,dtype=t)
                    break
                except:
                    pass
        elif isinstance(data,np.ndarray):
            _data=data

        return _data

    def add_test_mask(self,id,mask):
        """
        add a frequency test mask.
        id - dictionary key to use
        mask - [[....frequency points ....],[ ...limit points....]]
        """
        _mask = FreqMeasResult.to_numpy(mask)
        _f_mask=_mask[0]
        _l_mask=_mask[1]
        _mask= np.interp(self.freq, _f_mask, _l_mask, left=np.nan, right=np.nan, period=None)
        self.test_masks[id] = test_mask (_mask)


    def get_mask(self,id):
        """
        get a previously defined mask by its id
        """
        test_limit = self.test_masks.get(id,None)
        idx = np.where(np.isnan(test_limit)==False)

        f = np.take(self.freq,idx)[0]
        l = np.take(test_limit,idx)[0]
        return f,l

    def apppy_mask(self,id=None,action="lte"):
        """
        apply test mask to data
        id - test mask id
        
        """
        TEST_FN_dict={"eq":np.equal,"gte":np.greater_equal,"lte":np.less_equal,"lt":np.less,"gt":np.greater}
        test_limit = self.test_masks.get(id,None)

        test_fn = TEST_FN_dict.get(action)
        test_res = test_fn(self.data,test_limit,where=(np.isnan(test_limit)==False))

        return {}



    def get_type(self):
        pass




