# -*- coding: utf-8 -*-
"""Cambia el aviso de la barra superior en las doce páginas de una vez.

La barra lleva el aviso vigente —una kermés, una celebración, una inscripción—
y está repetida en las doce páginas porque el sitio no tiene build. Editarlas a
mano es cómo se termina con un aviso de septiembre en noviembre.

    python3 herramientas/aviso-barra.py "Misa de Navidad · 24 de diciembre 20:00" "avisos.html#aviso-navidad"
    python3 herramientas/aviso-barra.py --quitar

Después de usarlo no hace falta versionar nada: solo cambia HTML.
"""
import glob, io, re, os, sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitio"))
BLOQUE = re.compile(
    r'<span class="barra-superior__dato barra-superior__aviso">.*?</span>', re.S)

if len(sys.argv) == 2 and sys.argv[1] == "--quitar":
    nuevo = ""
elif len(sys.argv) == 3:
    texto, destino = sys.argv[1], sys.argv[2]
    nuevo = ('<span class="barra-superior__dato barra-superior__aviso">'
             '<i class="ph-thin ph-calendar-dot" aria-hidden="true"></i>'
             f'<a href="{destino}">{texto}</a></span>')
else:
    print(__doc__)
    sys.exit(1)

n = 0
for f in sorted(glob.glob("*.html")):
    if f.startswith("_"):
        continue
    s = io.open(f, encoding="utf-8").read()
    s2 = BLOQUE.sub(nuevo, s)
    if s2 != s:
        io.open(f, "w", encoding="utf-8").write(s2)
        n += 1
print(f"{n} páginas actualizadas" if n else "No se encontró el bloque del aviso.")
