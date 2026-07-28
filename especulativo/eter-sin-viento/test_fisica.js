#!/usr/bin/env node
/* Smoke test de física de las 5 simulaciones de "El éter sin viento".
   Regla de la casa: la física de toda sim se verifica en Node ANTES de publicar
   (el preview del browser no anima rAF). Este script extrae el bloque de motores
   puros del index.html —el MISMO código que corre en la página— y verifica los
   invariantes físicos que los epígrafes prometen.

   Uso:  node test_fisica.js        (sale con código 0 si todo pasa)          */

'use strict';
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const ini = html.indexOf('/*===MOTORES-INICIO===*/');
const fin = html.indexOf('/*===MOTORES-FIN===*/');
if (ini < 0 || fin < 0) { console.error('No encuentro el bloque de motores'); process.exit(1); }
const bloque = html.slice(ini, fin);
const module_ = { exports: {} };
new Function('module', bloque)(module_);
const M = module_.exports;

let pasan = 0, fallan = 0;
function test(nombre, cond, detalle) {
  if (cond) { pasan++; console.log('  PASS  ' + nombre + (detalle ? '  [' + detalle + ']' : '')); }
  else { fallan++; console.log('  FAIL  ' + nombre + (detalle ? '  [' + detalle + ']' : '')); }
}
const DT = 1 / 60, W = 760, H = 340;

/* ============ 1. EL TATUAJE — la carga viaja con el grano, jamás salta ============ */
console.log('\n[1] EL TATUAJE (superselección como juguete)');
{
  const m = M.motorTatuaje(W, H, 11);
  const nTat0 = m.granos.filter(p => p.q === 1).length;
  for (let i = 0; i < 3000; i++) {
    m.step(DT);
    if (i % 600 === 599) m.pintar(200 + i / 10 % 400, 100 + i / 20 % 200);
  }
  test('hay granos tatuados de arranque', nTat0 > 20, nTat0 + ' tatuados');
  test('el flujo mueve de verdad (desplazamiento medio > 80 px)',
    m.desplazMedio() > 80, m.desplazMedio().toFixed(0) + ' px en 50 s');
  test('se intentó pintar', m.intentos === 5, m.intentos + ' intentos');
  test('CERO tatuajes cambiados tras 50 s de flujo + 5 intentos de pintura',
    m.cambiadas() === 0, 'cambiadas = ' + m.cambiadas());
  test('sin NaN en posiciones', m.granos.every(p => isFinite(p.x) && isFinite(p.y)));
}

/* ============ 2. EL GLOBO — viento cero; anclar no fabrica viento duradero ============ */
console.log('\n[2] EL GLOBO (viento no es movimiento)');
{
  const m = M.motorGlobo(W, H, 22);
  let vMax = 0, recorrido = 0, xPrev = m.sonda.x;
  for (let i = 0; i < 1500; i++) {
    m.step(DT);
    vMax = Math.max(vMax, m.viento());
    recorrido += Math.abs(m.sonda.x - xPrev) + (m.sonda.x - xPrev > W / 2 ? -W : 0) * 0;
    xPrev = m.sonda.x;
  }
  test('modo libre: viento a bordo = 0 EXACTO durante 25 s (máx < 1e-9)',
    vMax < 1e-9, 'máx = ' + vMax.toExponential(1));
  test('…y sin embargo la sonda se movió muchísimo con el mar',
    recorrido > 200, recorrido.toFixed(0) + ' px recorridos');
  // intento de fabricar viento
  m.ancla(true);
  let pico = 0;
  for (let i = 0; i < 30; i++) { m.step(DT); pico = Math.max(pico, m.viento()); }
  for (let i = 0; i < 180; i++) m.step(DT);   // 3 s después
  const v3s = m.viento();
  test('al anclar aparece viento (pico > 5)', pico > 5, 'pico = ' + pico.toFixed(1));
  test('…pero el mar se reacomoda: a los 3 s queda < 8 % del pico',
    v3s < 0.08 * pico, (100 * v3s / pico).toFixed(1) + ' % del pico');
  const [ux, uy] = m.U(10, 10, m.t), [mx, my] = m.marLocal(10, 10);
  test('lejos de la sonda el mar sigue fluyendo igual (el remanso es local)',
    Math.hypot(mx - ux, my - uy) < 0.05 * Math.hypot(ux, uy) + 1e-9);
  m.ancla(false);
  for (let i = 0; i < 60; i++) m.step(DT);
  test('al soltar, la calma vuelve exacta', m.viento() < 1e-9,
    'viento = ' + m.viento().toExponential(1));
}

/* ============ 3. EL HOYO QUE VIAJA — acompaña sin estela ============ */
console.log('\n[3] EL HOYO QUE VIAJA (refleja, no persigue)');
{
  const m = M.motorHoyo(W, H, 33);
  for (let i = 0; i < 600; i++) m.step(DT);      // 10 s: estado estacionario móvil
  let s = 0, n = 0;
  for (let i = 0; i < 300; i++) { m.step(DT); s += m.sesgo(); n++; }
  const sesgoMovil = s / n;
  // en marcha, el único desvío es la inercia del trazador: ~v_b·τ/180 = 85·0.25/180 ≈ 0.12
  test('bola en marcha: la caída apunta a la bola salvo la inercia del trazador (|desvío| < 0.15)',
    Math.abs(sesgoMovil) < 0.15, 'desvío = ' + sesgoMovil.toFixed(3) + ' (trazador predice ~0.12)');
  m.pausada = true; m.bola.vx = 0; m.bola.vy = 0;
  for (let i = 0; i < 60; i++) m.step(DT);       // 1 s: el trazador olvida (τ = 0.25 s)
  let s2 = 0;
  for (let i = 0; i < 120; i++) { m.step(DT); s2 += m.sesgo(); }
  test('bola frenada: en 1 s la caída apunta EXACTO a ella — nada que perseguir (|desvío| < 0.04)',
    Math.abs(s2 / 120) < 0.04, 'desvío = ' + (s2 / 120).toFixed(3));
  test('sin NaN', m.granos.every(p => isFinite(p.x) && isFinite(p.y) && isFinite(p.vx)));
}

/* ============ 4. EL AMONTONAMIENTO — aritmética del panqueque ============ */
console.log('\n[4] EL AMONTONAMIENTO (γ y la forma)');
{
  const P = M.motorPanqueque;
  test('γ(0.8) = 5/3', Math.abs(P.gamma(0.8) - 5 / 3) < 1e-12);
  let ok1 = true, ok2 = true;
  for (const v of [0.3, 0.6, 0.8, 0.95]) {
    if (Math.abs(P.ejeLargo(100, v) - 100 * Math.sqrt(1 - v * v)) > 1e-9) ok1 = false;
    if (Math.abs(P.ejeAncho(100, v) - 100 * Math.pow(1 - v * v, -0.25)) > 1e-9) ok2 = false;
  }
  test('eje largo = R·√(1−β²) — se CONTRAE ÷γ a lo largo de la marcha', ok1);
  test('eje ancho = R·(1−β²)^(−1/4) — se INFLA a lo ancho (panqueque)', ok2);
  test('a v=0 los niveles son círculos perfectos',
    Math.abs(P.radioNivel(100, 0, 0.7) - 100) < 1e-12);
  let mono = true, prevL = 1e9, prevA = 0;
  for (let v = 0; v <= 0.951; v += 0.05) {
    const L = P.ejeLargo(100, v), A = P.ejeAncho(100, v);
    if (L > prevL + 1e-12 || A < prevA - 1e-12) mono = false;
    prevL = L; prevA = A;
  }
  test('monotonía: más rápido ⇒ más panqueque, siempre', mono);
}

/* ============ 5. EL REMOLINO — 1/r³ eterno vs viscoso que acumula ============ */
console.log('\n[5] EL REMOLINO (dulce de leche fantasma vs viscoso)');
{
  const m = M.motorRemolino(W, H, 55);
  m.K = 0.5;
  const C = m.OM * m.K * Math.pow(m.R, 3);
  let peor = 0;
  for (const p of m.fant) peor = Math.max(peor, Math.abs(m.wFant(p.d) * Math.pow(p.d, 3) - C) / C);
  test('fantasma: ω·r³ = const EXACTA en todos los granos (perfil 1/r³)',
    peor < 1e-12, 'error rel máx = ' + peor.toExponential(1));
  const antes = m.fant.map(p => m.wFant(p.d));
  for (let i = 0; i < 1800; i++) m.step(DT);     // 30 s
  let drift = 0;
  m.fant.forEach((p, i) => drift = Math.max(drift, Math.abs(m.wFant(p.d) - antes[i])));
  test('fantasma: 30 s después el remolino es EL MISMO — cero acumulación',
    drift < 1e-15, 'drift máx = ' + drift.toExponential(1));
  let monoV = true;
  for (const d of [45, 70, 100, 140]) {
    let prev = -1;
    for (let t = 1; t <= 60; t += 2) {
      const w = m.wVisc(d, t);
      if (w < prev - 1e-12) monoV = false;
      prev = w;
    }
  }
  test('viscoso: acumula MONÓTONO en toda capa (rumbo a co-rotación rígida)', monoV);
  test('viscoso: la capa íntima ya casi co-rota a los 60 s (>95 % de Ω)',
    m.wVisc(45, 60) / m.OM > 0.95, (100 * m.wVisc(45, 60) / m.OM).toFixed(1) + ' %');
  test('viscoso: la capa lejana viene más atrás (gradiente temporal real)',
    m.wVisc(150, 60) < m.wVisc(45, 60));
  test('correa real 10⁻⁹: el remolino fantasma es una milmillonésima de Ω',
    (function () { m.K = 1e-9; return m.wFant(m.R) / m.OM <= 1e-9 + 1e-24; })(),
    'ω(R)/Ω = ' + (m.wFant(m.R) / m.OM).toExponential(1));
}

/* ============ 6. WIRING DEL RENDER — DOM simulado, sin browser ============ */
console.log('\n[6] WIRING DEL RENDER (DOM simulado + frames a mano)');
{
  const si = html.indexOf('<script>'), sf = html.lastIndexOf('</' + 'script>');
  const codigo = html.slice(si + 8, sf);
  const ctxStub = new Proxy({}, { get: () => () => {}, set: () => true });
  function canvasStub() {
    return {
      _cw: 0, clientHeight: 340, width: 0, height: 0,
      get clientWidth() { return this._cw; },
      getContext: () => ctxStub,
      addEventListener: () => {}, setPointerCapture: () => {},
      getBoundingClientRect: () => ({ left: 0, top: 0 })
    };
  }
  function elemStub(valor) {
    return {
      onclick: null, oninput: null, textContent: '', value: valor || '0',
      classList: { add: () => {}, remove: () => {}, toggle: () => {}, contains: () => false },
      addEventListener: () => {}, dispatchEvent: () => {}
    };
  }
  const canvases = {}, elems = {};
  for (const id of ['c-tatuaje', 'c-globo', 'c-hoyo', 'c-panqueque', 'c-remolino'])
    canvases[id] = canvasStub();
  const doc = {
    hidden: false,
    body: { classList: { add: () => {}, toggle: () => {}, contains: () => false } },
    getElementById(id) {
      if (canvases[id]) return canvases[id];
      if (!elems[id]) elems[id] = elemStub(id === 'br-k' ? '0.97' : '0');
      return elems[id];
    },
    addEventListener: () => {}
  };
  const cola = []; let tSim = 0;
  const raf = cb => { cola.push(cb); };
  const frames = n => { for (let i = 0; i < n; i++) { const q = cola.splice(0); q.forEach(cb => cb(tSim += 16.7)); } };
  let err = null;
  try {
    new Function('window', 'document', 'localStorage', 'requestAnimationFrame',
      'performance', 'getComputedStyle', 'module', codigo)(
      { devicePixelRatio: 1 }, doc,
      { getItem: () => null, setItem: () => {} }, raf,
      { now: () => tSim }, () => ({ getPropertyValue: () => '#123456' }),
      undefined);
    frames(10);                       // fase 1: todos los canvas con ancho 0 (pestaña oculta)
  } catch (e) { err = e; }
  test('el script corre entero sin DOM real y aguanta 10 frames con canvas de ancho 0',
    !err && Object.values(canvases).every(c => c.width === 0), err ? String(err) : 'sin dibujo, sin crash');
  try {
    for (const c of Object.values(canvases)) c._cw = 718;   // fase 2: el pane aparece
    frames(3);
  } catch (e) { err = err || e; }
  test('al aparecer el ancho, TODAS las sims se rearman solas (width 0 → 718)',
    !err && Object.values(canvases).every(c => c.width === 718),
    Object.values(canvases).map(c => c.width).join('/'));
  try { frames(120); } catch (e) { err = err || e; }        // fase 3: 2 s de animación
  test('120 frames de animación sin excepciones', !err, err ? String(err) : 'ok');
  test('los medidores en vivo se actualizan (tatuaje / hoyo / panqueque / remolino)',
    /intentos de pintar/.test(elems['bt-cont'].textContent) &&
    /desvío de la caída/.test(elems['bh-med'].textContent) &&
    /γ = /.test(elems['bp-med'].textContent) &&
    /correa/.test(elems['br-med'].textContent),
    [elems['bt-cont'].textContent, elems['bh-med'].textContent,
     elems['bp-med'].textContent, elems['br-med'].textContent].join(' | ').slice(0, 120));
}

console.log('\n================================');
console.log(pasan + ' PASS · ' + fallan + ' FAIL');
if (fallan) { console.log('LA FÍSICA NO ESTÁ LISTA — no publicar.'); process.exit(1); }
console.log('Física de las 5 sims verificada. Se puede publicar.');
