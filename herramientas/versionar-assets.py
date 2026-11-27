# -*- coding: utf-8 -*-
"""Pone la versión del CSS y del JS en las doce páginas.

El sitio no tiene build, así que nada le pone una huella a los archivos. Sin
ella, quien ya visitó el sitio puede seguir viendo el CSS viejo durante días
después de un cambio: el navegador no tiene cómo saber que caducó.

La versión es el hash del propio archivo, así que cambia sola cuando cambia el
contenido y no hay que acordarse de subir un número.

    python3 herramientas/versionar-assets.py

Ejecutarlo SIEMPRE antes de un commit que toque sitio.css o sitio.js.
"""
import glob, io, re, hashlib, os, sys

raiz = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitio")
os.chdir(raiz)
css = hashlib.sha1(io.open("assets/css/sitio.css", "rb").read()).hexdigest()[:8]
js = hashlib.sha1(io.open("assets/js/sitio.js", "rb").read()).hexdigest()[:8]
cambiadas = 0
for f in sorted(glob.glob("*.html")):
    if f.startswith("_"):
        continue
    s = io.open(f, encoding="utf-8").read()
    antes = s
    s = re.sub(r'href="assets/css/sitio\.css(\?v=[0-9a-f]+)?"',
               f'href="assets/css/sitio.css?v={css}"', s)
    s = re.sub(r'src="assets/js/sitio\.js(\?v=[0-9a-f]+)?"',
               f'src="assets/js/sitio.js?v={js}"', s)
    if s != antes:
        io.open(f, "w", encoding="utf-8").write(s)
        cambiadas += 1
print(f"css v={css} · js v={js} · {cambiadas} páginas actualizadas")
