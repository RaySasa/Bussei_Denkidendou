#課題4
import numpy as np
import matplotlib.pyplot as plt

#温度と抵抗のフィット
a = 100 / (149.51 - 110.64)
b = 300 - a * 110.64

#正電流の測定
rp = [122.438, 126.309, 130.203, 134.011, 137.932, 141.803, 145.618, 149.519]
V2p = [533.309, 388.368, 273.298, 198.282, 144.479, 106.92, 79.2825, 59.3600]
V4p = [228.084, 159.723, 112.151, 81.1604, 59.0393, 43.4440, 32.1038, 23.9170]
#オームとmV

rp = np.array(rp)
V2p = np.array(V2p)
V4p = np.array(V4p)
Tp = a * rp + b

#負電流
rm = [122.541, 126.381, 130.261, 134.055, 137.993, 141.856, 145.672, 149.574]
V2m = [556.417, 389.546, 273.675, 198.336, 0, 106.6278, 79.0841, 59.2016]
V4m = [225.777, 158.545, 111.571, 80.7859, 58.7716, 43.2428, 31.9565, 23.7950]

rm = np.array(rm)
V2m = - np.array(V2m)
V4m = - np.array(V4m)
Tm = a * rm + b

#熱起電力の補正
rho2 = (V2p - V2m) / 2 * (2.32 / (1.01 * 1)) * 1e-3
rho4 = (V4p - V4m) / 2 * (2.32 / (1.01 * 1)) * 1e-3
rho2[4] = V2p[4] * (2.32 / (1.01 * 1)) * 1e-3
T = (Tp + Tm) / 2

log2 = np.log(rho2)
log4 = np.log(rho4)
t = 1/T

#最小2乗法
(p2, cov2) = np.polyfit(t, log2, 1, cov=True)
(p4, cov4) = np.polyfit(t, log4, 1, cov=True)

#係数
a2 = p2[0]
b2 = p2[1]
a4 = p4[0]
b4 = p4[1]

#誤差
da2 = np.sqrt(cov2[0, 0])
db2 = np.sqrt(cov2[1, 1])
da4 = np.sqrt(cov4[0, 0])
db4 = np.sqrt(cov4[1, 1])

t_fit = np.array([0.0024, 0.0031])
#フィッティング
log2_fit = a2 * t_fit + b2
log4_fit = a4 * t_fit + b4

e = 1.60e-19
k2 = 2 * 1.38e-23
E2 = a2 * k2 / e
E4 = a4 * k2 / e
print(E2, E4)


plt.scatter(t, log2, label= "2tanshi")
plt.scatter(t, log4, label= "4tanshi")
plt.plot(t_fit, log2_fit, label= "2tanshi-fit")
plt.plot(t_fit, log4_fit, label= "4tanshi-fit")
#plt.xlim(290, 410)
#plt.ylim(0, 1400)
plt.legend()
plt.show()