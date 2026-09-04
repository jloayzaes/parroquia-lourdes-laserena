# -*- coding: utf-8 -*-
"""Mide el contraste real del texto sobre las bandas con fotografía.

Las tres bandas del sitio —la portada, la de la Patrona y la del 1%— llevan un
velo semitransparente encima de una foto. Estimar el contraste con un color de
fondo promedio engaña: lo que decide es el píxel más oscuro que queda bajo el
texto. Este script compone el velo sobre la fotografía con la misma geometría
que usa el navegador (cover + background-position) y busca ese peor caso.

La geometría de cada banda —tamaño, posición del fondo y caja de cada texto— se
saca del navegador con getBoundingClientRect y se pasa a mano, porque cambia con
el ancho de la ventana.

Se usó para bajar los velos sin romper el mínimo AA de 4,5:1 que pidió la
parroquia. La clave fue oscurecer el texto a --azul: con --azul-medio no había
margen para transparentar nada.
"""
from PIL import Image

def lum(c):
    f = lambda v: (v/255/12.92) if v/255 <= .03928 else (((v/255)+.055)/1.055)**2.4
    r,g,b = map(f, c); return .2126*r+.7152*g+.0722*b
def contraste(a,b):
    L1,L2 = lum(a), lum(b); return (max(L1,L2)+.05)/(min(L1,L2)+.05)

def medir(archivo, banda, posicion, paradas, horizontal, textos, nombre=""):
    W,H = banda
    im = Image.open(f"sitio/assets/img/{archivo}").convert("RGB")
    iw,ih = im.size
    esc = max(W/iw, H/ih)
    dw,dh = iw*esc, ih*esc
    px,py = posicion
    ox, oy = (dw-W)*px, (dh-H)*py
    im = im.resize((round(dw), round(dh)), Image.LANCZOS).crop(
        (round(ox), round(oy), round(ox)+W, round(oy)+H))
    px_ = im.load()
    def alfa(x, y):
        t = (x/W) if horizontal else (y/H)
        for i in range(len(paradas)-1):
            p0,a0 = paradas[i]; p1,a1 = paradas[i+1]
            if p0 <= t <= p1:
                k = 0 if p1 == p0 else (t-p0)/(p1-p0)
                return a0 + (a1-a0)*k
        return paradas[-1][1]
    peores = []
    for t in textos:
        x0,y0,w,h = t["caja"]; color = t["color"]
        peor, donde = 99, None
        for y in range(max(0,y0), min(H, y0+h), 3):
            for x in range(max(0,x0), min(W, x0+w), 3):
                a = alfa(x, y)
                fondo = [round(VELO[i]*a + px_[x,y][i]*(1-a)) for i in range(3)]
                c = contraste(color, fondo)
                if c < peor: peor, donde = c, (x,y)
        peores.append((t["sel"], round(peor,2), donde))
    print(f"  {nombre or archivo}")
    for sel, c, d in peores:
        estado = "ok" if c >= 4.5 else "BAJO AA"
        print(f"    {sel:22} {c:5.2f}  {estado}")
    return min(c for _,c,_ in peores)
