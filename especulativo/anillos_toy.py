# ETAPA ESPECULATIVA TCI 2.0 - calculo de juguete, no validado (2026-07-17)
# ============================================================================
# ANILLOS DE CUERDA HQV CON TWIST ATRAPADO - mecanismo tipo "vorton"
# ----------------------------------------------------------------------------
# E(R; k) = alpha * R * (ln(R/xi) + c0)   [tension de cuerda de vortice, con log]
#         + beta * k^2 / R                [k vueltas de twist atrapadas en el lazo]
# Pregunta: hay minimo a R finito? como escala la torre E_k?
# Coeficientes DESCONOCIDOS para D4-BN (alpha,beta ~ rigideces del condensado);
# aca alpha=beta=xi=1, c0=1: SOLO la forma del espectro es significativa.
# ============================================================================
import numpy as np

al, be, xi, c0 = 1.0, 1.0, 1.0, 1.0

def E(R, k):
    return al * R * (np.log(R / xi) + c0) + be * k**2 / R

print(f"{'k':>3} {'R_k':>8} {'E_k':>8} {'E_k/k':>7} {'E_k/E_1':>8}")
Rs = np.linspace(0.05, 60, 400000)
Ek = []
for k in range(1, 9):
    Evals = E(Rs, k)
    i = np.argmin(Evals)
    Ek.append(Evals[i])
    print(f"{k:>3} {Rs[i]:>8.3f} {Evals[i]:>8.3f} {Evals[i]/k:>7.3f} {Evals[i]/Ek[0]:>8.3f}")

# exponente efectivo de la torre: E_k ~ k^p
ks = np.arange(1, 9)
p = np.polyfit(np.log(ks), np.log(Ek), 1)[0]
print(f"\nexponente efectivo de la torre: E_k ~ k^{p:.3f}")
print("(vorton puro sin log seria p=1; Hopfion Faddeev-Niemi: p=3/4)")

# control: sin twist (k=0) el minimo debe colapsar a R->0 (Derrick gana)
E0 = E(Rs, 0)
print(f"\ncontrol k=0: minimo en R = {Rs[np.argmin(E0)]:.4f} (esperado: colapso al borde inferior)")
