# Sitio web · Parroquia Nuestra Señora de Lourdes (La Serena)

Sitio parroquial público. **Todo se escribe en español** (es-CL): el contenido,
los comentarios del código y los nombres de clases.

El público objetivo son **adultos mayores y personas con poca experiencia
digital**. Ante la duda entre elegancia y claridad, gana la claridad.

## Qué se publica

Solo la carpeta `sitio/`. Es HTML, CSS y JavaScript planos: **no hay build, no
hay dependencias, no hay que instalar nada**. Se abre con doble clic o con:

```bash
python3 -m http.server 8123 --directory sitio
```

`design_handoff_sitio_parroquia_lourdes/` es el **handoff de diseño original**
(Claude Design). Su `README.md` es la especificación: tokens, tipografía,
espaciados, comportamiento de cada pantalla y contenidos confirmados por la
parroquia. **Leerlo antes de tocar cualquier decisión visual.**

`LEEME.md` es la guía para quien mantenga el sitio sin ser programador.

## Estructura

```
sitio/
├── index.html                        Inicio
├── historia.html · patrona.html · sacerdotes.html    Nuestra parroquia
├── horarios.html · avisos.html · sacramentos.html · servicios.html
├── certificados.html · capillas.html · pastorales.html
├── uno-por-ciento.html               1% a mi Iglesia
└── assets/{css/sitio.css, js/sitio.js, img/}
```

## La regla que más importa

**La cabecera, el menú y el pie están duplicados en las 12 páginas.** Es el
precio de no tener build. Cualquier cambio en un elemento compartido —un dato de
contacto, un ítem del menú, el pie— hay que aplicarlo en **las doce**, no en una.

El menú tiene **nueve botones**: Inicio · Nuestra parroquia · Horarios · Avisos ·
Sacramentos · Servicios · Certificados · Capillas · Pastorales. Con nueve ya no
cabe en horizontal bajo 1180px, por eso el menú táctil entra en ese umbral y la
holgura sobrante es de solo 32px: **agregar un décimo botón obliga a repensar el
menú**, no basta con sumarlo.

Conviene hacerlo con un script en vez de a mano:

```bash
cd sitio && python3 - <<'PY'
import glob
for f in glob.glob("*.html"):
    s = open(f, encoding="utf-8").read()
    s = s.replace("texto viejo", "texto nuevo")
    open(f, "w", encoding="utf-8").write(s)
PY
```

Lo mismo vale para los datos que se repiten dentro del contenido: el horario de
Secretaría y el teléfono aparecen en varias páginas.

## Convenciones

- **Ancho**: el sitio ocupa la pantalla completa. Los fondos (barra superior,
  hero, portadas de sección, franjas, pie) llegan de borde a borde; el contenido
  se detiene en `--ancho-contenido` (1400px) y se centra. El mecanismo es la
  variable `--canaleta`, que se usa como padding lateral en vez de `--lateral`.
  Al crear una sección nueva a todo el ancho, usar `padding: X var(--canaleta)`.
- **Colores**: siempre vía variables CSS del bloque `:root` en `sitio.css`
  (`var(--azul)`, `var(--celeste)`, `var(--borde)`…). Nunca un hex suelto.
- **Clases**: en español, estilo BEM suave — `.templo__nombre`,
  `.ficha--invertida`, `.indice__enlace--activo`.
- **Tipografía**: solo Montserrat. **Íconos**: solo Phosphor Thin
  (`<i class="ph-thin ph-church" aria-hidden="true">`), por CDN.
- **Sin `border-radius`** en tarjetas ni botones. Solo círculos perfectos en los
  badges de ícono (`.badge`).
- **Sin animaciones decorativas.**
- En hover de menú y pestañas se engruesa con `text-shadow`, **nunca** con
  `font-weight`: cambiar el peso mueve el layout.

## Contenido pendiente

Lo que la parroquia aún no confirma se marca literalmente así:

```html
<span class="pendiente">[POR COMPLETAR]</span>
```

Al completarlo se borra el `<span>` entero y se escribe el texto real. **No
inventar** requisitos, documentos, nombres de coordinadores ni horarios: si el
dato no está, se deja marcado.

## Avisos

`avisos.html` es la página de avisos: cambios de horario, celebraciones
especiales e inscripciones. **No hay noticias en este sitio, solo avisos** —
decisión del cliente. No reintroducir la palabra «noticias» en ningún texto.

La portada repite los **cuatro avisos más recientes**; la lista completa vive en
`avisos.html`. Al agregar un aviso importante hay que tocar los dos archivos.
`avisos.html` lleva un comentario HTML con las instrucciones de copiar y pegar
para quien edite sin ser programador: mantenerlo al día si cambia la estructura.

## Fotografías

Todas las fotos son marcadores rayados con su medida:

```html
<div class="foto" style="--alto:300px" aria-hidden="true">FOTO PRINCIPAL<br>Capilla Corpus Christi<br>460×300</div>
```

Al llegar la foto real se reemplaza el bloque completo por un `<img>` con `alt`
descriptivo y `width`/`height` (evitan el salto de layout mientras carga):

```html
<img class="capilla__foto" src="assets/img/capilla-corpus-christi.jpg"
     alt="Fachada de la Capilla Corpus Christi" width="460" height="300">
```

Exportar al doble de la medida indicada (retina) y comprimir. El hero de
`index.html` y la banda de la Patrona son **fondo de sección**: esas van en
`sitio.css`, en `.hero` y `.banda-patrona`, reemplazando `var(--rayado)`. Como
esas dos secciones son de borde a borde, conviene una imagen de 1920px de ancho.

## Accesibilidad (requisito del cliente, no opcional)

- Cuerpo mínimo **17px**. Contraste AA (4.5:1) en todo texto pequeño.
- Áreas táctiles de **44px o más** en móvil (hoy el menú usa 56px).
- Jerarquía correcta de encabezados, `alt` en toda imagen informativa,
  `<label>` visible en todo campo de formulario.
- Los marcadores de foto van con `aria-hidden="true"`: son decorativos.

## Móvil

Quedó pendiente en el handoff y se resolvió aquí. Los quiebres están al final de
`sitio.css`, comentados: **1000px** (menú hamburguesa con submenús en acordeón),
**960px**, **860px**, **760px** (teléfono) y **460px**. Verificado sin desbordes
hasta 320px.

En escritorio los desplegables del menú se abren por CSS puro (`:hover` /
`:focus-within`); en móvil, con el botón de cada ítem. JavaScript solo interviene
en móvil, en las categorías de Pastorales y en el formulario.

## Formulario de certificados

`certificados.html` envía a un servicio externo definido en la constante
`ENDPOINT_CERTIFICADOS`, al inicio de `sitio/assets/js/sitio.js`. **Mientras esté
vacía el formulario no envía nada** y avisa en pantalla — es deliberado, para no
perder solicitudes en silencio. Las instrucciones de conexión están en `LEEME.md`.

## Antes de dar por terminado un cambio

1. Levantar el servidor local y revisarlo en escritorio (1280px) y móvil (375px).
2. Validar enlaces, anclas, ids duplicados y balance de etiquetas:

```bash
cd sitio && python3 - <<'PY'
import re, os
from collections import Counter
paginas = sorted(f for f in os.listdir(".") if f.endswith(".html"))
problemas = []
for pag in paginas:
    s = open(pag, encoding="utf-8").read()
    for i, n in Counter(re.findall(r'\sid="([^"]+)"', s)).items():
        if n > 1: problemas.append(f"{pag}: id duplicado {i}")
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(("http", "mailto:", "tel:", "#", "assets/")): continue
        destino, _, ancla = href.partition("#")
        if destino not in paginas: problemas.append(f"{pag}: enlace roto -> {href}")
        elif ancla and f'id="{ancla}"' not in open(destino, encoding="utf-8").read():
            problemas.append(f"{pag}: ancla inexistente -> {href}")
print("\n".join(problemas) or "Sin problemas.")
PY
```

3. Revisar la consola del navegador: debe estar limpia.

## Despliegue

GitHub + Vercel. En Vercel, **Root Directory = `sitio`** y framework *Other*
(no hay build). Cada push a la rama principal redespliega solo.
