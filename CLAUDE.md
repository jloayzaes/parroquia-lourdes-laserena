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

El menú tiene **nueve botones**: Inicio · Nuestra parroquia · Horarios ·
Sacramentos · Servicios · Certificados · Capillas · Pastorales · **Avisos**.

**Avisos cierra la fila** y se distingue solo por el peso
(`.menu__enlace--destacado`): mismo azul parroquial que los demás, en negrita, sin
fondo ni ícono. Es deliberadamente sutil —se probó como botón celeste y el cliente
lo pidió más discreto—, así que no volver a agregarle caja, color propio ni ícono.
Cuando está activo sigue la regla general: celeste con subrayado inset.

El menú horizontal ocupa 1076px y cabe justo sobre **1180px**, que es el umbral del
menú táctil; quedan 32px de holgura. **Un décimo botón obliga a repensar el menú**,
no basta con sumarlo.

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
  Varias excepciones, todas porque Phosphor no tiene el glifo. **Dibujadas
  aquí, en SVG en línea** con el mismo trazo de 8 sobre un `viewBox` de 256: el
  calendario-con-reloj del horario de Secretaría en la cabecera, los **anillos**
  de Matrimonio —que usan una máscara para abrir el hueco donde uno cruza al
  otro— y el **cirio** de Bautismo. Dentro de un `.badge` se dimensionan solas
  con la regla `.badge svg`.

  **Entregadas por la parroquia**: el ostensorio de Adoración
  (`assets/img/icono-adoracion.png`, que reemplaza al badge entero) y el
  **cáliz** de Primera Comunión (`icono-primera-comunion.png`, que va dentro del
  badge con `.badge__dibujo`). Los dibujos llegan como línea oscura sobre
  blanco y hay que convertirlos: recortar a la caja del dibujo, engrosar el
  trazo —el suyo es unas cuatro veces más fino que el de Phosphor y a 38px
  desaparece— y guardarlo en blanco con transparencia. El script está en el
  historial del commit que los incorporó.

  Si hace falta otro ícono compuesto, seguir estos patrones antes que mezclar
  familias.

  La **paloma de Confirmación** es la quinta excepción y llegó dibujada desde la
  parroquia, en un SVG que traía un texto al pie: se recortó ese texto, se
  normalizó el trazado a un `viewBox` de 256 y se centró. Es un contorno
  *relleno*, no un trazo, y su línea es más fina que la de Phosphor, así que a
  tamaño de ícono se desvanecía. Se corrige con `.badge svg.paloma`, que le
  agrega `stroke` para engrosarla y le da un 69 % del badge en vez del 55 %,
  porque es una figura ancha y con mucho aire.
- **Sin `border-radius`** en tarjetas ni botones. Solo círculos perfectos en los
  badges de ícono (`.badge`).
- **Sin animaciones decorativas.**
- En hover de menú y pestañas se engruesa con `text-shadow`, **nunca** con
  `font-weight`: cambiar el peso mueve el layout.

## Reglas de redacción que pidió la parroquia

- **«Parroquia», nunca «parroquia matriz».** Es una sola parroquia con un
  santuario y cinco capillas; la distinción entre ellos se mantiene, pero sin
  esa palabra.
- **Los días van en plural** cuando el horario se repite cada semana:
  «Sábados 19:00 hrs.», «Domingos 11:00 hrs.». En español solo cambian sábado y
  domingo; lunes a viernes son invariables. Los rangos se dejan como están
  («martes a sábado»), porque «martes a sábados» no es correcto. El singular se
  reserva para una celebración con fecha propia: «Domingo 13 de septiembre».
- **El sacramento se llama «Reconciliación · Confesión»**, en el menú, en la
  ficha y en las tarjetas de Inicio y Horarios.
- **«Unción de los enfermos»**, con minúscula en «enfermos».
- En las fichas de sacramentos con catequesis el campo es **«Duración de la
  catequesis»**, no «Destinatarios» ni «¿A quién está dirigido?». La edad y las
  condiciones para participar van en «Requisitos».
- Unción y Reconciliación **no llevan** Destinatarios, Requisitos ni Documentos.
- Las fichas de pastorales **no llevan** frecuencia de reunión, actividades ni
  cantidad de integrantes.
- Las capillas **no publican horario de atención**, solo el de la Santa Misa.

## Datos con ícono

Todo dato de contacto o de horario va acompañado de su ícono, siempre el mismo:

| Dato | Ícono |
|---|---|
| Días de atención | `ph-calendar-blank` |
| Horas | `ph-clock` |
| Dirección | `ph-map-pin` |
| Teléfono | `ph-phone` |
| Correo | `ph-envelope-simple` |

La estructura es `.datos-icono`, una lista donde cada `<li>` lleva el ícono y un
`<span>`. Está en Horarios, Sacramentos, Servicios, Certificados y Pastorales:
**si se agrega un bloque de contacto nuevo, usar esa misma lista.** Los días y
las horas van en líneas separadas, cada una con su ícono.

`.aclaracion` es la nota que acompaña a un dato: un punto más chica y en gris
medio. Con `--cursiva` para la aclaración de la Misa de San Carlo Acutis.

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

Hay **tres avisos reales**, entregados por la parroquia con sus fotos: la kermés
del 13 de septiembre, la inscripción de pymes y el inicio de la campaña del 1%.
Los ejemplos que traía el handoff (catequesis, adulto mayor, misioneros del 1%)
eran inventados y se sacaron: **no volver a poner avisos de muestra en el sitio
publicado**. Si en algún momento no hay avisos vigentes, es preferible borrar la
sección antes que dejar plantillas en blanco a la vista.

La línea celeste de arriba no es solo una fecha: es **fecha o estado**. Puede ser
un día («Domingo 13 de septiembre de 2026»), un plazo («Hasta el viernes 11 de
septiembre») o una situación («Inscripciones abiertas»). Cuando es una fecha
concreta va dentro de `<time datetime="AAAA-MM-DD">`; cuando es un estado, no
lleva `<time>`.

El **aviso destacado** sí es información real —la Misa de San Carlo Acutis del día
12, que también aparece en `horarios.html`— y por eso se mantuvo.

La rejilla de avisos tiene clase propia, `.rejilla--avisos`: cada ficha es una
foto de 200px más el texto al lado, así que **necesita ancho**. Sobre 1180px van
dos columnas; bajo eso, una sola. Con dos columnas en pantallas medianas la
columna de texto quedaba en 150px y el contenido se salía.

Las fotos van en `assets/img/aviso-*.jpg`, exportadas a **800px de ancho** y
comprimidas (unos 150–200 KB). El hueco mide 200×152 en escritorio, así que la
foto se recorta con `object-fit: cover`: conviene que el motivo esté al centro.

## Ilustraciones de los sacramentos

Las siete fichas llevan ilustración (`assets/img/sacramento-*.jpg`): acuarelas
cuadradas sobre **fondo blanco**, entregadas por la parroquia, exportadas a
720×720 y unos 55 KB. Van en `img.ficha__foto` con `object-fit: contain`, no
`cover`: como el fondo de la ilustración es el mismo blanco de la ficha, se ven
enteras sin costura, y recortarlas cortaba el cirio o la rama que acompañan al
símbolo.

El orden de las fichas y del desplegable del menú lo fijó la parroquia:
**Bautismo · Primera Comunión · Confirmación · Catequesis de adultos ·
Matrimonio · Reconciliación · Unción**. Si se reordena, hay que recalcular la
alternancia: las fichas impares son `.ficha` y las pares
`.ficha ficha--invertida`, para que la ilustración vaya cambiando de lado.

## Coordinador, coordinadora, coordinadores

La etiqueta se escribe según quién coordina, no en genérico: **Coordinador** si
es un hombre, **Coordinadora** si es una mujer, **Coordinadoras** si son dos
mujeres y **Coordinadores** si hay un hombre y una mujer. Donde coordina un
matrimonio la etiqueta es **Matrimonio coordinador** —Pastoral de Migrantes,
Pastoral de Redes Sociales y el Coro Matrimonio Rodríguez Gallardo—. Mientras el
nombre esté sin confirmar se deja **Coordinador/a**.

## Fotografías

Todas las fotos son marcadores rayados con su medida:

```html
<div class="foto" style="--alto:300px" aria-hidden="true">FOTO PRINCIPAL<br>Capilla Corpus Christi<br>460×300</div>
```

Al llegar la foto real se reemplaza el bloque completo por un `<img>` con `alt`
descriptivo, `width`/`height` (evitan el salto de layout mientras carga) y
`loading="lazy"` si está bajo el pliegue:

```html
<img class="capilla__foto" src="assets/img/capilla-corpus-christi.jpg"
     alt="Fachada roja y blanca con techo de zinc y campanario de ladrillo"
     width="920" height="600" loading="lazy">
```

El `alt` **describe la foto**, no repite el nombre que ya está en el `<h3>` de al
lado: quien usa lector de pantalla ya escuchó el nombre.

Las clases `.templo__foto` (Horarios) e `img.capilla__foto` (Capillas) llevan
`object-fit: cover`, así que la foto se recorta al hueco sin deformarse. Aun así
conviene entregar el recorte hecho, porque **cada templo se muestra en dos huecos
de proporción muy distinta**:

| Página | Hueco | Se exporta a |
|---|---|---|
| Capillas | 460×300 (relación 1,53) | 920×600 |
| Horarios | 688×170 (relación 4,05) | 1376×340 |

La banda de Horarios es tan apaisada que no cabe una torre entera: hay que elegir
qué franja se ve. Para eso está `herramientas/recortar-fotos.py`, que hace los
dos recortes de una vez:

```bash
python3 herramientas/recortar-fotos.py "~/Downloads/Santiago Apóstol.png" capilla-santiago --centro 0.45
```

`--centro` va de 0 a 1 sobre el alto del original y decide qué franja sobrevive.
**Hay que mirar el resultado**: si cortó la torre o la cruz, se repite con otro
valor. Cuando el original viene vertical —como el de San Joaquín— la banda queda
en una franja angosta, así que conviene centrarla en el elemento reconocible
(ahí, la cruz vidriada).

Peso: JPEG con calidad 80, entre 50 y 110 KB por archivo.

Exportar al doble de la medida indicada (retina) y comprimir.

**Ojo con `aspect-ratio`**: si el `<img>` trae atributos `width`/`height`, el
navegador los usa como alto y el `aspect-ratio` del CSS no se aplica. Hay que
agregar `height: auto` en la regla. Pasó en el par de la historia y en la gruta.

Sobre las dos fotos de fondo va un **velo blanco**, no azul: la parroquia lo
pidió así para que la fotografía se vea. Por eso el texto de esas dos bandas va
en `--azul` y `--azul-medio`, y sus botones son el relleno normal y
`.boton--linea-azul`. Si alguna vez se vuelve al velo oscuro, hay que devolver
también los textos a blanco y los botones a `--blanco` y `--linea-blanca`.

El hero de `index.html` y la banda de la Patrona son **fondo de sección**, en
`.hero` y `.banda-patrona` de `sitio.css`. Van a 1600px de ancho y con calidad
68, porque encima llevan un velo oscuro que tapa el detalle fino, y **tienen una
versión chica para el teléfono** (`-movil.jpg`, 900px) que se cambia en el
quiebre de 760px: pesan un tercio y en un celular no se nota la diferencia. Si
se agrega otro fondo de sección, conviene repetir ese par.

## Accesibilidad (requisito del cliente, no opcional)

- Cuerpo mínimo **17px**. Contraste AA (4.5:1) en todo texto pequeño.
- **El botón `.boton` va en `--azul-medio`, no en `--celeste`.** Con celeste, su
  texto blanco de 14px quedaba en 2,89:1, muy por debajo de AA; en azul medio
  sube a 6,6:1. Cualquier color de fondo nuevo para texto blanco hay que
  medirlo antes.
- Queda pendiente el mismo problema en `.antetitulo`, que usa `--celeste` sobre
  blanco (2,7:1). Es el rótulo pequeño en mayúsculas que encabeza las secciones;
  cambiarlo toca todas las páginas, así que está a la espera de decisión.
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

### Tres trampas que ya rompieron el móvil una vez

**`.pagina` lleva `overflow-x: hidden`.** Eso significa que lo que se sale del
ancho no se puede arrastrar para verlo: queda cortado y el visitante nunca se
entera. Un desborde en móvil no se ve como un error, se ve como texto que falta.
Por eso conviene medirlo, no mirarlo: en la consola del navegador, a 375px,

```js
const vw = document.documentElement.clientWidth;
[...document.querySelectorAll('body *')]
  .filter(el => el.getBoundingClientRect().right > vw + 1 && el.className !== 'salto-contenido')
  .forEach(el => console.log(el.tagName, el.className, Math.round(el.getBoundingClientRect().width)));
```

**Un `style=` en línea le gana a cualquier media query.** Una rejilla con
`style="grid-template-columns:300px 1fr"` se queda en dos columnas en el
teléfono aunque `sitio.css` diga lo contrario, y la segunda columna —el texto—
desaparece de la pantalla. Es lo que pasaba en `historia.html` y `patrona.html`.
Si un valor tiene que cambiar en móvil, va en una clase, no en línea. Para eso
existen `.rejilla--con-lateral` (con `--col-lateral` para el ancho) y
`.panel-cierre`. En línea solo quedan valores que no cambian con el ancho.

**Un correo es una sola palabra.** No se puede cortar por sílabas, así que
ensancha su tarjeta más allá del borde de la pantalla. Se resuelve por los dos
lados: `a[href^="mailto:"] { overflow-wrap: anywhere }` en el CSS, y un `<wbr>`
después de la arroba en el HTML —`secretariaplourdes@<wbr>gmail.com`— para que
el corte caiga en el lugar correcto y no en mitad del dominio. **Todo correo que
se agregue al sitio necesita ese `<wbr>`.**

Por lo mismo, los marcadores de foto llevan el alto limitado en el teléfono
(`min(var(--alto), 58vw)`): el alto fijo del handoff está pensado para el
escritorio y en un celular se come media pantalla.

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
