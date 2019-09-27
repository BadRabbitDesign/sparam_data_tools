
import cmath
import math


class Results_Container():
    def __init__(self,f,d,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.f=f
        self.d=d



class touchstone_error(BaseException):
    def __init__(self, message, *args):
        self.message = message
        super(touchstone_error, self).__init__(message, *args)


def get_from_list(data_list,idx,default=None):
    return  default if idx > len(data_list) else data_list[idx]


def __RI_Handler(d_r,d_i):
    return complex(d_r, d_i)
        

def __MA_Handler(d_m,d_a):
    return cmath.rect(d_m, math.radians(d_a))
        

def __DB_Handler(d_mdb,d_a):
    return  cmath.rect(((10**(d_mdb/20.0))/1000.0),d_a)

handler_dict = {"RI":__RI_Handler,"DB":__DB_Handler,"MA":__MA_Handler}
Freq_dict = {"GHz":1e9, "MHz":1e6, "KHz":1e3, "Hz":1e0}




def process_touchstone_s2p(fn,results_class=Results_Container):

    with open(fn, 'r') as fh:
        data = fh.read()

    zs = 50.0

    in_data = False
    f = []
    s11 = []
    s21 = []
    s12 = []
    s22 = []

    for line_raw in data.splitlines():
        
        line = line_raw.strip()
        
        if (line=='' or line[0]=='!'):
            pass
        elif in_data == False:
            if '#' in line:
                in_data = True
                touch_stone_data = line.split(' ')
                freq_type = get_from_list(touch_stone_data,1) # GHz, MHz, KHz and Hz
                parm_type = get_from_list(touch_stone_data,2) # S ,Y, Z, H or G
                format_type = get_from_list(touch_stone_data,3) # RI,DB,MA
                ref_resistance = float(get_from_list(touch_stone_data,5,50))

                handler_fnct = handler_dict.get(format_type,None)
                Freq_Mult = Freq_dict.get(freq_type,1)
        else:
            try:
                d = tuple([float(v) for v in line.split('\t')])

                f.append(d[0]*Freq_Mult)
                s11.append(handler_fnct(d[1], d[2]))
                s21.append(handler_fnct(d[3], d[4]))
                s12.append(handler_fnct(d[5], d[6]))
                s22.append(handler_fnct(d[7], d[8]))

                
            except:
                raise touchstone_error("cannot convert data")
    
    s11_data = results_class(f, s11, sparam_format='RI', sparam_meas='S11',param_type=parm_type)
    s21_data = results_class(f, s21, sparam_format='RI', sparam_meas='S21',param_type=parm_type)
    s12_data = results_class(f, s12, sparam_format='RI', sparam_meas='S12',param_type=parm_type)
    s22_data = results_class(f, s22, sparam_format='RI', sparam_meas='S22',param_type=parm_type)

    return {"s11":s11_data,"s21":s21_data,"s12":s12_data,"s22":s22_data}

def sparam_load(filename):
    pass
