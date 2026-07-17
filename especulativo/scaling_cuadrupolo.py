# ETAPA ESPECULATIVA TCI 2.0 - calculo preliminar, no validado (2026-07-17)
# ============================================================================
# ANATOMIA DE HULSE-TAYLOR, mitad 1: verificar numericamente que una binaria
# de "cargas" acopladas a un campo sin masa de velocidad v radia con la FORMA
# de la formula del cuadrupolo de Einstein: P proporcional a q^2 d^4 W^6 / v^5.
# ----------------------------------------------------------------------------
# Metodo: campo escalar sin masa (canal generico), dos cargas iguales q en
# orbita circular de diametro d y frecuencia W. Potencia radiada por armonico m:
#   P_m = (w_m^2 / (8 pi^2 v^3)) * Integral dOmega |S_m(k n)|^2,  w_m = m W,
#   S_m(k) = q * (1/T) Int_0^T dt e^{i m W t} [e^{-i k.X(t)} + e^{+i k.X(t)}]
# (transformada de la fuente en el armonico m, |k| = w_m / v; los armonicos
# impares se cancelan por simetria de las dos cargas). Se integra numericamente
# SIN expansion multipolar y se fitean los exponentes en W, d, v.
# Esperado (regimen kd<<1, domina m=2): P ~ W^6 d^4 v^-5 (+correcciones).
# ============================================================================
import numpy as np

def P_total(W, d, v, q=1.0, Nt=600, Ndir=200, mmax=6):
    i = np.arange(Ndir)
    phig = np.pi*(3-np.sqrt(5))*i
    z = 1 - 2*(i+0.5)/Ndir
    r = np.sqrt(1-z*z)
    ndirs = np.stack([r*np.cos(phig), r*np.sin(phig), z], axis=1)
    t = np.linspace(0, 2*np.pi/W, Nt, endpoint=False)
    X = 0.5*d*np.stack([np.cos(W*t), np.sin(W*t), 0*t], axis=1)
    P = 0.0
    for m in range(2, mmax+1, 2):
        wm = m*W
        k = wm/v
        kdotX = k * (ndirs @ X.T)               # (Ndir, Nt)
        fase = np.exp(1j*m*W*t)[None, :]
        S = q * np.mean(fase*(np.exp(-1j*kdotX) + np.exp(1j*kdotX)), axis=1)
        integ = 4*np.pi*np.mean(np.abs(S)**2)   # Int dOmega |S|^2
        # flujo far-field ~ w^2 |A|^2 / v con A = S/4pi  (errata #7 corregida:
        # antes tenia v^3 en el denominador por mal conteo del flujo)
        P += wm**2/(8*np.pi**2*v) * integ
    return P

# ---- fit de exponentes (regimen kd<<1: W d / v = 0.02 tipico)
base = dict(W=1.0, d=0.02, v=1.0)
def expfit(var, vals):
    Ps = []
    for x in vals:
        kw = dict(base); kw[var] = x
        Ps.append(P_total(**kw))
    p = np.polyfit(np.log(vals), np.log(Ps), 1)[0]
    return p

for var, vals, esperado in [("W", np.array([0.5, 1.0, 2.0, 4.0]), 6),
                            ("d", np.array([0.01, 0.02, 0.04, 0.08]), 4),
                            ("v", np.array([1.0, 1.5, 2.25, 3.375]), -5)]:
    p = expfit(var, vals)
    print(f"P ~ {var}^{p:.3f}   (Einstein-forma esperada: {var}^{esperado})")

print()
print("Conclusion si los tres exponentes dan (6, 4, -5): la FORMA del cuadrupolo")
print("de Einstein es universal para binarias acopladas a un canal sin masa de")
print("dispersion lineal -- Hulse-Taylor no testea la forma sino el COEFICIENTE.")
