# -*- coding: utf-8 -*-
"""Extraccion cruda de texto de un PDF (FlateDecode) sin dependencias."""
import re, sys, zlib

path = sys.argv[1]
data = open(path, 'rb').read()
streams = re.findall(rb'stream\r?\n(.*?)endstream', data, re.S)
out = []
for s in streams:
    try:
        d = zlib.decompress(s)
    except Exception:
        continue
    # juntar los fragmentos de texto (Tj / TJ) de cada stream
    frags = re.findall(rb'\((?:[^()\\]|\\.)*\)', d)
    if not frags:
        continue
    txt = b' '.join(frags)
    txt = re.sub(rb'\\[()]', b'', txt)
    txt = txt.replace(b'(', b'').replace(b')', b'')
    out.append(txt.decode('latin-1', 'replace'))
open(sys.argv[2], 'w', encoding='utf-8').write('\n@@PAGE@@\n'.join(out))
print(f"{len(out)} streams con texto; escrito en {sys.argv[2]}")
