"use strict";
// Every number shown here comes from the JSON endpoints; this file only formats and lays them out.
// Model output is never parsed as HTML: it reaches the page as <img src> of a server SVG or as text.

const $ = (s, r = document) => r.querySelector(s);
const SVGNS = "http://www.w3.org/2000/svg";

function applyAttrs(e, attrs) {
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "class") e.setAttribute("class", v);
    else if (k.startsWith("on")) e.addEventListener(k.slice(2), v);
    else if (k === "style") e.style.cssText = v;
    else e.setAttribute(k, v === true ? "" : v);
  }
}
function addKids(e, kids) {
  for (const c of kids.flat(Infinity)) if (c !== null && c !== undefined && c !== false) e.append(c.nodeType ? c : document.createTextNode(String(c)));
}
function el(tag, attrs, ...kids) { const e = document.createElement(tag); applyAttrs(e, attrs); addKids(e, kids); return e; }
function sv(tag, attrs, ...kids) { const e = document.createElementNS(SVGNS, tag); applyAttrs(e, attrs); addKids(e, kids); return e; }
const setKids = (node, ...kids) => node.replaceChildren(...kids.flat(Infinity).filter(k => k !== null && k !== undefined && k !== false));
const qs = o => new URLSearchParams(Object.entries(o).filter(([, v]) => v !== null && v !== undefined && v !== "")).toString();
async function jget(u) {
  const r = await fetch(u);
  if (!r.ok) throw new Error("request failed " + r.status);
  return r.json();
}
async function jpost(u, b) {
  const r = await fetch(u, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(b) });
  return { code: r.status, data: await r.json() };
}
const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;

// ---- formats
const APP = { models: [], names: {}, kits: [], conds: [], ftypes: [] };
const pct = x => Math.round(100 * x) + "%";
const pctN = (x, passes, n) => pct(x) + " (" + passes + "/" + n + ")";
const score2 = x => x.toFixed(2);
const px1 = x => x.toFixed(1) + " px";
const deg1 = x => x.toFixed(1) + "°";
const ANGLE = ["orient", "upright", "angle"];
const unitOf = kind => ANGLE.includes(kind) ? "°" : " px";
const errText = (v, kind) => v === null || v === undefined ? "n/a" : ANGLE.includes(kind) ? deg1(v) : px1(v);
const tolText = (v, kind) => v + unitOf(kind);
const thousands = n => Number(n).toLocaleString("en-US");
const secs = n => Math.round(n) + " s";
const usd = c => c === null || c === undefined ? "n/a" : "$" + c.toFixed(2);
const modelName = m => APP.names[m] || m;
const modelShort = m => { const n = modelName(m); return n.startsWith("Claude ") ? n.split(" ")[1] : n.replace(/^Gemini /, ""); };
const condInfo = id => APP.conds.find(c => c.id === id) || { id, letter: id, short: SETTING[id] || id };
const condLetter = id => condInfo(id).letter || id;
const condLabel = id => condInfo(id).short;
const kitName = k => k.charAt(0).toUpperCase() + k.slice(1).replace(/_/g, " ");
const mcol = m => "var(--s" + (APP.models.indexOf(m) + 1) + ")";
const fcol = t => "var(--f" + (APP.ftypes.indexOf(t) + 1) + ")";
const cssVar = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const mhex = m => cssVar("--s" + (APP.models.indexOf(m) + 1));
const fhex = t => cssVar("--f" + (APP.ftypes.indexOf(t) + 1));
const asOf = iso => iso ? "Data as of " + iso.slice(0, 16).replace("T", " ") + " UTC" : "";

function inkFor(hex) {
  const m = /^#([0-9a-f]{6})$/i.exec(hex);
  if (!m) return "#0b0b0b";
  const ch = [0, 2, 4].map(i => { const v = parseInt(m[1].substr(i, 2), 16) / 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
  const lum = 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2];
  return (lum + 0.05) / 0.05 > 1.05 / (lum + 0.05) ? "#0b0b0b" : "#ffffff";
}

// ---- small components
let uid = 0;
function icon(ok) {
  return sv("svg", { class: "ic", width: "14", height: "14", viewBox: "0 0 16 16", "aria-hidden": "true" },
    sv("path", { d: ok ? "M3 8.5l3.2 3.2L13 5" : "M4 4l8 8M12 4l-8 8", fill: "none", stroke: ok ? "var(--good)" : "var(--bad)", "stroke-width": "2.4", "stroke-linecap": "round", "stroke-linejoin": "round" }));
}
function partialIcon() {
  return sv("svg", { class: "ic", width: "14", height: "14", viewBox: "0 0 16 16", "aria-hidden": "true" },
    sv("circle", { cx: "8", cy: "8", r: "5.6", fill: "none", stroke: "var(--text-2)", "stroke-width": "1.8" }),
    sv("path", { d: "M8 2.4a5.6 5.6 0 0 1 0 11.2z", fill: "var(--text-2)" }));
}
const badge = ok => el("span", { class: "badge " + (ok ? "pass" : "fail") }, icon(ok), ok ? "PASS" : "FAIL");
const dot = col => el("i", { class: "dot", style: "background:" + col });
const empty = text => el("div", { class: "empty", role: "status" }, text);
const skeleton = (h = 220) => el("div", { class: "skel", style: "height:" + h + "px", "aria-hidden": "true" });
const chip = (text, title) => el("span", { class: "chip", title: title || null }, text);
function mname(m, withId = true) {
  return el("span", { class: "mname", title: m }, modelName(m), withId ? el("small", {}, m) : null);
}
function labelled(text, control) {
  const id = control.id || (control.id = "f" + ++uid);
  return el("div", {}, el("label", { for: id }, text), control);
}
function select(items, value) {
  const s = el("select", {}, items.map(([v, t]) => el("option", { value: v }, t)));
  if (value !== undefined && value !== null) s.value = value;
  return s;
}
function head(title, sub, tools) {
  return el("div", { class: "card-head" }, el("div", {}, el("h2", {}, title), sub ? el("p", { class: "sub" }, sub) : null), tools ? el("div", { class: "tools" }, tools) : null);
}
const headText = h => typeof h === "string" ? h : h.t;
function dataTable(heads, rows, opts) {
  const o = typeof opts === "string" ? { cls: opts } : opts || {};
  return el("div", { class: "tablewrap" }, el("table", { class: o.cls || "" },
    o.widths ? el("colgroup", {}, o.widths.map(w => el("col", { style: "width:" + w }))) : null,
    el("thead", {}, el("tr", {}, heads.map(h => el("th", { scope: "col" }, headText(h), typeof h === "string" ? null : h.n)))),
    el("tbody", {}, rows.map(r => el("tr", {}, r.map((c, i) => el(i ? "td" : "th", { scope: i ? null : "row", "data-label": i ? headText(heads[i]) : null }, c)))))));
}

// A drawing on a paper-tone frame; the cream canvas is inset, with a loading note until the image arrives.
function pic(src, alt, kind) {
  const img = el("img", { src, alt, decoding: "async" });
  const box = el("div", { class: "pic " + (kind || "wide") }, img);
  img.addEventListener("load", () => box.classList.add("loaded"));
  img.addEventListener("error", () => { box.classList.add("fail"); box.append("Image unavailable"); });
  return el("div", { class: "frame" }, box);
}
const trialParams = t => ({ cond: t.cond, kit: t.kit, model: t.model, trial: t.trial, src: t.src === "live" ? "live" : "results", run: t.src === "live" ? t.run : null });
const trialHash = t => "#trial/" + [t.cond, t.kit, t.model, t.trial].map(encodeURIComponent).join("/") + (t.src === "live" ? "?" + qs({ src: "live", run: t.run }) : "");
const annSrc = (t, o = {}) => "/svg/annotated?" + qs({ ...trialParams(t), i: o.index === null || o.index === undefined ? null : o.index, all: o.all ? 1 : null, fit: o.fit ? 1 : null, zoom: o.zoom === false ? 0 : null });
const closeupSrc = (t, index) => annSrc(t, { index });
const CLOSEUP_ALT = "Close-up of the failed check: red ring where the part landed, green ring where it belongs, arrow between them and the error";

// ---- glossary: an info icon with a popover, reachable by keyboard
const GLOSS = {
  settings: "Joints not listed, parts unnamed: the parts are labelled p01, p02 and so on. Joints not listed: the parts are named. Joints listed: we name every connection to make.",
  "built correctly": "A build is built correctly only when every check passes and the reply has no problems.",
  score: "The share of a build's checks that pass, from 0.00 to 1.00. A build is built correctly only when every check passes.",
  tolerance: "How far a feature may sit from its correct spot and still count: pixels for positions, degrees for angles.",
  "pass^k": "Kits where every build by that model was built correctly, out of the kits it attempted.",
};
function gl(key) {
  const id = "gl" + ++uid;
  const pop = el("span", { class: "pop", role: "tooltip", id, hidden: true }, GLOSS[key]);
  const btn = el("button", { class: "info", type: "button", "aria-label": "What is " + key + "?", "aria-describedby": id, "aria-expanded": "false" }, "i");
  const box = el("span", { class: "gl" }, btn, pop);
  const show = () => {
    pop.hidden = false; btn.setAttribute("aria-expanded", "true"); pop.style.left = "0px";
    const r = pop.getBoundingClientRect();
    if (r.right > innerWidth - 12) pop.style.left = (innerWidth - 12 - r.right) + "px";
  };
  const hide = () => { pop.hidden = true; btn.setAttribute("aria-expanded", "false"); };
  btn.addEventListener("click", e => { e.preventDefault(); e.stopPropagation(); show(); });
  btn.addEventListener("focus", show); btn.addEventListener("blur", hide);
  box.addEventListener("mouseenter", show); box.addEventListener("mouseleave", () => { if (document.activeElement !== btn) hide(); });
  box.addEventListener("keydown", e => { if (e.key === "Escape") hide(); });
  return box;
}

// ---- theme
const THEME_CHANGE = [];
function themeIcon() {
  return sv("svg", { width: "24", height: "24", viewBox: "0 0 24 24", "aria-hidden": "true", fill: "none", stroke: "currentColor", "stroke-width": "2" },
    sv("circle", { cx: "12", cy: "12", r: "9" }), sv("path", { d: "M12 3a9 9 0 0 0 0 18z", fill: "currentColor" }));
}
function setupTheme() {
  const btns = [...document.querySelectorAll(".theme-btn")];
  const system = matchMedia("(prefers-color-scheme: dark)");
  let saved = null;
  try { saved = localStorage.getItem("theme"); } catch (e) { saved = null; }
  const stored = saved === "dark" || saved === "light";
  let mode = stored ? saved : (system.matches ? "dark" : "light");
  const apply = (persist) => {
    document.documentElement.setAttribute("data-theme", mode);
    const label = mode === "dark" ? "Switch to light mode" : "Switch to dark mode";
    for (const btn of btns) {
      setKids(btn, themeIcon(), btn.classList.contains("ghost") ? label : null);
      btn.setAttribute("aria-label", label); btn.title = label; btn.setAttribute("aria-pressed", String(mode === "dark"));
    }
    if (persist) { try { localStorage.setItem("theme", mode); } catch (e) { /* storage may be blocked */ } }
  };
  let userChose = false;
  for (const btn of btns) btn.addEventListener("click", () => { mode = mode === "dark" ? "light" : "dark"; userChose = true; apply(true); rebuildCharts(); });
  apply(false);
  system.addEventListener("change", e => { if (!stored && !userChose) { mode = e.matches ? "dark" : "light"; apply(false); rebuildCharts(); } });
}

// ---- charts (Apache ECharts, colours read from the CSS tokens so light and dark both follow the theme)
const CHARTS = new Set();
const NARROW = 700;  // below this a chart uses short labels and fewer ticks
const tipEl = (title, rows) => el("div", { class: "etip" }, el("div", { class: "tt" }, title),
  rows.map(r => el("div", { class: "tr" }, r.c ? el("i", { class: "sw", style: "background:" + r.c }) : null, el("b", {}, r.v), el("span", { class: "l" }, r.l))));

function baseOption() {
  return {
    animation: !reduced(), animationDuration: 600, animationDurationUpdate: 400, animationEasing: "cubicOut",
    textStyle: { fontFamily: "'Roboto Condensed','Arial Narrow',system-ui,sans-serif", color: cssVar("--text-2") },
    aria: { enabled: true },
    tooltip: { confine: true, backgroundColor: cssVar("--surface"), borderColor: cssVar("--border"), borderWidth: 1, padding: 10,
      textStyle: { color: cssVar("--text"), fontSize: 12 }, extraCssText: "box-shadow:" + cssVar("--shadow-2") + ";border-radius:8px" },
    legend: { show: false },
  };
}
const axisStyle = () => ({
  axisLine: { lineStyle: { color: cssVar("--axis") } }, axisTick: { show: false },
  axisLabel: { color: cssVar("--text-2"), fontSize: 13 }, splitLine: { lineStyle: { color: cssVar("--grid") } },
});
const valueAxisName = text => ({ name: text, nameLocation: "middle", nameGap: 30, nameTextStyle: { color: cssVar("--text-2"), fontSize: 13 } });

// A chart handle: build(narrow, width) returns the option from current tokens; draw() re-inits so the entry animation plays again.
function mountChart(node, build, onClick, height) {
  const h = { chart: null, node, build, onClick, height, narrow: false };
  h.draw = () => {
    if (h.chart) { h.chart.dispose(); h.chart = null; }
    if (!node.isConnected || !node.clientWidth) return;
    h.narrow = node.clientWidth < NARROW;
    node.style.height = h.height(h.narrow) + "px";
    h.chart = echarts.init(node, null, { renderer: "svg" });
    h.chart.setOption(h.build(h.narrow, node.clientWidth));
    if (h.onClick) h.chart.on("click", h.onClick);
  };
  h.ro = new ResizeObserver(() => {
    if (!h.chart) return;
    if ((node.clientWidth < NARROW) !== h.narrow) h.draw(); else h.chart.resize();
  });
  h.ro.observe(node);
  CHARTS.add(h);
  return h;
}
function rebuildCharts() { for (const h of CHARTS) if (h.node.isConnected) h.draw(); }
function disposeCharts() {
  for (const h of CHARTS) { h.ro.disconnect(); if (h.chart) h.chart.dispose(); }
  CHARTS.clear();
}

// The legend lives in HTML above the canvas, so it can wrap without ever covering the plot.
function legendBar(items, hidden, onToggle) {
  return el("div", { class: "legend", role: "group", "aria-label": "Legend: click an item to show or hide it" }, items.map(it =>
    el("button", { type: "button", title: it.title || null, class: "lg-btn" + (hidden.has(it.key) ? " off" : ""), "aria-pressed": String(!hidden.has(it.key)), onclick: () => onToggle(it.key) },
      el("i", { class: "sw", style: "background:" + it.color }), it.label)));
}

// A card with a title, optional controls, a chart and a table twin. emptyText() returns a message when there is nothing to draw.
function chartCard(o) {
  const body = el("div", { class: "chart", role: "img", "aria-label": o.label });
  const tableBox = el("div", { hidden: true }), emptyBox = el("div", { hidden: true }), legendBox = el("div", {});
  const wrap = el("div", { class: "chart-wrap" }, body, emptyBox);
  const hidden = new Set();
  let asTable = false, handle = null;
  const toggle = el("button", { class: o.bare ? "tbtn" : "ghost", type: "button", "aria-pressed": "false" }, "View as table");
  let seen = !o.bare;
  function drawLegend() {
    if (!o.legendItems) { setKids(legendBox, o.legend || null); return; }
    setKids(legendBox, legendBar(o.legendItems(), hidden, key => { if (hidden.has(key)) hidden.delete(key); else hidden.add(key); drawLegend(); handle.draw(); }));
  }
  function show() {
    const msg = o.emptyText();
    emptyBox.hidden = !msg; setKids(emptyBox, msg ? empty(msg) : null);
    body.hidden = !!msg || asTable;
    legendBox.hidden = !!msg || asTable;
    tableBox.hidden = !asTable || !!msg;
    if (asTable && !msg) setKids(tableBox, o.table());
    if (!msg && !asTable) {
      drawLegend();
      if (seen) handle.draw();
      else { seen = true; body.style.height = o.height(hidden, body.clientWidth < NARROW) + "px"; whenVisible(body, () => handle.draw()); }
    }
    toggle.hidden = !!msg;
  }
  toggle.addEventListener("click", () => {
    asTable = !asTable; toggle.textContent = asTable ? "View as chart" : "View as table"; toggle.setAttribute("aria-pressed", String(asTable)); show();
  });
  handle = mountChart(body, (n, w) => o.build(hidden, n, w), o.onClick, n => o.height(hidden, n));
  for (const c of o.controls || []) c.querySelector("select").addEventListener("change", () => show());
  if (o.bare) {
    const top = el("div", { class: "sec-head" }, el("div", {}, el("h2", { class: "sec-title" }, o.title), el("p", { class: "sec-intro" }, o.sub)), el("div", { class: "controls" }, o.controls || [], toggle));
    const card = el("div", { class: "hchart rv" }, o.side ? [top, el("div", { class: "fails" }, el("div", {}, wrap, tableBox), legendBox)] : [top, legendBox, wrap, tableBox]);
    queueMicrotask(() => requestAnimationFrame(() => { if (card.isConnected) show(); }));
    return card;
  }
  const card = el("section", { class: "card" }, head(o.title, o.sub, [o.controls || [], toggle]), legendBox, wrap, tableBox, o.caption ? el("p", { class: "cap" }, o.caption) : null);
  queueMicrotask(() => requestAnimationFrame(() => { if (card.isConnected) show(); }));
  return card;
}

// ---- overview charts
const tableOf = (D, cond, model) => (D.tables[cond] || []).find(t => t.model === model);

function ladderOption(D, hidden, narrow) {
  const L = D.ladder_matched, models = APP.models.filter(m => L[m]), order = D.ladder_order.filter(c => !hidden.has(c));
  const base = baseOption(), nameOf = narrow ? modelShort : modelName;
  return {
    ...base,
    grid: { left: 8, right: narrow ? 56 : 110, top: 8, bottom: 46, containLabel: true },
    tooltip: { ...base.tooltip, trigger: "item", formatter: p => {
      const d = p.data;
      return tipEl(modelName(d.model) + " · " + SETTING[d.cond], [
        { c: cssVar("--cond-" + d.cond), v: pct(d.value), l: d.passes + " of " + d.trials + " builds correct" },
        { c: null, v: String(d.kits.length), l: "kits compared: " + d.kits.map(kitName).join(", ") },
        { c: null, v: "→", l: "click to list these trials" }]);
    } },
    xAxis: { type: "value", min: 0, max: 1, interval: narrow ? 0.5 : 0.2, ...axisStyle(), ...valueAxisName("Share built correctly"), axisLabel: { color: cssVar("--text-2"), fontSize: 12, formatter: v => pct(v) } },
    yAxis: { type: "category", inverse: true, data: models.map(nameOf), ...axisStyle(), splitLine: { show: false }, axisLabel: { color: cssVar("--text"), fontSize: narrow ? 12 : 13, width: narrow ? 56 : 150, overflow: "truncate" } },
    series: order.map(c => ({
      name: SETTING[c], type: "bar", barWidth: 14, barGap: "20%", cursor: "pointer",
      itemStyle: { color: cssVar("--cond-" + c), borderRadius: [0, 4, 4, 0] },
      emphasis: { focus: "series" },
      label: { show: true, position: "right", color: cssVar("--text"), fontSize: 13, fontWeight: 400, formatter: p => narrow ? pct(p.data.value) : pct(p.data.value) + " (" + p.data.passes + " of " + p.data.trials + ")" },
      data: models.map(m => ({ value: L[m].conditions[c].rate, passes: L[m].conditions[c].passes, trials: L[m].conditions[c].trials, kits: L[m].kits, model: m, cond: c })),
    })),
  };
}
const ladderHeight = (D, hidden) => 50 + APP.models.filter(m => D.ladder_matched[m]).length * (Math.max(1, D.ladder_order.filter(c => !hidden.has(c)).length) * 14 + 24);
function ladderTable(D) {
  const L = D.ladder_matched, models = APP.models.filter(m => L[m]);
  return dataTable(["Model", "Kits compared", ...D.ladder_order.map(c => SETTING[c])], models.map(m => [mname(m), L[m].kits.map(kitName).join(", "),
    ...D.ladder_order.map(c => el("a", { href: "#results?" + qs({ cond: c, model: m }) }, pct(L[m].conditions[c].rate) + " (" + L[m].conditions[c].passes + " of " + L[m].conditions[c].trials + ")"))]), "txt stack");
}

function failureModels(D, sel) {
  const conds = sel === "all" ? APP.conds.map(c => c.id) : [sel];
  return APP.models.filter(m => conds.some(c => tableOf(D, c, m)));
}
function failureOption(D, sel, hidden, narrow, width) {
  const models = failureModels(D, sel), data = D.failures[sel] || {}, base = baseOption(), types = APP.ftypes.filter(t => !hidden.has(t));
  const total = m => types.reduce((a, t) => a + ((data[m] || {})[t] || 0), 0);
  const unit = (width - (narrow ? 70 : 160)) / Math.max(1, ...models.map(total));
  return {
    ...base,
    grid: { left: 8, right: 16, top: 8, bottom: 46, containLabel: true },
    tooltip: { ...base.tooltip, trigger: "item", formatter: p => tipEl(modelName(p.data.model), [
      { c: fhex(p.seriesName), v: String(p.value), l: failName(p.seriesName) }, { c: null, v: String(total(p.data.model)), l: "failed builds in this bar" },
      { c: null, v: "→", l: "click to see these failures" }]) },
    xAxis: { type: "value", minInterval: 1, splitNumber: narrow ? 3 : 6, ...axisStyle(), ...valueAxisName("Failed builds") },
    yAxis: { type: "category", inverse: true, data: models.map(narrow ? modelShort : modelName), ...axisStyle(), splitLine: { show: false }, axisLabel: { color: cssVar("--text"), fontSize: narrow ? 12 : 13, width: narrow ? 56 : 150, overflow: "truncate" } },
    series: types.map(t => ({
      name: t, type: "bar", stack: "fail", barWidth: 22, cursor: "pointer", emphasis: { focus: "series" },
      itemStyle: { color: fhex(t), borderColor: cssVar("--surface"), borderWidth: 1 },
      label: { show: true, color: inkFor(fhex(t)), fontSize: 12, fontWeight: 650, formatter: p => p.value * unit >= 16 ? p.value : "" },
      data: models.map(m => ({ value: (data[m] || {})[t] || 0, model: m, type: t })),
    })),
  };
}
function failureTable(D, sel) {
  const models = failureModels(D, sel), data = D.failures[sel] || {};
  return dataTable(["Model", ...APP.ftypes.map(failName), "Failed builds"], models.map(m => {
    const cs = APP.ftypes.map(t => (data[m] || {})[t] || 0);
    return [mname(m), ...cs.map((n, i) => n ? el("a", { href: "#failures?" + qs({ cond: sel === "all" ? null : sel, model: m, type: APP.ftypes[i] }) }, String(n)) : "0"), cs.reduce((a, b) => a + b, 0)];
  }), "txt stack");
}
const failureEmpty = (D, sel) => failureModels(D, sel).length && Object.keys(D.failures[sel] || {}).length ? "" : "No failed builds for this setting yet.";

// ---- replay: parts start where the kit sheet stores them and move to where the model placed them
const ease = t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const mstr = m => "matrix(" + m.join(",") + ")";
const applyM = (m, x, y) => [m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5]];
function mixMatrix(s, e, box, k) {
  const cx = (box[0] + box[2]) / 2, cy = (box[1] + box[3]) / 2;
  const ps = applyM(s, cx, cy), pe = applyM(e, cx, cy);
  const ks = Math.hypot(s[0], s[1]) + (Math.hypot(e[0], e[1]) - Math.hypot(s[0], s[1])) * k;
  const as = Math.atan2(s[1], s[0]) * 180 / Math.PI, ae = Math.atan2(e[1], e[0]) * 180 / Math.PI;
  const delta = ((ae - as + 540) % 360) - 180, a = (as + delta * k) * Math.PI / 180;
  const px = ps[0] + (pe[0] - ps[0]) * k, py = ps[1] + (pe[1] - ps[1]) * k, c = Math.cos(a) * ks, sn = Math.sin(a) * ks;
  return [c, sn, -sn, c, px - (c * cx - sn * cy), py - (sn * cx + c * cy)];
}
function partGroup(p, style, cls) {
  const g = sv("g", { class: cls, ...style });
  for (const path of p.paths) {
    const attrs = { d: path.d };
    for (const [k, v] of Object.entries(path.style || {})) if (/^[a-z-]+$/.test(k) && /^[#\w.,() -]*$/.test(String(v))) attrs[k] = v;
    g.append(sv("path", attrs));
  }
  return g;
}
function buildStage(data) {
  const [vx, vy, vw, vh] = data.view, wrap = el("div", { class: "stage" });
  const svg = sv("svg", { viewBox: vx + " " + vy + " " + vw + " " + vh, role: "img", "aria-label": "Animated assembly: parts move from the kit sheet to where the model placed them" });
  svg.append(sv("rect", { x: vx, y: vy, width: vw, height: vh, fill: "#F8F7F2" }));
  const ghosts = sv("g", {}), parts = sv("g", {}), marks = sv("g", {});
  const els = new Map();
  for (const p of data.parts) {
    const g = partGroup(p, data.part_style, "part" + (p.end ? "" : " unplaced")), t = data.failed_parts.includes(p.part);
    g.setAttribute("transform", mstr(p.start)); parts.append(g); els.set(p.part, g);
    if (t) { const gh = partGroup(p, {}, "ghost-part"); gh.setAttribute("transform", mstr(p.ref)); ghosts.append(gh); }
  }
  const r = Math.max(vw / 90, 10);
  for (const f of data.failed_points) if (f.landed) marks.append(sv("circle", { class: "mark", cx: f.landed[0], cy: f.landed[1], r }));
  svg.append(ghosts, parts, marks);
  wrap.append(svg);
  return { node: wrap, data, els, token: 0 };
}
function showEnd(st) {
  for (const p of st.data.parts) if (p.end) st.els.get(p.part).setAttribute("transform", mstr(p.end));
  st.node.classList.add("arrived");
}
function playReplay(st) {
  const token = ++st.token;
  st.node.classList.remove("arrived");
  for (const p of st.data.parts) st.els.get(p.part).setAttribute("transform", mstr(p.start));
  if (reduced()) { showEnd(st); return Promise.resolve(); }
  const t0 = performance.now(), dur = 1500;
  return new Promise(done => {
    const frame = now => {
      if (token !== st.token || !st.node.isConnected) { done(); return; }
      const k = Math.min(1, (now - t0) / dur), e = ease(k);
      for (const p of st.data.parts) if (p.end) st.els.get(p.part).setAttribute("transform", k >= 1 ? mstr(p.end) : mstr(mixMatrix(p.start, p.end, p.box, e)));
      if (k < 1) requestAnimationFrame(frame); else { st.node.classList.add("arrived"); done(); }
    };
    requestAnimationFrame(frame);
  });
}
async function loadStage(t) {
  const data = await jget("/api/replay?" + qs(trialParams(t)));
  const st = buildStage(data);
  showEnd(st);
  return st;
}

// ---- before/after slider: both images share one window, so the divider always shows the same spot
function compareSlider(modelSrc, refSrc, start = 50, labels = ["Model", "Correct"]) {
  const box = el("div", { class: "cmp", style: "--pos:" + start + "%" },
    el("img", { class: "under", src: refSrc, alt: "Correct assembly, placed on the model's base part" }), el("img", { class: "over", src: modelSrc, alt: "The model's assembly" }),
    el("div", { class: "handle" }), el("div", { class: "knob", "aria-hidden": "true" }, "↔"));
  const range = el("input", { type: "range", min: "0", max: "100", step: "1", value: String(start), "aria-label": "Slide between the model's assembly (left) and the correct assembly (right)" });
  const set = v => { box.style.setProperty("--pos", v + "%"); range.value = String(Math.round(v)); };
  const fromPointer = e => { const b = box.getBoundingClientRect(); set(Math.min(100, Math.max(0, 100 * (e.clientX - b.left) / b.width))); };
  box.addEventListener("pointerdown", e => { box.setPointerCapture(e.pointerId); fromPointer(e); });
  box.addEventListener("pointermove", e => { if (box.hasPointerCapture(e.pointerId)) fromPointer(e); });
  range.addEventListener("input", () => set(+range.value));
  return el("div", {}, el("div", { class: "cmphead" }, el("span", {}, labels[0]), el("span", {}, labels[1])), el("div", { class: "frame" }, box), range);
}

// ---- Home (overview)
const SETTING = { C: "Joints listed", A: "Joints not listed", B: "Joints not listed, parts unnamed", A_alt: "Joints not listed" };
const FAIL_NAMES = ["Part in the wrong place or turned wrong", "Almost right", "Part missing, doubled, mirrored or resized", "Hit the length limit before answering", "Answer could not be read"];
const FAIL_GLOSS = ["", "every miss small, at least one just outside the allowed margin", "", "", ""];
const failName = t => FAIL_NAMES[APP.ftypes.indexOf(t)] || t;
const NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"];
const numWord = n => NUMBER_WORDS[n] || String(n);
const cap1 = s => s.charAt(0).toUpperCase() + s.slice(1);
const lower1 = s => s.charAt(0).toLowerCase() + s.slice(1);
const isAngle = kind => ANGLE.includes(kind);
const sizeOff = (err, kind) => err === null || err === undefined ? "" : isAngle(kind) ? deg1(err) : err.toFixed(1) + " pixels";

// Runs fn once when node first scrolls into view; at once when motion is reduced or observers are missing.
const seenIO = typeof IntersectionObserver === "undefined" ? null : new IntersectionObserver(entries => {
  for (const e of entries) if (e.isIntersecting) { seenIO.unobserve(e.target); const fn = WAITING.get(e.target); WAITING.delete(e.target); if (fn && e.target.isConnected) fn(); }
}, { threshold: 0.15 });
const WAITING = new WeakMap();
function whenVisible(node, fn) {
  if (!seenIO || reduced()) { fn(); return; }
  WAITING.set(node, fn); seenIO.observe(node);
}
function reveal(root) {
  root.querySelectorAll(".rv").forEach(n => {
    n.style.setProperty("--i", String([...n.parentNode.children].filter(c => c.classList.contains("rv")).indexOf(n)));
    whenVisible(n, () => n.classList.add("in"));
  });
}

function countUp(node, to, fmt) {
  node.textContent = fmt(to);
  if (reduced()) return;
  whenVisible(node, () => {
    const t0 = performance.now(), dur = 900;
    const step = now => {
      const k = Math.min(1, (now - t0) / dur);
      node.textContent = fmt(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1 && node.isConnected) requestAnimationFrame(step); else node.textContent = fmt(to);
    };
    node.textContent = fmt(0);
    requestAnimationFrame(step);
  });
}

const bold = (...kids) => el("b", {}, ...kids);

function subline(D) {
  const s = D.summary, t = D.totals, has = c => s[c].trials > 0;
  if (!t.trials) return el("p", { class: "subline" }, "No finished builds yet; results appear here as the run progresses.");
  const r = c => bold(pct(s[c].best_rate)), n = numWord(t.models), k = numWord(t.kits);
  const both = t.kit_names.includes("bike") && t.kit_names.includes("wheelbarrow");
  const wide = ["We gave " + n + " AI models the loose parts of " + k + " kits" + (both ? ", from a road bike to a wheelbarrow," : ",") + " and asked them to put each one together.",
    has("C") ? [" When we listed every joint, the best model built ", r("C"), " correctly."] : "",
    has("A") ? [has("C") ? " When we didn't, the best managed " : " The best model managed ", r("A"), "."] : "",
    has("B") ? [" With the part names hidden too, ", r("B"), "."] : ""];
  const narrow = [cap1(n) + " AI models, " + k + " kits of loose parts. Best result: ",
    [has("C") ? [r("C"), " built correctly with the joints listed"] : null, has("A") ? [r("A"), " without"] : null, has("B") ? [r("B"), " with the part names hidden too"] : null]
      .filter(Boolean).flatMap((x, i) => i ? [", ", x] : [x]), "."];
  return el("p", { class: "subline" }, el("span", { class: "wide" }, wide), el("span", { class: "phone" }, narrow));
}

function heroCaption(h) {
  const err = h.point ? h.point.err : null, kind = h.point ? h.point.kind : h.kind;
  if (isAngle(kind)) return h.short + (err === null ? " turned the wrong way" : " turned " + deg1(err) + " wrong");
  return h.short + " in the wrong place" + (err === null || err === undefined ? "" : " · " + sizeOff(err, kind) + " off");
}

// Rings and the curved arrow are drawn from numbers only, over the server's plain drawing.
function marksOverlay(h) {
  const p = h.point, svg = sv("svg", { class: "marks", viewBox: h.view.join(" "), "aria-hidden": "true" });
  if (!p) return svg;
  const [a, b, r, w] = [p.landed, p.expected, p.radius, p.stroke], d = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1;
  const u = [(b[0] - a[0]) / d, (b[1] - a[1]) / d];
  svg.append(sv("circle", { class: "mk-green", cx: b[0], cy: b[1], r, "stroke-width": w * 1.5 }), sv("circle", { class: "mk-red", cx: a[0], cy: a[1], r, "stroke-width": w * 1.5 }));
  if (d > 2.2 * r) {
    const s = [a[0] + u[0] * r * 1.15, a[1] + u[1] * r * 1.15], e = [b[0] - u[0] * r * 1.45, b[1] - u[1] * r * 1.45];
    const c = [(s[0] + e[0]) / 2 - u[1] * d * 0.22, (s[1] + e[1]) / 2 + u[0] * d * 0.22];
    const t = Math.hypot(e[0] - c[0], e[1] - c[1]) || 1, v = [(e[0] - c[0]) / t, (e[1] - c[1]) / t], hs = r * 0.55;
    const tip = [e[0] + v[0] * hs * 0.4, e[1] + v[1] * hs * 0.4], base = [e[0] - v[0] * hs * 0.6, e[1] - v[1] * hs * 0.6];
    svg.append(sv("path", { class: "mk-arrow", d: "M" + s.join(" ") + " Q" + c.join(" ") + " " + base.join(" "), pathLength: "1", "stroke-width": w * 1.3 }),
      sv("polygon", { class: "mk-head", points: [tip, [base[0] - v[1] * hs * 0.5, base[1] + v[0] * hs * 0.5], [base[0] + v[1] * hs * 0.5, base[1] - v[0] * hs * 0.5]].map(q => q.join(",")).join(" ") }));
  }
  return svg;
}

function drawing(src, alt, overlay) {
  const img = el("img", { src, alt, decoding: "async" });
  const box = el("div", { class: "draw" }, img, overlay || null);
  whenVisible(box, () => box.classList.add("on"));
  return box;
}

function heroSection(D) {
  const h = D.hero, intro = [el("p", { class: "eyebrow" }, "An AI benchmark"), el("h1", {}, "Can AI put a machine together from its parts?"), subline(D), el("p", { class: "byline" }, "by Naveen Kumar Chilakala")];
  if (!h) return el("section", { class: "hero", "aria-label": "Headline result" }, intro, el("div", { style: "margin-top:32px" }, empty("No failed builds yet; the most striking failure appears here once builds finish.")));
  const t = { src: "results", cond: h.cond, kit: h.kit, model: h.model, trial: h.trial };
  const figs = el("div", { class: "hero-figs", "data-show": "model" },
    el("figure", { class: "fig-model" },
      drawing("/svg/trial?" + qs({ ...trialParams(t), plain: 1, fit: 1, paper: 0 }), "The model's assembly, with a red ring where the part landed and a green ring where it belongs", marksOverlay(h)),
      el("figcaption", { class: "cap-hero", title: h.check }, heroCaption(h), el("small", {}, modelName(h.model) + ", " + lower1(SETTING[h.cond])))),
    el("figure", { class: "fig-correct" },
      drawing("/svg/reference?" + qs({ ...trialParams(t), plain: 1, paper: 0 }), "A correct assembly of the same kit"),
      el("figcaption", { class: "cap-hero" }, "A correct assembly")));
  const btn = el("button", { type: "button", class: "ghost showbtn", "aria-pressed": "false" }, "Show a correct assembly");
  btn.addEventListener("click", () => {
    const on = figs.dataset.show === "model";
    figs.dataset.show = on ? "correct" : "model"; btn.setAttribute("aria-pressed", String(on));
    btn.textContent = on ? "Show the AI's assembly" : "Show a correct assembly";
  });
  return el("section", { class: "hero", "aria-label": "Headline result and most striking failure" }, intro, figs, btn);
}

function stepsSection(D) {
  const s = D.story, intro = "Every build follows the same four steps.";
  const head = el("div", { class: "sec-head" }, el("div", {}, el("h2", { class: "sec-title", id: "how-h" }, "How the test works"), el("p", { class: "sec-intro" }, intro)));
  if (!s) return el("section", { class: "sec", "aria-labelledby": "how-h" }, head, empty("The walkthrough appears once a model has failed a kit."));
  const t = { src: "results", cond: s.cond, kit: s.kit, model: s.model, trial: s.trial };
  const fail = s.failed > 0;
  const bars = D.ladder_order.map(c => {
    const cell = ((D.grids[c] || {})[s.kit] || {})[s.model];
    const rate = cell && cell.trials ? cell.passes / cell.trials : null;
    return el("div", { class: "mb" }, el("span", {}, SETTING[c]), el("div", { class: "bar" }, el("i", { style: "width:" + (rate === null ? 0 : Math.round(100 * rate)) + "%;--c:var(--cond-" + c + ")" })),
      bold(rate === null ? "–" : pct(rate)));
  });
  const step = (n, title, art, text, extra) => el("div", { class: "step rv" }, el("div", { class: "art" }, art), el("h3", {}, el("i", {}, n + "."), title), el("p", {}, text), extra || null);
  return el("section", { class: "sec", "aria-labelledby": "how-h" }, head, el("div", { class: "steps" },
    step(1, "The parts", drawing("/svg/kit?" + qs({ kit: s.kit, cond: s.cond, plain: 1 }), "The loose parts of one kit, with no marks showing where they connect"), "Every part arrives on its own, most of them turned away from how they sit in the finished machine."),
    step(2, "The request", el("div", { class: "bubble" }, "Assemble a working " + s.noun + "."),
      s.cond === "C" ? "The request lists every connection to make, but gives no positions or angles."
        : "The request also explains how the build will be checked, but gives no positions and no list of which part joins which."),
    step(3, "The AI's assembly", drawing("/svg/trial?" + qs({ ...trialParams(t), plain: 1, fit: 1, paper: 0 }), "One model's assembly of the same kit"), "The model replies with one picture that places each part: moved and turned, never redrawn."),
    el("div", { class: "step rv" }, el("div", { class: "art" }, el("div", { class: "verdict" }, el("div", { class: "stamp " + (fail ? "fail" : "pass"), role: "img", "aria-label": fail ? "Failed" : "Passed" }, fail ? "FAIL" : "PASS"),
      el("div", { class: "minibars" }, el("div", { class: "t" }, "This model's builds of the " + s.noun + ", by setting:"), bars))),
      el("h3", {}, el("i", {}, "4."), "The check"), el("p", {}, "Code checks every joint, the way each part faces, and that nothing is missing or mirrored. " + s.failed + " of " + s.checks + " checks failed."))));
}

function statCard(D, c, i) {
  const s = D.summary[c], wide = i === D.ladder_order.length - 1 && i % 2 === 0;
  const link = (...kids) => el("a", { class: "stat rv" + (wide ? " wide" : ""), href: "#results?" + qs({ cond: c }), "aria-label": SETTING[c] + ": open results" }, ...kids);
  if (!s.trials) return link(el("div", { class: "lbl" }, SETTING[c]), el("div", { class: "num", style: "color:var(--muted)" }, "–"), el("div", { class: "note" }, "No finished builds yet"));
  const tied = (D.tables[c] || []).filter(t => Math.abs(t.pass_rate - s.best_rate) < 1e-9);
  const best = tableOf(D, c, s.best_model), num = el("div", { class: "num" });
  countUp(num, s.best_rate, v => Math.round(100 * v) + "%");
  const names = tied.map(t => modelName(t.model));
  const note = tied.length > 1 ? "Top score, shared by " + names.slice(0, -1).join(", ") + " and " + names[names.length - 1]
    : "Best model: " + modelName(s.best_model) + ", " + best.passes + " of " + best.trials + " builds correct";
  return link(el("div", { class: "lbl" }, SETTING[c]), num, el("div", { class: "track", role: "img", "aria-label": SETTING[c] + ": " + pct(s.best_rate) + " built correctly" }, el("i", { style: "width:" + pct(s.best_rate) })), el("div", { class: "note" }, note));
}

function ladderSection(D) {
  const order = D.ladder_order;
  return chartCard({ bare: true, title: "Each model in all three settings",
    sub: "Share of builds assembled correctly. Each model is shown only on kits it built the same number of times in all three settings, so these figures can differ from the cards above.",
    label: "Grouped bar chart: share of builds assembled correctly per model in each of the three settings",
    legendItems: () => order.map(c => ({ key: c, label: SETTING[c], color: cssVar("--cond-" + c) })),
    build: (hidden, narrow) => ladderOption(D, hidden, narrow), height: hidden => ladderHeight(D, hidden),
    onClick: p => { if (p.data) location.hash = "#results?" + qs({ cond: p.data.cond, model: p.data.model }); },
    emptyText: () => APP.models.some(m => D.ladder_matched[m]) ? "" : "No model has built the same kit in all three settings yet.", table: () => ladderTable(D) });
}

function failSection(D) {
  const sel = select([["all", "All settings"], ...D.ladder_order.map(c => [c, SETTING[c]])], "all");
  return chartCard({ bare: true, side: true, title: "How models fail", sub: "Every failed build, grouped by its main problem. Use the selector to see one setting.", controls: [labelled("Setting", sel)],
    label: "Stacked bar chart: failed builds per model by main problem",
    legendItems: () => APP.ftypes.map(t => ({ key: t, label: failName(t), title: FAIL_GLOSS[APP.ftypes.indexOf(t)], color: fhex(t) })),
    build: (hidden, narrow, w) => failureOption(D, sel.value, hidden, narrow, w), height: () => 56 + failureModels(D, sel.value).length * 36,
    onClick: p => { if (p.data && p.data.type) location.hash = "#failures?" + qs({ cond: sel.value === "all" ? null : sel.value, model: p.data.model, type: p.data.type }); },
    emptyText: () => failureEmpty(D, sel.value), table: () => failureTable(D, sel.value) });
}

function mistakeCard(m, i) {
  const ex = m.example, t = { src: "results", cond: ex.cond, kit: ex.kit, model: ex.model, trial: ex.trial };
  const angle = isAngle(m.kind), unit = m.median_err === null ? "" : angle ? deg1(m.median_err) : m.median_err.toFixed(1) + " pixels";
  return el("a", { class: "mc rv", href: trialHash(t), title: m.check },
    el("div", { class: "win" }, el("img", { src: closeupSrc(t, ex.index), alt: CLOSEUP_ALT, decoding: "async", loading: "lazy" })),
    el("p", {}, bold(m.short + (angle ? " turned the wrong way" : " in the wrong place")), " · in " + m.trials + " builds" + (unit ? " · typically " + unit + " off; worst case shown" : "")));
}

function mistakesSection(D) {
  return el("section", { class: "sec", "aria-labelledby": "mist-h" },
    el("div", { class: "sec-head" }, el("div", {}, el("h2", { class: "sec-title", id: "mist-h" }, "The mistakes models make most"),
      el("p", { class: "sec-intro" }, "Counted across all settings. Each picture shows the worst case. Red: where the model put the part. Green: where it belongs.")),
      el("a", { class: "seelink", href: "#failures" }, "See every failed build →")),
    D.top_mistakes.length ? el("div", { class: "mgrid3" }, D.top_mistakes.slice(0, 3).map(mistakeCard)) : empty("No failed builds yet."));
}

async function viewOverview(main) {
  const D = await jget("/api/overview"), t = D.totals;
  main.classList.add("home");
  setKids(main, heroSection(D), stepsSection(D),
    el("section", { class: "sec", "aria-labelledby": "res-h" }, el("h2", { class: "sr", id: "res-h" }, "Results"),
      el("div", { class: "results" }, el("div", { class: "stats" }, D.ladder_order.map((c, i) => statCard(D, c, i))), ladderSection(D))),
    el("section", { class: "sec" }, failSection(D)), mistakesSection(D),
    el("footer", { class: "foot" }, "Every build is checked by code: each joint, the way each part faces, and that nothing is missing · " + thousands(t.trials) + " builds · " + t.kits + " kits · " + t.models + " AI models · Built by Naveen Kumar Chilakala"));
  reveal(main);
}


// ---- Failures gallery
const PAGE_SIZE = 24;
const NO_PICTURE = ["No marked picture", "The grader found this check failed, but there is no spot to mark (for example a part that is missing or turned wrong)."];
const noPicture = () => el("div", { class: "frame" }, el("div", { class: "noans" }, icon(false), el("b", {}, NO_PICTURE[0]), NO_PICTURE[1]));
const noAnswerText = f => "The model spent its whole length allowance" + (f.token_limit ? " (" + thousands(f.token_limit) + " tokens)" : "") + " thinking and never gave an answer. This counts as a failed build.";
const NO_ANSWER = { "unusable output": ["Output could not be used", "The reply held no assembly that could be graded."] };
function failCard(f) {
  const t = { src: "results", cond: f.cond, kit: f.kit, model: f.model, trial: f.trial };
  const none = !f.checks, unmarked = !none && !f.closeup, msg = f.failure_type === "no answer before token cap" ? ["No answer", noAnswerText(f)] : NO_ANSWER[f.failure_type] || ["No answer", "The reply could not be graded."];
  return el("a", { class: "fcard", href: trialHash(t) },
    el("figure", { class: "fig" }, none ? el("div", { class: "frame" }, el("div", { class: "noans" }, icon(false), el("b", {}, msg[0]), msg[1])) : unmarked ? noPicture() : pic(closeupSrc(t, null), CLOSEUP_ALT, "cu")),
    el("div", { class: "fmeta" },
      el("div", { class: "ft" }, kitName(f.kit), " · ", dot(mcol(f.model)), el("span", { title: f.model }, modelName(f.model))),
      el("div", { class: "fs" }, badge(false), el("span", {}, condLabel(f.cond)), el("span", {}, "build " + f.trial), el("span", {}, "score " + score2(f.score)),
        el("span", {}, none ? "No answer, counts as failed" : f.failed_checks + " of " + f.checks + " checks failed")),
      el("div", { class: "ftype" }, el("i", { class: "sw", style: "background:" + fcol(f.failure_type) }), failName(f.failure_type))));
}
async function viewFailures(main, params) {
  const D = await jget("/api/failures");
  const all = D.failures, opt = (label, items) => [["", "All " + label], ...items];
  const sel = {
    cond: select(opt("settings", D.conditions.map(c => [c.id, condLabel(c.id)])), params.get("cond") || ""),
    model: select(opt("models", D.models.map(m => [m, modelName(m)])), params.get("model") || ""),
    kit: select(opt("kits", D.kits.map(k => [k, kitName(k)])), params.get("kit") || ""),
    type: select(opt("kinds of failure", D.failure_types.map(t => [t, failName(t)])), params.get("type") || "") };
  const gallery = el("div", { class: "fgrid" }), more = el("button", { class: "ghost", type: "button" }, "Show more"), count = el("p", { class: "count", role: "status" });
  let shown = PAGE_SIZE;
  function draw() {
    const rows = all.filter(f => (!sel.cond.value || f.cond === sel.cond.value) && (!sel.model.value || f.model === sel.model.value)
      && (!sel.kit.value || f.kit === sel.kit.value) && (!sel.type.value || f.failure_type === sel.type.value));
    count.textContent = "Showing " + Math.min(shown, rows.length) + " of " + rows.length + " failed builds" + (rows.length < all.length ? " matching the filters (" + all.length + " in total)" : "") + ", newest first";
    setKids(gallery, rows.length ? rows.slice(0, shown).map(failCard) : empty(all.length ? "No failed builds match these filters." : "No failed builds yet."));
    more.hidden = rows.length <= shown;
  }
  more.addEventListener("click", () => { shown += PAGE_SIZE; draw(); });
  for (const s of Object.values(sel)) s.addEventListener("change", () => {
    shown = PAGE_SIZE; draw();
    const q = qs({ cond: sel.cond.value, model: sel.model.value, kit: sel.kit.value, type: sel.type.value });
    history.replaceState(null, "", "#failures" + (q ? "?" + q : ""));
  });
  setKids(main, el("h1", {}, "Failures"), el("p", { class: "lede" }, "Every failed build as a close-up of its first failed check. Click one for the whole build."),
    el("div", { class: "filters" }, labelled("Setting", sel.cond), labelled("Model", sel.model), labelled("Kit", sel.kit), labelled("Kind of failure", sel.type)), count,
    gallery, el("p", { style: "text-align:center;margin-top:24px" }, more));
  draw();
}

// ---- Trial view
function errCell(c) {
  if (c.err === null || c.err === undefined) return el("td", { class: "errcell", "data-label": "Error against tolerance" }, el("div", { class: "v" }, "n/a"), el("div", { class: "t" }, (c.why || "part missing or invalid") + " · tolerance " + tolText(c.tol, c.kind)));
  const scale = Math.max(c.err, c.tol * 3);
  return el("td", { class: "errcell", "data-label": "Error against tolerance" }, el("div", { class: "v" }, errText(c.err, c.kind)),
    el("span", { class: "ebar", role: "img", "aria-label": "error " + errText(c.err, c.kind) + " against tolerance " + tolText(c.tol, c.kind) }, el("i", { style: "width:" + (100 * c.err / scale) + "%" }), el("b", { style: "left:" + (100 * c.tol / scale) + "%" })),
    el("div", { class: "t" }, "tolerance " + tolText(c.tol, c.kind)));
}
async function viewTrial(main, params, seg) {
  const [cond, kit, model, trial] = seg.slice(1).map(decodeURIComponent);
  const t = { src: params.get("src") === "live" ? "live" : "results", run: params.get("run"), cond, kit, model, trial: +trial };
  const back = el("a", { class: "back", href: prevHash || "#failures" }, "← Back");
  let d;
  try { d = await jget("/api/trial?" + qs(trialParams(t))); } catch (e) {
    if (!String(e.message).endsWith("404")) throw e;
    d = { error: "not found" };
  }
  const title = kitName(kit) + " · " + modelName(model);
  if (d.error || d.status !== "ok") {
    setKids(main, back, el("h1", {}, title), empty(d.status && d.status !== "ok" ? "API error, excluded from every number: " + (d.error || "") : "This build is not in the current results."));
    return;
  }
  const failed = d.failed.length ? el("div", { class: "tablewrap" }, el("table", { class: "txt stack checks fixed" },
    el("colgroup", {}, ["34%", "26%", "40%"].map(w => el("col", { style: "width:" + w }))),
    el("thead", {}, el("tr", {}, ["Failed check", "Error against tolerance", "Close-up"].map(h => el("th", { scope: "col" }, h)))),
    el("tbody", {}, d.failed.map(c => el("tr", {},
      el("td", {}, el("span", { class: "lg", style: "align-items:flex-start" }, icon(false), c.text)), errCell(c),
      el("td", { class: "cucell" }, c.closeup ? pic(closeupSrc(t, c.index), CLOSEUP_ALT, "cu") : noPicture())))))) : el("p", { class: "muted" }, "No failed checks.");
  const stageBox = el("div", {}, skeleton(260));
  const replayBtn = el("button", { class: "btn", type: "button" }, "Replay assembly");
  let st = null, busy = false;
  replayBtn.addEventListener("click", async () => {
    if (busy || !st) return;
    busy = true; replayBtn.disabled = true; await playReplay(st); busy = false; replayBtn.disabled = false; replayBtn.textContent = "Replay again";
  });
  const inTok = d.input_tokens, tokens = inTok ? thousands(d.output_tokens + inTok) + " tokens (" + thousands(inTok) + " in · " + thousands(d.output_tokens) + " out)" : thousands(d.output_tokens) + " output tokens";
  setKids(main, back, el("h1", {}, title),
    el("div", { class: "chiprow" }, badge(d.pass), chip("score " + score2(d.score)),
      d.failure_type ? el("span", { class: "chip" }, el("i", { class: "sw", style: "background:" + fcol(d.failure_type) }), failName(d.failure_type)) : null,
      chip(condLabel(cond), condInfo(cond).name), chip("build " + t.trial), chip(tokens), chip(secs(d.seconds)), chip(d.failed.length + " of " + d.n_checks + " checks failed")),
    t.src === "results" ? el("p", { class: "sub triallinks", style: "margin-top:8px" }, el("a", { href: "/transcript?" + buildQ(t), target: "_blank", rel: "noopener" }, "Transcript"), " · ", el("a", { href: "/raw?" + buildQ(t), target: "_blank", rel: "noopener" }, "Raw reply")) : null,
    d.issues.length ? el("p", { class: "sub", style: "margin-top:8px" }, el("b", {}, "Issues: "), d.issues.join("; ")) : null,
    el("section", { class: "card" }, head("Model against the correct assembly", "Drag the divider or use the slider. The correct assembly sits on the model's base part, so matching parts line up."),
      compareSlider("/svg/trial?" + qs({ ...trialParams(t), plain: 1, fit: 1 }), "/svg/reference?" + qs({ ...trialParams(t), plain: 1, fit: 1 }))),
    el("section", { class: "card" }, head("Replay", "Parts start where the kit stores them and move to where the model placed them.", replayBtn),
      el("div", { class: "frame" }, stageBox), d.pass ? null : el("div", { class: "replay-bar" }, el("span", {}, el("i", { class: "key-ring", style: "border-color:var(--bad)" }), "failed joint"), el("span", {}, el("i", { class: "key-ring", style: "border-color:var(--good)" }), "where the part belongs (ghost)"))),
    el("section", { class: "card" }, head("Failed checks", "Each close-up shows a red ring where the part landed, a green ring where it belongs and the error in between."), failed),
    el("details", {}, el("summary", {}, "Raw reply (text only)"), el("pre", {}, d.output || "(empty reply)")));
  try { st = await loadStage(t); setKids(stageBox, st.node); } catch (e) { setKids(stageBox, empty("Replay is not available for this build.")); replayBtn.disabled = true; }
}

// ---- Results
const costOf = m => usd(m.cost_usd);
const STAT_HEADS = () => ["Model", "Builds", { t: "Built correctly", n: gl("built correctly") }, "Share built correctly", { t: "Kits built correctly every time", n: gl("pass^k") }, { t: "Average score", n: gl("score") }, "Average output tokens", "Average time", "Cost"];
function statsTable(models) {
  if (!models.length) return empty("No finished builds yet.");
  return dataTable(STAT_HEADS(), models.map(m => [el("span", { class: "lg" }, dot(mcol(m.model)), mname(m.model)), m.trials, m.passes, pctN(m.pass_rate, m.passes, m.trials), m.passk + "/" + m.kits,
    score2(m.mean_score), thousands(Math.round(m.mean_output_tokens)), secs(m.mean_seconds), costOf(m)]), { cls: "stack fixed", widths: ["20%", "7%", "10%", "11%", "15%", "9%", "12%", "8%", "8%"] });
}
const buildQ = i => qs({ cond: i.cond, kit: i.kit, model: i.model, trial: i.trial });
function buildsTable(items) {
  if (!items.length) return empty("No builds match these filters.");
  const link = (href, t) => el("a", { href, target: "_blank", rel: "noopener" }, t);
  const two = (main, small) => el("span", {}, main, small ? el("small", { class: "s2" }, small) : null);
  const ok = i => i.status === "ok";
  return dataTable(["Setting", "Kit", "Model", "Result", "Kind of failure", "Time", "Cost", "Links"], items.map(i => [condLabel(i.cond),
    two(kitName(i.kit), "build " + i.trial), mname(i.model, false),
    ok(i) ? el("span", {}, badge(i.pass), el("small", { class: "s2" }, "score " + score2(i.score))) : el("span", { class: "muted" }, "API error (excluded)"),
    i.failure_type ? failName(i.failure_type) : "–",
    two(i.seconds ? secs(i.seconds) : "–", i.tokens === null || i.tokens === undefined ? null : thousands(i.tokens) + " tokens"),
    two(i.cost_usd === null || i.cost_usd === undefined ? "–" : "$" + i.cost_usd.toFixed(3), i.route || "Claude API"),
    el("span", { class: "links" }, ok(i) ? el("a", { href: trialHash(i) }, "Open") : null, link("/raw?" + buildQ(i), "Raw reply"), link("/transcript?" + buildQ(i), "Transcript"))]),
    { cls: "txt stack builds fixed", widths: ["15%", "11%", "11%", "12%", "17%", "11%", "10%", "13%"] });
}
function cellView(cell) {
  if (!cell.trials) return "API error";
  const ic = cell.passes === cell.trials ? icon(true) : cell.passes === 0 ? icon(false) : partialIcon();
  return el("span", { class: "cellv" }, ic, cell.passes + "/" + cell.trials);
}
function conditionBlock(c, f, src, run) {
  const kits = Object.keys(c.grid).filter(k => !f.kit || k === f.kit);
  const models = c.models.filter(m => !f.model || m.model === f.model);
  const gridModels = APP.models.filter(m => !f.model || m === f.model);
  const colW = (78 / gridModels.length) + "%";
  const grid = el("div", { class: "tablewrap" }, el("table", { class: "grid fixed" },
    el("colgroup", {}, el("col", { style: "width:22%" }), gridModels.map(() => el("col", { style: "width:" + colW }))),
    el("thead", {}, el("tr", {}, el("th", {}, "Kit"), gridModels.map(m => el("th", { title: modelName(m) }, modelShort(m))))),
    el("tbody", {}, kits.map(k => el("tr", {}, el("th", { scope: "row" }, kitName(k)), gridModels.map(m => {
      const cell = c.grid[k][m];
      if (!cell) return el("td", { class: "muted" }, "–");
      const go = () => { location.hash = "#results?" + qs({ cond: c.condition, kit: k, model: m, src: src === "live" ? "live" : null, run: src === "live" ? run : null }); };
      return el("td", { class: "cell", tabindex: "0", role: "button", "aria-label": kitName(k) + ", " + modelName(m) + ": list builds", onclick: go, onkeydown: e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); } } }, cellView(cell));
    }))))));
  const key = el("div", { class: "keyline" }, el("span", {}, icon(true), "all built correctly"), el("span", {}, partialIcon(), "some built correctly"), el("span", {}, icon(false), "none built correctly"), el("span", {}, "– not run"));
  const out = [el("h3", { style: "margin-top:0" }, condLabel(c.condition)), statsTable(models),
    el("p", { class: "sub", style: "margin:16px 0 8px" }, "Kit by model, builds built correctly out of builds. Click a cell to list its builds."), grid, key];
  const errs = c.api_errors.filter(e => (!f.kit || e.kit === f.kit) && (!f.model || e.model === f.model));
  if (errs.length) out.push(el("p", { class: "sub", style: "margin-top:12px" }, "API errors (excluded from every number): ", errs.map(e => kitName(e.kit) + " / " + modelName(e.model) + " t" + e.trial).join(", ")));
  return el("section", { class: "card" }, out);
}
function listTrials(conds, f, src, run) {
  const items = [];
  for (const c of conds) for (const k of Object.keys(c.grid)) for (const [m, cell] of Object.entries(c.grid[k]))
    if ((!f.kit || k === f.kit) && (!f.model || m === f.model)) for (const t of cell.list) items.push({ ...t, cond: c.condition, kit: k, model: m, src, run });
  return items;
}
async function viewResults(main, params) {
  const d = await jget("/api/results");
  const f = { cond: params.get("cond") || "", model: params.get("model") || "", kit: params.get("kit") || "" };
  const sel = { cond: select([["", "All settings"], ...APP.conds.map(c => [c.id, condLabel(c.id)])], f.cond),
    model: select([["", "All models"], ...APP.models.map(m => [m, modelName(m)])], f.model), kit: select([["", "All kits"], ...APP.kits.map(k => [k, kitName(k)])], f.kit) };
  const body = el("div", {});
  const live = params.get("src") === "live" ? params.get("run") : null;
  function draw() {
    f.cond = sel.cond.value; f.model = sel.model.value; f.kit = sel.kit.value;
    const q = qs({ ...f, src: live ? "live" : null, run: live });
    history.replaceState(null, "", "#results" + (q ? "?" + q : ""));
    const conds = d.conditions.filter(c => !f.cond || c.condition === f.cond);
    const nodes = [];
    if (!d.conditions.length) nodes.push(empty("No results yet."));
    else if (!conds.length) nodes.push(empty("No finished builds for this setting yet."));
    else nodes.push(conds.map(c => conditionBlock(c, f, "results", "")));
    if (conds.length) nodes.push(el("section", { class: "card" }, head("Every build", "Every build in the submitted run. Raw reply is the provider's response exactly as returned; the transcript adds the prompt and the model's thinking."),
      buildsTable(listTrials(conds, f, "results", ""))));
    nodes.push(el("h2", { style: "margin-top:40px" }, "Live runs (this machine)"));
    if (!d.live.length) nodes.push(el("p", { class: "muted", style: "margin-top:8px" }, "No live runs yet."));
    for (const r of d.live) nodes.push(el("h3", {}, "Run " + r.run), r.conditions.filter(c => !f.cond || c.condition === f.cond).map(c => conditionBlock(c, f, "live", r.run)));
    setKids(body, nodes);
  }
  for (const s of Object.values(sel)) s.addEventListener("change", draw);
  setKids(main, el("h1", {}, "Results"), el("p", { class: "lede" }, "Submitted results, hardest setting first, then the same tables for live runs on this machine."),
    d.as_of ? el("p", { class: "asof", style: "margin-top:-12px" }, asOf(d.as_of)) : null,
    el("div", { class: "filters" }, labelled("Setting", sel.cond), labelled("Model", sel.model), labelled("Kit", sel.kit)), body);
  draw();
}

// ---- Kits
// Picture | SVG code panel; the code is fetched on first use and shown as text only.
function svgPanel(title, picture, field, href, base, kit, cond) {
  const picBtn = el("button", { type: "button", class: "ghost", "aria-pressed": "true" }, "Picture");
  const codeBtn = el("button", { type: "button", class: "ghost", "aria-pressed": "false" }, "SVG code");
  const code = el("pre", { class: "svgcode", tabindex: "0", "aria-label": title + ", SVG code" }, "Loading...");
  const copy = el("button", { type: "button", class: "ghost" }, "Copy SVG");
  const tools = el("div", { class: "svgtools" }, copy, el("a", { class: "ghost", href, download: base + ".svg" }, "Download .svg"), el("span", { class: "muted", role: "status" }));
  const note = tools.lastChild, code_box = el("div", { class: "svgcodebox", hidden: true }, tools, code);
  const view = el("div", { class: "svgview" }, picture);
  let loaded = false;
  const show = isCode => {
    picBtn.setAttribute("aria-pressed", String(!isCode)); codeBtn.setAttribute("aria-pressed", String(isCode));
    view.hidden = isCode; code_box.hidden = !isCode;
    if (isCode && !loaded) { loaded = true; jget("/api/kitsvg?" + qs({ kit, cond })).then(r => { code.textContent = r[field]; }).catch(() => { loaded = false; code.textContent = "Could not load the SVG."; }); }
  };
  picBtn.addEventListener("click", () => show(false)); codeBtn.addEventListener("click", () => show(true));
  copy.addEventListener("click", async () => {
    let ok = false;
    try { await navigator.clipboard.writeText(code.textContent); ok = true; } catch (e) { /* fall back to selection */ }
    if (!ok) { const r = document.createRange(); r.selectNodeContents(code); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); }
    note.textContent = ok ? "Copied" : "Selected, press Ctrl+C or Cmd+C to copy";
    setTimeout(() => { note.textContent = ""; }, 2500);
  });
  return el("figure", { class: "fig svgpanel" }, el("div", { class: "svghead" }, el("b", {}, title), el("div", { class: "svgtoggle", role: "group", "aria-label": title + " view" }, picBtn, codeBtn)), view, code_box);
}
async function viewKits(main) {
  const d = await jget("/api/kits");
  const sel = select(APP.conds.map(c => [c.id, condLabel(c.id)]));
  const out = el("div", {});
  setKids(main, el("h1", {}, "Kits"), el("p", { class: "lede" }, "The " + (NUMBER_WORDS[d.kits.length] || String(d.kits.length)) + " objects, their parts, and the exact request each setting sends."), labelled("Setting for part ids, kit sheet and request", sel), out);
  function draw() {
    const cond = sel.value, nodes = [];
    for (const k of d.kits) {
      const pre = el("pre", {}, "Loading...");
      const det = el("details", {}, el("summary", {}, "Request"), pre);
      det.addEventListener("toggle", () => { if (det.open && !pre.dataset.done) { pre.dataset.done = "1"; jget("/api/prompt?" + qs({ kit: k.kit, cond })).then(p => { pre.textContent = p.prompt || p.error; }).catch(() => { pre.textContent = "Could not load the prompt."; }); } });
      nodes.push(el("section", { class: "card" }, el("h2", {}, kitName(k.kit)),
        el("p", { class: "sub" }, k.noun.charAt(0).toUpperCase() + k.noun.slice(1) + (k.view ? ", " + k.view : "")),
        el("p", { class: "kmeta" }, "Canvas " + k.canvas.join(" × ") + " px"),
        el("div", { class: "kgrid" },
          svgPanel("Parts as given to the model", pic("/svg/kit?" + qs({ kit: k.kit, cond, plain: 1 }), "The loose parts of " + kitName(k.kit) + " as given to the model", "wide"), "parts_svg", "/svg/kitparts?" + qs({ kit: k.kit, cond }), k.kit + "-parts-" + cond, k.kit, cond),
          svgPanel("Correct assembly", pic("/svg/solution?" + qs({ kit: k.kit, cond }), "Correct assembly of " + kitName(k.kit), "wide"), "solution_svg", "/svg/solution?" + qs({ kit: k.kit, cond }), k.kit + "-assembly-" + cond, k.kit, cond)),
        el("p", {}, el("b", {}, "Parts: "), k.parts[cond].join(", ")), det));
    }
    setKids(out, ...nodes);
  }
  sel.addEventListener("change", draw); draw();
}

// ---- Method
const SETTING_LABELS = { provider: "Provider", route: "Route", max_tokens: "Max output tokens", max_output_tokens: "Max output tokens", thinking: "Thinking", output_config: "Effort", thinking_level: "Thinking level" };
function settingText(k, v) {
  if (k === "provider") return v === "anthropic" ? "Claude (Anthropic)" : v === "gemini" ? "Google Gemini" : String(v);
  if (k === "route") return v === "vertex" ? "Google Vertex AI" : v === "claude-api" ? "Claude API" : String(v);
  if (typeof v === "number") return thousands(v);
  if (k === "thinking" && v && v.type) return String(v.type);
  if (k === "output_config" && v && v.effort) return String(v.effort);
  return typeof v === "object" ? JSON.stringify(v) : String(v);
}
function settingsView(s) {
  return el("div", {}, el("div", {}, Object.entries(s).map(([k, v]) => (SETTING_LABELS[k] || k.replace(/_/g, " ")) + ": " + settingText(k, v)).join(" · ")),
    el("details", { style: "margin:8px 0 0" }, el("summary", {}, "Exact request"), el("pre", {}, JSON.stringify(s, null, 2))));
}
async function viewMethod(main) {
  const d = await jget("/api/method");
  const kitSel = select(d.kits.map(k => [k, kitName(k)]));
  const promptBox = c => {
    const pre = el("pre", {}, "Loading..."), det = el("details", {}, el("summary", {}, "Exact request for this setting"), pre);
    const load = () => { pre.textContent = "Loading..."; jget("/api/prompt?" + qs({ kit: kitSel.value, cond: c })).then(p => { pre.textContent = p.prompt || p.error; }).catch(() => { pre.textContent = "Could not load the prompt."; }); };
    det.addEventListener("toggle", () => { if (det.open) load(); });
    kitSel.addEventListener("change", () => { if (det.open) load(); });
    return det;
  };
  const roles = { B: "The parts are unlabelled and no joints are listed. The hardest setting.", A: "The parts are named but no joints are listed: the model has to know how this object goes together.",
    C: "Every connection is spelled out, so a correct build shows the model can place parts when told how.", A_alt: "The same as the setting without joints, with reworded instructions, to check that results do not hinge on wording." };
  const ran = new Set(d.kits_run || []);
  setKids(main,
    el("h1", {}, "Method"), el("p", { class: "lede" }, "Each setting uses one fixed request (template " + d.template_version + "). The model replies with a single SVG, and code checks where every part lands."),
    el("section", { class: "card" }, head("Settings", "Hardest first. The more help, the easier the build.", labelled("Kit for the requests", kitSel)),
      d.conditions.map(c => el("div", { style: "margin-top:16px" }, el("b", {}, condLabel(c.id)), el("p", { class: "muted" }, (roles[c.id] || "")), promptBox(c.id)))),
    el("section", { class: "card" }, head("What is checked", el("span", {}, "Each check yields an error that must stay within its tolerance ", gl("tolerance"), ". The score ", gl("score"), " is the share of checks that pass; a build is built correctly only if all of them pass and the reply is clean.")),
      dataTable(["Check", "What it requires"], d.check_kinds.map(k => [el("span", { title: k.kind }, k.name), k.text]), { cls: "txt", widths: ["22%", "78%"] })),
    el("section", { class: "card" }, head("Tolerances", "Position and orientation tolerances are stated in every request that does not list the joints; the base part must also stay upright."),
      dataTable(["Kit", "Position", "Orientation", "Base part upright"], d.kits.map(k => [el("span", {}, kitName(k), ran.has(k) ? null : el("span", { class: "muted" }, " (not yet run)")),
        d.tolerances[k].position_px + " px", d.orient_tol + "°", d.tolerances[k].upright_deg + "°"]), { cls: "txt", widths: ["34%", "22%", "22%", "22%"] })),
    el("section", { class: "card" }, head("Models and settings", "The exact request settings, stored with every result."),
      dataTable(["Model", "Settings"], d.models.map(m => [el("span", { class: "lg" }, dot(mcol(m.model)), mname(m.model)), settingsView(m.settings)]), { cls: "txt", widths: ["30%", "70%"] })),
    el("section", { class: "card" }, head("What is left out"), el("p", { class: "muted", style: "margin-top:4px" },
      "Provider errors such as timeouts, rate limits and server failures are retried, and if they still fail the build is marked as an API error. It is excluded from every number and never counted as a model failure.")));
}

// ---- Run live
let pollTimer = null;
const EMPTY_LIVE = "No live runs yet. Choose kits and models, then Plan to see the cost and build count.";
function checklist(id, label, items) {
  const boxes = items.map(([v, t]) => el("label", {}, el("input", { type: "checkbox", value: v, checked: true }), t));
  const setAll = on => boxes.forEach(b => { b.firstChild.checked = on; });
  return el("fieldset", { id }, el("div", { class: "legrow" }, el("legend", {}, label),
    el("div", { class: "minilinks" }, el("button", { class: "ghost", type: "button", onclick: () => setAll(true) }, "All"), el("button", { class: "ghost", type: "button", onclick: () => setAll(false) }, "None"))),
    el("div", { class: "checklist" }, boxes));
}
const picked = id => [...$("#" + id).querySelectorAll("input:checked")].map(i => i.value);
async function viewRun(main) {
  const o = await jget("/api/options");
  const vertex = o.route === "vertex", gemini = o.models.some(m => m.startsWith("gemini"));
  const form = () => ({ condition: $("#cond").value, kits: picked("kits"), models: picked("models"), trials: +$("#trials").value, workers: +$("#workers").value });
  setKids(main, el("h1", {}, "Run it yourself"), el("p", { class: "lede" }, "Run a small batch against the models from this machine. Results go to a separate folder and never mix with the submitted ones."),
    el("section", { class: "card run-live" },
      el("p", { class: "muted", style: "margin-bottom:20px" }, vertex ? "Claude runs through Google Vertex AI with this machine's Google credentials, so no key is needed. Nothing is written to disk." : "Keys stay in this server's memory for the run only, are never written to disk and are not shown again."),
      el("div", { class: "form" },
        vertex ? null : el("div", {}, el("label", { for: "akey" }, "Anthropic API key"), el("input", { id: "akey", type: "password", autocomplete: "off" })),
        gemini ? el("div", {}, el("label", { for: "gkey" }, "Gemini API key"), el("input", { id: "gkey", type: "password", autocomplete: "off" })) : null,
        el("div", {}, el("label", { for: "cond" }, "Setting"), el("select", { id: "cond" }, o.condition_info.map(c => el("option", { value: c.id }, condLabel(c.id))))),
        checklist("kits", "Kits", o.kits.map(k => [k, kitName(k)])),
        checklist("models", "Models", o.models.map(m => [m, modelName(m)])),
        el("div", { class: "cols2" },
          el("div", {}, el("label", { for: "trials" }, "Builds per kit and model (1-5)"), el("input", { id: "trials", type: "number", min: "1", max: "5", value: "1" })),
          el("div", {}, el("label", { for: "workers" }, "Workers (1-12)"), el("input", { id: "workers", type: "number", min: "1", max: "12", value: "6" }))),
        el("div", { class: "btnrow" }, el("button", { class: "ghost", type: "button", onclick: plan }, "Plan"), el("button", { class: "btn", id: "runbtn", type: "button", onclick: run }, "Run")))),
    el("section", { class: "card run-live" }, head("Status", "The plan, then progress of the live run."), el("div", { id: "plan", class: "muted", role: "status" }), el("div", { id: "live" }, empty(EMPTY_LIVE))));
  async function plan() {
    const r = await jpost("/api/plan", form());
    $("#plan").textContent = r.code === 200 ? r.data.trials + " builds, " + r.data.estimate : r.data.error;
  }
  async function run() {
    const body = { ...form(), anthropic_key: $("#akey") ? $("#akey").value : "", gemini_key: $("#gkey") ? $("#gkey").value : "" };
    for (const id of ["#akey", "#gkey"]) if ($(id)) $(id).value = "";
    const r = await jpost("/api/run", body);
    if (r.code !== 200) { $("#plan").textContent = r.data.error; return; }
    $("#plan").textContent = "Started run " + r.data.run + " (" + r.data.total + " builds)";
    poll(); pollTimer = setInterval(poll, 2000);
  }
  poll(); pollTimer = setInterval(poll, 2000);
}
async function poll() {
  const host = $("#live"); if (!host) return;
  const s = await jget("/api/status");
  if (s.state === "idle") { setKids(host, empty(EMPTY_LIVE)); return; }
  setKids(host, el("h3", { style: "margin-top:0" }, "Run " + s.run + ": " + s.state + " (" + s.done + "/" + s.total + ")"), s.error ? el("p", {}, badge(false), " " + s.error) : null,
    dataTable(["Kit", "Model", "Build", "Result", "Score", "Time", ""], s.trials.map(t => [kitName(t.kit), modelName(t.model), t.trial,
      t.status === "ok" ? badge(t.pass) : "API error", t.score === null ? "" : score2(t.score), t.seconds === null || t.seconds === undefined ? "" : secs(t.seconds),
      t.status === "ok" ? el("a", { href: trialHash({ src: "live", run: s.run, cond: t.cond, kit: t.kit, model: t.model, trial: t.trial }) }, "view") : t.error]), "txt stack"));
  if (s.state !== "running" && pollTimer) { clearInterval(pollTimer); pollTimer = null; }
}

// ---- Router: hash routes, back/forward and deep links
const TABS = [["overview", "Overview", viewOverview], ["failures", "Failures", viewFailures], ["results", "Results", viewResults],
  ["kits", "Kits", viewKits], ["method", "Method", viewMethod], ["run", "Run it yourself", viewRun]];
let prevHash = "", currentHash = "", renderToken = 0;
function parseHash() {
  const raw = location.hash.slice(1) || "overview", [path, query] = raw.split("?");
  return { seg: path.split("/"), params: new URLSearchParams(query || "") };
}
function fadeTabs() {
  const nav = $("#tabs"), wrap = $("#navwrap");
  wrap.classList.toggle("fade-l", nav.scrollLeft > 4);
  wrap.classList.toggle("fade-r", nav.scrollLeft + nav.clientWidth < nav.scrollWidth - 4);
}
function drawTabs(active) {
  const tabs = TABS.filter(t => t[0] !== "run");
  for (const nav of [$("#tabs"), $("#sheet-tabs")]) setKids(nav, tabs.map(([id, label]) => el("a", { href: "#" + id, "aria-current": id === active ? "page" : null }, label)));
  for (const a of [$("#runlive"), $("#sheet-run")]) a.setAttribute("aria-current", active === "run" ? "page" : "false");
  const nav = $("#tabs"), a = nav.querySelector("[aria-current]");
  nav.scrollLeft = a ? Math.max(0, a.offsetLeft - (nav.clientWidth - a.offsetWidth) / 2) : 0;
  fadeTabs();
}
function setupMenu() {
  const burger = $("#burger"), sheet = $("#sheet");
  const set = open => { sheet.hidden = !open; burger.setAttribute("aria-expanded", String(open)); burger.setAttribute("aria-label", open ? "Close menu" : "Open menu"); };
  burger.addEventListener("click", () => set(sheet.hidden));
  addEventListener("hashchange", () => set(false));
  addEventListener("resize", () => { if (innerWidth > 767) set(false); });
}
async function route() {
  const { seg, params } = parseHash(), name = seg[0], token = ++renderToken, main = $("#main");
  const tab = TABS.find(t => t[0] === name), isTrial = name === "trial" && seg.length >= 5;
  const page = isTrial ? "trial" : tab ? name : "overview";
  if (currentHash && !currentHash.startsWith("#trial")) prevHash = currentHash;
  currentHash = location.hash || "#overview";
  const cameFrom = prevHash.slice(1).split(/[/?]/)[0];
  drawTabs(isTrial ? (TABS.some(t => t[0] === cameFrom) ? cameFrom : null) : page);
  disposeCharts();
  main.classList.remove("home");
  if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
  scrollTo(0, 0);
  setKids(main, skeleton(70), skeleton(260), skeleton(260));
  try {
    if (isTrial) await viewTrial(main, params, seg); else await (tab || TABS[0])[2](main, params);
    if (token !== renderToken) return;
    document.title = (isTrial ? "Build" : (tab || TABS[0])[1]) + " · Kit Assembly";
    $("#live-status").textContent = document.title;
    main.focus({ preventScroll: true });
  } catch (e) {
    if (token === renderToken) setKids(main, el("div", { class: "err", role: "alert" }, "Could not load this view. Check that the dashboard server is still running, then reload."));
  }
}
async function boot() {
  setupTheme();
  setupMenu();
  $("#tabs").addEventListener("scroll", fadeTabs, { passive: true });
  addEventListener("resize", fadeTabs);
  try {
    const o = await jget("/api/options");
    Object.assign(APP, { models: o.models, names: o.model_names, kits: o.kits, conds: o.condition_info, ftypes: o.failure_types });
  } catch (e) { setKids($("#main"), el("div", { class: "err", role: "alert" }, "Could not reach the dashboard server.")); return; }
  addEventListener("hashchange", route);
  route();
}
boot();
