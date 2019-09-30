from  data_analysis.tools import touchstone
from data_analysis import measurment
import matplotlib.pyplot as plt
import sys

print(sys.path)


test_file = r"C:\Users\caspar.lucas.TRACABZ\Google Drive\Colab Notebooks\projects\RD Aisg Site Controller\33-503-01-01 evaluation\data\rf_paths\p1=j3_p2=j1_Mde=1_Dir=0_095124.s2p"


_class = measurment.Measurment_factory(measurment.MeasurmentResultType.SPRAM,"test sparam")

res = touchstone.process_touchstone_s2p(test_file,_class)


Test_RL = [[0.5e9,3e9,3e9,3.5e9],[-20,-20,-10,-10]]
Test_ISO = [[0.5e9,3e9,3e9,3.5e9],[-50,-50,-35,-35]]

res["s11"].add_test_mask("m",Test_RL,"lte","return loss 1")
res["s22"].add_test_mask("m",Test_RL,"lte","return loss 1")
res["s21"].add_test_mask("m",Test_ISO,"lte","isolation 1")
res["s12"].add_test_mask("m",Test_ISO,"lte","isolation 1")

for k,v in res.items():
    plt.plot(v.freq,v.as_db)
    f,l=v.get_mask("m")
    plt.plot(f,l,'--')


plt.show()






