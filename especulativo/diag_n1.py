# -*- coding: utf-8 -*-
"""Diagnóstico n=1: espectro bajo completo con radios de localización."""
import sys
sys.argv.append("--solo-ciclico")   # evitar que el import corra las 3 diagonalizaciones
import importlib.util, numpy as np
spec = importlib.util.spec_from_file_location(
    "toy", r"C:\ClaudeInMyComputer\TCI CON Fable New folder\ift-theory\especulativo\core_indice_toy.py")
toy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toy)

HB = toy.hamiltoniano(1)
E, V = np.linalg.eigh(HB)
N, L, c = toy.N, toy.L, toy.c
xs = np.arange(N) // L
ys = np.arange(N) % L
rs = np.hypot(xs - c, ys - c)
orden = np.argsort(np.abs(E))
print("n=1 — los 10 estados de menor |E| (E, r_medio, peso r<5, peso 5-10, peso >10):")
for k in orden[:10]:
    w = np.abs(V[:, k]) ** 2
    wsite = w[:2*N].reshape(N, 2).sum(1) + w[2*N:].reshape(N, 2).sum(1)
    rmed = float(np.sum(wsite * rs))
    p1 = float(wsite[rs < 5].sum()); p2 = float(wsite[(rs >= 5) & (rs < 10)].sum())
    p3 = float(wsite[rs >= 10].sum())
    print(f"  E={E[k]:+.5f}  rmed={rmed:5.2f}  [<5]={p1:.2f}  [5-10]={p2:.2f}  [>10]={p3:.2f}")
