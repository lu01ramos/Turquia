"""Gera o app da Turquia no mesmo modelo do app 'Roma con Amore' (lu01ramos/roma, pasta gerador/).
Uso: python3 gerar_turquia.py <pasta do gerador de Roma> <pasta de saída>
"""
import json, sys, os, shutil, hashlib, html, re
from urllib.parse import quote_plus
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

roma, out = sys.argv[1], sys.argv[2]   # roma = raiz do repositório de Roma
ANO = {"12": 2026, "1": 2027}

def e(s): return html.escape(str(s or ""), quote=True)
def gimg(q): return "https://www.google.com/search?tbm=isch&q=" + quote_plus(q)
def ext(url, inner, cls=""): return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener">{inner}</a>'
def go(dest, inner, cls=""): return f'<a class="{cls}" href="#{e(dest)}">{inner}</a>'
def slug(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:40]
def first_sentence(t):
    m = re.match(r"(.+?[.;:])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) < 170 else s[:160].rsplit(" ", 1)[0] + "…"

if os.path.isdir(out):
    for n in os.listdir(out):
        if n == ".git": continue
        p = os.path.join(out, n); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
for d_ in ("fonts", "icons"): os.makedirs(os.path.join(out, d_), exist_ok=True)
for f in os.listdir(os.path.join(roma, "docs", "fonts")):
    shutil.copy(os.path.join(roma, "docs", "fonts", f), os.path.join(out, "fonts", f))

PAGES = []
def page(pid, body, title, cls=""):
    PAGES.append(f'<section class="pg {cls}" id="p-{e(pid)}" data-title="{e(title)}">{body}</section>')

def simple_head(kick, title, sub=None):
    s = f'<div class="kick">{e(kick)}</div><h2 class="h">{e(title)}</h2>'
    if sub: s += f'<p class="muted small">{e(sub)}</p>'
    return s + "<hr>"

# ------------------------------------------------------------- início
rows = []
for d in DAYS:
    rows.append(go(d["id"], f'<span class="num">{e(d["date"].split("/")[0])}</span>'
                 f'<span class="txt"><span class="kick muted">Dia {d["n"]} · {e(d["wd"])} · {e(d["date"])}</span>'
                 f'<span class="tt">{e(d["title"])}</span></span><span class="chev">›</span>', "dayrow"))
datas = {}
for d in DAYS:
    dd, mm = d["date"].split("/")
    datas[d["id"]] = f"{ANO[mm]}-{int(mm):02d}-{int(dd):02d}"
home = f'''
<div class="cover">
  <div class="kick gold">Guia de viagem</div>
  <div class="orn"></div>
  <h1 class="roma">Turquia</h1>
  <div class="amore">Istambul e o Egeu</div>
  <div class="orn"></div>
  <div class="sub">28 de dezembro a 4 de janeiro</div>
  <div class="grp">2026 · 2027 · 6 pessoas</div>
</div>
<a id="hoje" class="btn gold big" href="#" hidden></a>
<div class="wrap">
  <div class="kick">Turquia</div>
  <h2 class="h">Sumário</h2>
  <p class="muted small">Toque em um dia para abrir a programação.</p>
  <nav class="days">{"".join(rows)}</nav>
  <div class="btn3">{go("checklist", "Antes de ir", "btn")}{go("reservas", "Reservas", "btn gold")}{go("dicas", "Dicas", "btn line")}</div>
  <p id="instalar" class="tip" hidden></p>
</div>
<script>window.DATAS = {json.dumps(datas)};</script>'''
page("inicio", home, "Turquia", "home")

# ------------------------------------------------------------- antes de ir (lista para marcar)
def chk_items(lst, pref):
    o = []
    for dt, txt, did in lst:
        key = "tq-" + hashlib.md5((pref + txt).encode()).hexdigest()[:10]
        t = e(txt) + (f' {go(did, "Ver dia ›", "more")}' if did else "")
        o.append(f'<label class="chk"><input type="checkbox" data-k="{key}"><span>{t}</span></label>')
    return "".join(o)
page("checklist", '<div class="wrap">' + simple_head("Preparativos", "Antes de ir")
     + '<p class="muted small">Marque o que já foi feito: fica salvo neste celular.</p>'
     + '<div class="band">Reservar agora</div>' + chk_items(RESERVAR, "r")
     + '<div class="band">Confirmar de 7 a 14 dias antes</div>' + chk_items(CONFIRMAR, "c")
     + "</div>", "Antes de ir")

# ------------------------------------------------------------- reservas (lista com situação)
rs = []
for lst, st in ((RESERVAR, ("wine", "A reservar")), (CONFIRMAR, ("gold", "A confirmar"))):
    for dt, txt, did in lst:
        inner = (f'<div class="rtop"><span class="rdate">{e(dt)}</span><span class="pill {st[0]}">{st[1]}</span></div>'
                 f'<div class="rtt">{e(txt)}</div>')
        rs.append(go(did, inner + '<span class="chev">›</span>', "res") if did else f'<div class="res">{inner}</div>')
page("reservas", '<div class="wrap">' + simple_head("Reservas e ingressos", "Reservas e ingressos",
     "Toque em um item para abrir o dia.") + "".join(rs) + "</div>", "Reservas")

# ------------------------------------------------------------- dicas e fontes
b = '<div class="wrap">' + simple_head("Lembretes", "Dicas da viagem")
b += f'<div class="band">Clima e roupa</div><p class="serif">{e(LEMBRETES)}</p>'
b += '<div class="band">Sobre os horários</div>' + "".join(f'<p class="serif">{e(p)}</p>' for p in INTRO)
b += f'<div class="band">Fontes para reconfirmação</div><p class="small muted">{e(FONTES_NOTA)}</p>'
for n, ds, u in FONTES:
    b += ext(u, f'<div class="rtt">{e(n)}</div><div class="muted small">{e(ds)}</div><span class="chev">›</span>', "res")
b += "</div>"
page("dicas", b, "Dicas")

# ------------------------------------------------------------- dias e lugares
for i, d in enumerate(DAYS):
    b = (f'<header class="dayhead"><span class="big">{e(d["date"].split("/")[0])}</span>'
         f'<div class="kick lgold">Dia {d["n"]} · {e(d["wd"])} · {e(d["date"])}</div>'
         f'<h2>{e(d["title"])}</h2><span class="bar"></span></header><div class="wrap">'
         f'<div class="kick muted">{e(d["place"])}</div>')
    for p in d["intro"]: b += f'<p class="lead">{e(p)}</p>'
    b += ext(d["route"], "Mapa do percurso do dia", "btn wide")
    b += '<ol class="tl">'
    for k, it in enumerate(d["items"]):
        mv = it.get("k") == "move"
        hora = it.get("t", "")
        if mv:
            titulo = it.get("n") or "Deslocamento"
            nota = " ".join(it["p"])
            core = (f'<span class="hora">{e(hora)}</span><span class="dot"></span>'
                    f'<span class="body"><span class="ttl2">{e(titulo)}</span><span class="nota">{e(nota)}</span></span>')
            if it.get("m"):
                b += f'<li class="it">{ext(maps(it["m"]), core + "<span class=legin>Mapa ›</span>", "row")}</li>'
            else:
                b += f'<li class="it"><div class="row">{core}</div></li>'
            continue
        refeicao = any(w in it["n"].lower() for w in ("almoço", "jantar", "café"))
        tem_pagina = bool(it["p"]) and len(" ".join(it["p"])) > 120
        nota = first_sentence(it["p"][0]) if it["p"] else ""
        dot = "refeicao" if refeicao else ("ref" if tem_pagina else "")
        core = (f'<span class="hora{" g" if tem_pagina else ""}">{e(hora)}</span><span class="dot {dot}"></span>'
                f'<span class="body"><span class="{"ttl" if tem_pagina else "ttl2"}">{e(it["n"])}</span>'
                + (f'<span class="nota">{e(nota if tem_pagina else " ".join(it["p"]))}</span>' if it["p"] else "") + "</span>")
        if tem_pagina:
            pid = f'{d["id"]}-{slug(it["n"])}'
            b += f'<li class="it">{go(pid, core + "<span class=chev>›</span>", "row")}</li>'
            # página do lugar
            pb = (f'<div class="wrap"><div class="kickrow"><div class="kick">Dia {d["n"]} · {e(d["date"])} · {e(hora)}</div></div>'
                  f'<h2 class="h">{e(it["n"])}</h2>')
            busca = (it.get("m") or it["n"]).split(",")[0]
            pb += ext(gimg(busca + " " + ("Istanbul" if i < 4 else "Turkey")), "<span>Ver fotos ›</span>", "nophoto")
            pb += '<div class="btn2">'
            pb += ext(maps(it["m"]), "Como chegar", "btn") if it.get("m") else ""
            if it.get("l"): pb += ext(it["l"][0][1], e(it["l"][0][0]), "btn line")
            elif it.get("m"): pb += ext(gimg(busca), "Mais fotos", "btn line")
            pb += "</div>"
            pb += '<div class="band">No roteiro</div><div class="serif">' + "".join(f"<p>{e(p)}</p>" for p in it["p"]) + "</div>"
            for lab, url in it.get("l", [])[1:]:
                pb += ext(url, e(lab), "btn line wide")
            pb += go(d["id"], f'‹ Dia {e(d["date"])}', "chip") + "</div>"
            page(pid, pb, it["n"])
        elif it.get("m"):
            b += f'<li class="it">{ext(maps(it["m"]), core + "<span class=legin>Mapa ›</span>", "row")}</li>'
        else:
            b += f'<li class="it"><div class="row">{core}</div></li>'
    b += "</ol>"
    if d.get("walk"): b += f'<p class="small muted" style="margin-top:14px"><i>{e(d["walk"])}</i></p>'
    prev = DAYS[i - 1] if i else None
    nxt = DAYS[i + 1] if i + 1 < len(DAYS) else None
    b += ('<nav class="pn">' + (go(prev["id"], "‹ " + e(prev["date"]), "chip") if prev else "<span></span>")
          + go("inicio", "Sumário", "chip") + (go(nxt["id"], e(nxt["date"]) + " ›", "chip") if nxt else go("checklist", "Antes de ir ›", "chip")) + "</nav></div>")
    page(d["id"], b, f'{d["date"]} · {d["title"]}', "day")

# ------------------------------------------------------------- ícones (mesmo desenho do de Roma, em verde)
GREEN, GOLD, LGOLD = "#1E646B", "#B8893B", "#E8C987"
FONTS = os.path.join(roma, "docs", "fonts")
def icon(size, path, pad=0.0):
    im = Image.new("RGB", (size, size), GREEN); dr = ImageDraw.Draw(im)
    s = size; inset = int(s * (0.1 + pad))
    dr.rectangle([inset, inset, s - inset, s - inset], outline=GOLD, width=max(2, s // 90))
    f1 = ImageFont.truetype(os.path.join(FONTS, "Lora-600.ttf"), int(s * (0.24 - pad * 0.4)))
    f2 = ImageFont.truetype(os.path.join(FONTS, "Lora-MediumItalic.ttf"), int(s * (0.11 - pad * 0.2)))
    dr.text((s / 2, s * 0.47), "Turquia", font=f1, fill="#FFFDF9", anchor="ms")
    dr.text((s / 2, s * 0.64), "2026 · 2027", font=f2, fill=LGOLD, anchor="ms")
    im.save(os.path.join(out, path))
icon(512, "icons/icon-512.png"); icon(192, "icons/icon-192.png"); icon(180, "icons/apple-touch-icon.png")
icon(512, "icons/maskable-512.png", pad=0.06)

# ------------------------------------------------------------- arquivos (CSS e JS do app de Roma, cores trocadas)
css = open(os.path.join(roma, "gerador", "app.css"), encoding="utf-8").read()
css = (css.replace("--wine:#7A2E1F", "--wine:" + GREEN).replace("--wine2:#8E3C2B", "--wine2:#2A7279")
          .replace("--alert:#F6E3D6", "--alert:#E3EFEC"))
js = open(os.path.join(roma, "gerador", "app.js"), encoding="utf-8").read().replace("Roma con Amore", "Turquia")
open(os.path.join(out, "app.css"), "w", encoding="utf-8").write(css)
open(os.path.join(out, "app.js"), "w", encoding="utf-8").write(js)

index = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Turquia</title>
<meta name="description" content="{e(SUBTITLE)} · {e(DATES)}">
<meta name="theme-color" content="{GREEN}">
<meta name="color-scheme" content="light">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Turquia">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="stylesheet" href="app.css">
</head>
<body>
<div class="topbar"><button id="voltar" aria-label="Voltar">‹</button><span id="titulo">Turquia</span><a id="casa" href="#inicio" aria-label="Sumário">☰</a></div>
<main>
{"".join(PAGES)}
</main>
<script src="app.js"></script>
</body>
</html>'''
open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(index)

manifest = {"name": "Turquia 2026–2027", "short_name": "Turquia", "lang": "pt-BR", "start_url": "./", "scope": "./",
            "display": "standalone", "background_color": "#F7F1E6", "theme_color": GREEN,
            "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                      {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                      {"src": "icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
json.dump(manifest, open(os.path.join(out, "manifest.webmanifest"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

files = []
for root, _, fs in os.walk(out):
    if ".git" in root: continue
    for f in fs:
        rel = os.path.relpath(os.path.join(root, f), out).replace(os.sep, "/")
        if rel not in ("sw.js", "CNAME") and not rel.startswith("."): files.append(rel)
files.sort()
hsh = hashlib.sha1()
for f in files: hsh.update(f.encode()); hsh.update(open(os.path.join(out, f), "rb").read())
ver = hsh.hexdigest()[:10]
sw = open(os.path.join(roma, "gerador", "sw.js"), encoding="utf-8").read()
sw = sw.replace('"roma-__VERSAO__"', '"turquia-__VERSAO__"').replace("__VERSAO__", ver).replace("__ARQUIVOS__", json.dumps(["./"] + files, indent=0))
open(os.path.join(out, "sw.js"), "w", encoding="utf-8").write(sw)
open(os.path.join(out, ".nojekyll"), "w").write("")
tot = sum(os.path.getsize(os.path.join(out, f)) for f in files)
print(f"ok {out}: {len(PAGES)} telas, {len(files)} arquivos, {tot / 1e6:.1f} MB, versão {ver}")
