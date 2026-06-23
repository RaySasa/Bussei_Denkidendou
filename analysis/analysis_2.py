#実験1 銅の電気抵抗の温度依存性
import numpy as np
import matplotlib.pyplot as plt

#温度と抵抗のフィット
a = 100 / (149.51 - 110.64)
b = 300 - a * 110.64

#正電流の測定
rp = [110, 114, 118]
V2p = [1344, 1088, 803]
V4p = [557, 451, 332]
#オームとmV

rp = np.array(rp)
V2p = np.array(V2p)
V4p = np.array(V4p)
Tp = a * rp + b

#負電流
rm = [110, 114, 118.1124]
V2m = [1401, 1120, 816]
V4m = [556, 448, 329]

rm = np.array(rm)
V2m = - np.array(V2m)
V4m = - np.array(V4m)
Tm = a * rm + b

#熱起電力の補正
R2 = (V2p - V2m) / 2
R4 = (V4p - V4m) / 2
T = (Tp + Tm) / 2

plt.scatter(T, R2, label= "2tanshi")
plt.scatter(T, R4, label= "4tanshi")
plt.legend()
plt.show()