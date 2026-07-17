import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

THETA_D = 240.0
R0 = 0.5030460252
A = 364.856010091

T_MIN = 80.0
T_MAX = 401.0

def bg_integrand(x):
    if x == 0:
        return 0.0

    exm1 = np.expm1(x)
    return x**5 * np.exp(x) / exm1**2

def bg_factor(T):
    integral, _ = quad(
        bg_integrand,
        0.0,
        THETA_D / T,
        epsrel=1e-8,
        limit=100
    )

    return (T / THETA_D)**5 * integral

def resistance_from_temperature(T):
    return R0 + A * bg_factor(T)

def temperature_from_resistance(R):
    def equation(T):
        return resistance_from_temperature(T) - R

    return brentq(equation, T_MIN, T_MAX)
