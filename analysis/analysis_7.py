import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#texフォントを使用
plt.rcParams["text.usetex"] = False

# 表のデータ
T_data = np.array([
    80, 90, 100, 110, 120, 130, 140, 150, 160, 170,
    180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
    280, 290, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400
], dtype=float)

R_data = np.array([
    20.1, 24.43, 28.76, 33.07, 37.34, 41.58, 45.79,
    49.98, 54.14, 58.27, 62.39, 66.48, 70.57, 74.63,
    78.69, 82.72, 86.74, 90.76, 94.76, 98.75, 102.72,
    106.68, 110.64, 114.57, 118.50, 122.41, 126.31,
    130.20, 134.07, 137.94, 141.81, 145.66, 149.51
], dtype=float)

# Ptのデバイ温度
theta_D = 240.0  # K

def bg_integrand(x):
    return x**5 * np.exp(x) / (np.expm1(x))**2

def bg_factor(T, theta=theta_D):
    integral, _ = quad(bg_integrand, 0.0, theta / T)#, epsrel=1e-10, limit=200)
    return (T / theta)**5 * integral

def R_bloch_gruneisen(T, R0, A):
    T = np.asarray(T)
    return np.array([
        R0 + A * bg_factor(t)
        for t in T
    ])

# フィッティング
initial_guess = [0.0, 300.0]  # R0, A の初期値
params, covariance = curve_fit(
    R_bloch_gruneisen,
    T_data,
    R_data,
    p0=initial_guess
)

R0_fit, A_fit = params

print(f"R0 = {R0_fit:.6f} Ω")
print(f"A  = {A_fit:.6f} Ω")

# フィット結果
R_fit = R_bloch_gruneisen(T_data, R0_fit, A_fit)

residual = R_data - R_fit
rmse = np.sqrt(np.mean(residual**2))

print(f"RMSE = {rmse:.6f} Ω")

# グラフ表示
T_plot = np.linspace(0, 50, 1000)
R_plot = R_bloch_gruneisen(T_plot, R0_fit, A_fit)


#plt.scatter(T_data, R_data, label="table data")
plt.plot(T_plot, R_plot)
plt.xlabel("temperature [K]")
plt.ylabel(r"resistance [$\Omega$]")
#plt.legend()
plt.ylim(0, None)
plt.grid()
plt.savefig("tex/resistivity_Pt(lowtemp).pdf", dpi=300, bbox_inches="tight")
plt.show()