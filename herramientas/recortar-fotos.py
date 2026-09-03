# -*- coding: utf-8 -*-
"""Recorta una foto de templo a los dos huecos que usa el sitio.

Cada capilla se muestra en dos lugares con proporciones muy distintas:

    Capillas   460x300  (relación 1,53)  ->  se exporta a  920x600
    Horarios   688x170  (relación 4,05)  ->  se exporta a 1376x340

La banda de Horarios es tan apaisada que no cabe una torre entera, así que hay
que elegir qué franja se ve. Eso se hace con --centro (y --centro-x), que van de
0 a 1 sobre el alto (o el ancho) del original: 0.5 es el medio, 0.3 más arriba.

Uso:

    python3 herramientas/recortar-fotos.py "~/Downloads/Santiago Apóstol.png" \\
        capilla-santiago --centro 0.45

    # solo uno de los dos, y afinando la franja de la banda
    python3 herramientas/recortar-fotos.py foto.png capilla-santiago \\
        --solo banda --centro 0.35

Escribe en sitio/assets/img/<nombre>.jpg y <nombre>-banda.jpg. Después hay que
mirarlos: si el recorte cortó algo importante, se repite con otro --centro.

Necesita Pillow (python3 -m pip install Pillow).
"""
import argparse
import os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "sitio", "assets", "img")

MEDIDAS = {"ficha": (920, 600), "banda": (1376, 340)}


def recortar(origen, medida, centro_y, centro_x, calidad, salida):
    im = Image.open(origen).convert("RGB")
    ancho, alto = im.size
    relacion = medida[0] / medida[1]
    # la caja más grande con esa relación que cabe en el original
    if ancho / alto > relacion:
        h = alto
        w = int(round(alto * relacion))
    else:
        w = ancho
        h = int(round(ancho / relacion))
    x = max(0, min(ancho - w, int(round(centro_x * ancho - w / 2))))
    y = max(0, min(alto - h, int(round(centro_y * alto - h / 2))))
    im = im.crop((x, y, x + w, y + h)).resize(medida, Image.LANCZOS)
    im.save(salida, "JPEG", quality=calidad, optimize=True, progressive=True)
    print("%-38s %dx%d   recorte %dx%d en (%d,%d)   %d KB"
          % (os.path.basename(salida), medida[0], medida[1], w, h, x, y,
             os.path.getsize(salida) // 1024))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("origen", help="foto original")
    p.add_argument("nombre", help="nombre de salida sin extensión, p. ej. capilla-santiago")
    p.add_argument("--centro", type=float, default=0.5,
                   help="centro vertical del recorte, de 0 a 1 (por omisión 0.5)")
    p.add_argument("--centro-x", type=float, default=0.5,
                   help="centro horizontal del recorte, de 0 a 1 (por omisión 0.5)")
    p.add_argument("--solo", choices=sorted(MEDIDAS), help="generar solo uno de los dos")
    p.add_argument("--calidad", type=int, default=80, help="calidad JPEG (por omisión 80)")
    a = p.parse_args()

    origen = os.path.expanduser(a.origen)
    if not os.path.exists(origen):
        p.error("no existe el archivo: %s" % origen)
    os.makedirs(DESTINO, exist_ok=True)

    for clave in ([a.solo] if a.solo else ["ficha", "banda"]):
        sufijo = "" if clave == "ficha" else "-banda"
        salida = os.path.join(DESTINO, a.nombre + sufijo + ".jpg")
        recortar(origen, MEDIDAS[clave], a.centro, a.centro_x, a.calidad, salida)


if __name__ == "__main__":
    main()
