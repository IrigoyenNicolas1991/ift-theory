# -*- coding: utf-8 -*-
import re
t = open('dubovsky_texto.txt', encoding='utf-8').read()
t = t.replace(' ', '')
open('dubovsky_flat.txt', 'w', encoding='utf-8').write(t)
for kw in ['gauge', 'Yukawa', 'screen', 'rotat', 'dragg', 'vector', 'm2=0', 'source']:
    idxs = [m.start() for m in re.finditer(kw, t, re.I)]
    print(kw, len(idxs), idxs[:15])
