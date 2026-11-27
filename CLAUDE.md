# Sitio web · Parroquia Nuestra Señora de Lourdes (La Serena)

Sitio parroquial público. **Todo se escribe en español** (es-CL): el contenido,
los comentarios del código y los nombres de clases.

El público objetivo son **personas de mediana edad y jóvenes**, con manejo
digital normal. *(Corregido el 26 de noviembre de 2026: hasta entonces este
archivo decía «adultos mayores y personas con poca experiencia digital», y esa
premisa frenó decisiones de diseño durante meses. No volver a esa redacción.)*

Eso **no** rebaja la accesibilidad, que sigue siendo requisito del cliente:
contraste AA, 17px de cuerpo mínimo, áreas táctiles de 44px. Lo que cambia es el
techo: el sitio puede permitirse interacción, movimiento y un acabado más
ambicioso, en vez de resolverlo todo por la vía más conservadora.

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

  La paleta entera vive en once grados de tono, del 206° al 217°: es un solo
  azul en catorce claridades. Eso le da unidad, pero significa que **el color no
  puede crear jerarquía** —si todo es el mismo azul, nada destaca por ser
  azul—. La jerarquía la hacen el tamaño, el peso y el espaciado; el color solo
  separa lo oscuro de lo claro. Antes de agregar un token nuevo conviene
  preguntarse si no hay ya uno que haga lo mismo: `--texto-2` y `--pie-texto` se
  eliminaron por eso, porque eran indistinguibles de `--texto` y de
  `--celeste-sobre-azul`.

  Tres tokens tienen un uso acotado y no son grises de propósito general:

  | Token | Solo para |
  |---|---|
  | `--pendiente` | `[POR COMPLETAR]` y marcadores de foto. Para texto secundario real va `--texto-3`. |
  | `--error` · `--error-fondo` | Algo salió mal. Hoy: el aviso del formulario de certificados. |
  | `--exito` · `--exito-fondo` | Algo salió bien. Hoy: el visto y el recuadro de la confirmación de envío. |
  | `--acento` | **Dónde estás**, y nada más. |

  `--acento` (`#9C6B2E`) es el **único color cálido del sitio** y la única
  excepción a que todo sea azul. Sale de la fotografía de la propia parroquia:
  las tejas del techo y las llamas de los cirios de las acuarelas. Marca una
  sola cosa —el ítem activo del menú, la pestaña activa y la categoría activa
  del índice— y su fuerza viene justamente de eso: es lo único no azul en la
  pantalla. **Repartirlo por antetítulos o enlaces lo convierte en un segundo
  color de marca y deja de marcar nada**; se probó así y se descartó.

  **No está en el manual de identidad y aun así se queda**: la parroquia lo
  confirmó el 26 de noviembre de 2026, después de ver las tres versiones. Si
  algún día se actualiza el manual, este es el color que habría que agregarle.

  Error y éxito están desaturados a propósito: al lado de este azul, un rojo o
  un verde vivos se leen como un cuerpo extraño. **Sin ellos el formulario no
  comunicaba**: el mensaje de error tenía exactamente el mismo estilo que una
  nota informativa.
- **Clases**: en español, estilo BEM suave — `.templo__nombre`,
  `.ficha--invertida`, `.indice__enlace--activo`.
- **Tipografía**: solo **Nunito Sans** (Google Fonts, OFL). Reemplazó a
  Montserrat el 26 de noviembre de 2026, por decisión de la parroquia: sigue la
  línea de Vatican News, que usa Museo Sans —de pago—, y Nunito Sans es su
  equivalente libre. El documento original está en
  `tipografia-web-nunito-sans.md`; venía escrito para un proyecto Next.js con
  Tailwind, así que **las secciones 2, 3 y 5 no aplican aquí**: este sitio no
  tiene build. Lo que sí aplica —la familia, los grosores, la escala y las
  reglas de redacción visual— está traducido a `sitio.css`.

  **El cuerpo son 16px, no 17.** Se midió el tamaño dominante de las tres
  referencias —Vatican News 15px, Cedarcrest 16, Holy Family 16— y el sitio
  estaba en 18, herencia del público equivocado que este archivo daba por bueno
  hasta noviembre de 2026. Bajó a 16, el secundario a 15 y los rótulos a 13, y
  el sitio pasó de 40,8 a 37,6 pantallas.

  **Dos excepciones a 17px, y tienen motivo medido**: `.acceso p`,
  `.aviso-tarjeta__texto` y `.texto-tarjeta` viven en columnas estrechas, y a
  16 su línea bajaba a 47–53 caracteres, por debajo del rango cómodo.

  **Bajar el cuerpo obliga a acotar la medida.** Sin tope, los párrafos pasaban
  de 74 caracteres por línea a 88. Hay `max-width: 39em` en el texto de lectura
  y 42em en `.aclaracion`; hoy la media del sitio es de 65 caracteres.
  **No usar la unidad `ch`**: mide el ancho del glifo «0», que en Nunito Sans
  vale 0,6em, así que `68ch` daban 652px, es decir 88 caracteres. Se cometió
  ese error y solo apareció al medir las líneas reales.

  **Grosores: 300, 400, 600 y 700.** No hay 200 ni 500, y no se piden al CDN.
  El contraste lo da el grosor, no una segunda familia.

  | px | Peso | Interl. | Rol | En móvil |
  |---|---|---|---|---|
  | 44 | 300 + `<strong>` 700 | 1.1 | Título mayor: hero y portada de sección | 32 |
  | 32 | 300 | 1.2 | Título de sección | 26 |
  | 24 | 600 | 1.25 | Cifra destacada: hora de Misa, dato grande | 22 |
  | 21 | 700 | 1.25 | Título de tarjeta, de ficha, de templo | 19 |
  | 21 | 300 | 1.35 | Frase destacada: franja del 1 %, bajada del hero | 19 |
  | 20 | 300 *itálica* | 1.35 | Cita | 18 |
  | 18 | 400 | 1.65 | **Cuerpo** | 17 |
  | 14 | 600 | 1.4 | Dato y etiqueta: menú, botones, rótulos | 14 |
  | 13 | 600 | 1.4 | **Antetítulo** · `letter-spacing: .25em` | 12 |
  | 17 | 400 | 1.6 | Contenido secundario: aclaraciones, ayudas, subtítulos | 17 |
  | 13 | 400 | 1.5 | Solo accesorio: crédito del pie y marcadores de foto | 13 |

  **La única excepción al peso 300 es `.banda-patrona h2`**, que va en 600. La
  parroquia pidió dos veces que ese título fuera más grueso, primero con
  Montserrat y otra vez con Nunito Sans: sobre la fotografía un 300 cuesta de
  leer. Su `<strong>` sigue en 700, así que las dos mitades casi no se
  distinguen; se aceptó a cambio de que el título se lea.

  **Las mayúsculas sostenidas quedan solo en el antetítulo.** El menú, los
  botones, las pestañas y todos los rótulos van en minúscula normal, y sin
  `letter-spacing`. Eso encogió el menú de 1076px a 821px, así que ahora sobran
  287px en el quiebre de 1180 en vez de 32: **hoy sí cabría un décimo botón**.

  El `letter-spacing` solo sobrevive en tres sitios: el antetítulo (`.25em`),
  los títulos mayores (`-.01em`) y los dos lockups de marca.

  `body` lleva `font-variant-numeric: lining-nums tabular-nums`, para que los
  horarios y los teléfonos queden alineados en columna.

  **El documento es referencia, no ley**, y donde choca con lo que ya estaba
  medido gana lo medido. Dos casos concretos:

  - Su «nota y texto secundario» en **13px** se subió a **17px** donde el texto
    es contenido real —`.aclaracion`, `.campo__ayuda`, `.ficha__subtitulo`,
    `.formulario__nota`—, porque el mínimo de 17px del cuerpo es un requisito
    de la parroquia y ahí dentro no hay notas al pie sino frases como «Si aún
    no estás bautizado, puedes prepararte…». Los 13px quedan para el crédito
    del pie y los marcadores de foto.
  - Su paleta (sección 3) **no se aplicó a los textos**: ver el apartado de
    colores. El celeste y el azul medio que propone no alcanzan el mínimo AA.

  **Pendiente del documento:** su sección 1 dice que el logotipo es siempre la
  imagen SVG oficial (símbolo + nombre) y que el nombre de la parroquia nunca se
  reescribe en Nunito Sans. Hoy la cabecera y el pie sí lo escriben como texto
  al lado del dibujo. Falta que la parroquia entregue ese SVG.

  **Íconos**: solo Phosphor Thin
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
- **Interacción.** El movimiento es corto, con una sola curva
  (`var(--curva)`), y siempre dentro de `prefers-reduced-motion`. Hay cuatro
  gestos y no más: las tarjetas suben 3px con sombra más alta al pasar por
  encima, la foto de un aviso hace un zoom del 4 %, las piezas aparecen al
  entrar en pantalla, y el menú se queda fijo arriba al despegarse.

  **El revelado lleva red de seguridad y hay que conservarla.** Esconde las
  piezas con `opacity: 0` hasta que el observador las ve; si ese observador no
  dispara, el contenido se queda invisible y la página está rota. Por eso: lo
  que ya está a la vista al cargar no se esconde nunca, y a los 2,5 segundos se
  muestra todo pase lo que pase. Una animación que no ocurre es un detalle;
  contenido que no aparece, no.

  **`.pagina` lleva `overflow-x: clip`, no `hidden`.** Los dos cortan igual lo
  que se sale de ancho, pero `hidden` convierte al elemento en contenedor de
  scroll y eso anula el `position: sticky` del menú. Fue exactamente lo que
  pasó al montarlo.

- **Al cambiar el fondo hay que volver a medir el contraste.** Pasar la página
  de blanco a arena rompió tres cosas en silencio, porque todo estaba medido
  contra blanco: las aclaraciones caían a 4,32, el `[POR COMPLETAR]` a 2,65 y
  **siete separadores quedaban en 1,00 sobre el arena, es decir invisibles**
  —los de Capillas, las pestañas, la línea de tiempo y el encabezado de
  categoría—. Por eso existe `--papel-linea`: la línea que va sobre la página,
  distinta de `--borde`, que va dentro de las tarjetas blancas. Si algún día
  cambia `--papel`, se repite la medición de los dos tokens y de los siete
  selectores.

- **Ya no queda ningún marcador rayado.** Eran once y se fueron todos: cuatro en
  Capillas y Horarios, tres en Sacerdotes, el resto antes. Mientras no llegue la
  fotografía, la ficha va sin imagen —`.capilla--sin-foto`,
  `.sacerdote--sin-foto`—. Un recuadro a rayas al lado de fichas con foto real
  se lee como una imagen rota, y sobre el arena, siendo azul frío, peor todavía.
  **No reintroducirlos.**

- **Densidad de scroll: medir antes de apretar.** Se hizo una pasada completa y
  el reparto es claro: en Horarios y Sacramentos **las imágenes son el 63–68 %
  del alto**; en el resto manda el texto. Apretar el padding de sección y el
  relleno de todas las tarjetas aportó **apenas un 2 %**. El sitio no tiene
  grasa de maquetación, tiene contenido, así que a partir de aquí recortar
  márgenes empieza a recortar legibilidad.

  Lo que sí funcionó: **bajar la foto de las tarjetas de templo de 46/30 a
  46/18** —se llevaba 438 de los 723px de la tarjeta, para tres líneas de
  texto— que dejó Horarios un 13 % más corta. Y quitar repeticiones: el dato de
  inscripción estaba cinco veces en Sacramentos, además de la barra superior y
  de la bajada de esa misma página.

  **Capillas se queda a todo el ancho, una comunidad por fila.** Se probó en
  dos columnas y bajaba un 25 %, pero es la página con mejor lectura del sitio
  y la parroquia prefirió conservarla. No reintentarlo.

- **Las seis comunidades son seis tarjetas iguales** (`.lista-comunidades` y
  `.comunidad`): caja blanca, fotografía a sangre por el lado izquierdo y la
  hora de Misa en 24px arriba a la derecha. Reemplazó en noviembre de 2026 a
  las fichas sin caja separadas por una línea, y el motivo no era de gusto:
  **dos comunidades no tienen fotografía**, así que cuatro fichas iban a dos
  columnas y dos a una, y las seis no se leían como lo mismo. La hora, que es
  lo que se viene a buscar, era el segundo de tres datos en letra normal.

  A las dos sin fotografía les va `.comunidad__foto--sello`, un panel celeste
  con el ícono de iglesia. Es la misma regla de los marcadores rayados por el
  otro lado: un dibujo deliberado se lee como un dibujo, un recuadro vacío se
  lee como una imagen rota. **Cuando lleguen las fotos se cambia el panel por
  un `<img class="comunidad__foto ampliable">` y nada más.**

  La página pasó de 2.676 a 1.715px de fichas, un 36 % menos. Se probaron
  también una rejilla de tarjetas (−56 %) y un directorio desplegable (−67 %),
  y la parroquia eligió esta: las otras dos escondían las fotografías o la
  historia de cada comunidad detrás de un clic, y esas historias son de lo
  mejor que tiene el sitio.

- **Los avisos caducan, y nadie avisa.** En noviembre de 2026 el sitio seguía
  anunciando la kermés del 13 de septiembre en la barra de las doce páginas,
  en la portada y en Avisos, más una inscripción de pymes cerrada el 11 de
  septiembre. Al quitar un aviso hay que mirar **los tres sitios**: la barra
  (`herramientas/aviso-barra.py`), la tarjeta de la portada y la ficha de
  `avisos.html`. La rejilla de la portada aguanta uno, dos o tres avisos sin
  descuadrarse.

- **El fondo lleva grano, no líneas.** `.pagina` combina el arena con un ruido
  fractal en SVG al 5,5 % de opacidad. Un plano liso se lee frío por más cálido
  que sea el tono, pero **la primera versión usaba líneas finas y se veían como
  rayas**: lo que funciona es una textura sin dirección. Se probaron cinco
  fondos —liso, grano, puntos, degradado y líneas— y la parroquia eligió el
  grano. Va embebido en el CSS, así que no cuesta una petición.

- **La cabecera en móvil está apretada a propósito.** Ocupaba 280px, el 34 % de
  la pantalla, antes de que empezara el contenido; hoy son 226px. El teléfono
  sale de la barra en el teléfono —está en la tarjeta «Comunícate» y completo en
  el pie—, el logo baja a 50px y la fila del menú a 52px, que sigue sobre el
  mínimo táctil de 44. **No quitar la palabra «Menú»**: va en la misma fila que
  la hamburguesa, no ahorra un solo píxel de alto, y el botón solo con el ícono
  se entiende peor.

- **El aviso de la barra superior se cambia con una herramienta**, no a mano:

  ```bash
  python3 herramientas/aviso-barra.py "Misa de Navidad · 24 de diciembre 20:00" "avisos.html#aviso-navidad"
  python3 herramientas/aviso-barra.py --quitar
  ```

  Está repetido en las doce páginas, que es exactamente cómo se termina con un
  aviso de septiembre en noviembre.

- **Visor de fotografías.** Cualquier `<img class="ampliable">` se abre en
  grande. El `alt` hace de pie de foto, así que no se escribe el texto dos
  veces —y eso es un motivo más para que el `alt` describa de verdad—. Se
  cierra con Escape, con el botón o pinchando fuera, y devuelve el foco a la
  foto de origen. **No ponérselo a la foto de una tarjeta de aviso**: esa
  tarjeta entera ya es un enlace y el clic tiene dueño.

- **Versionado de los assets.** `sitio.css` y `sitio.js` se enlazan con `?v=`
  más el hash de su contenido. Sin eso, quien ya visitó el sitio puede seguir
  viendo el CSS viejo durante días, porque nada le dice al navegador que
  caducó. **Correr `python3 herramientas/versionar-assets.py` antes de cualquier
  commit que toque esos dos archivos**; la versión se calcula sola.
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
| Coordinador o coordinadora | `ph-user` |

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

La portada repite los **tres avisos más recientes**; la lista completa vive en
`avisos.html`. Al agregar un aviso importante hay que tocar los dos archivos.

Los dos usan maquetas distintas a propósito. En `avisos.html` la ficha es
horizontal —foto al lado del texto— porque ahí el aviso se lee entero. En la
portada se ojea, así que van tres **tarjetas verticales de la misma altura**
(`.avisos-portada` y `.aviso-tarjeta`): foto arriba, texto recortado a tres
líneas y el enlace anclado abajo con `margin-top: auto`. La ficha horizontal
dejaba huecos grandes, porque los avisos tienen largos muy distintos.

La tarjeta entera se puede pinchar sin anidar enlaces: el enlace del pie lleva
un `::after` que cubre la tarjeta. Si se agrega otro enlace dentro de la
tarjeta, quedará tapado por ese `::after` — hay que dejarlo fuera o levantarlo
con `position: relative`.

Cada aviso de `avisos.html` tiene `id` (`aviso-kermes`, `aviso-pymes`…) para que
la tarjeta de la portada lleve al aviso correcto.
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
| Capillas y Horarios | relación 46/30 | 920×600 |
| Horarios · ficha de la parroquia | banda de 1400×400 en escritorio | 1400×400 y 920×600 |

La ficha de la parroquia ocupa las dos columnas y por eso lleva **banda ancha**,
pero bajo 960px vuelve a una columna y esa banda deja el Cristo del frontis en
una franja. Ahí `<picture>` cambia al archivo de 920×600, y el CSS le devuelve
la proporción 46/30. **Es el único sitio con dos archivos para la misma foto**:
si se agrega otra ficha ancha, conviene repetir el patrón.

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

La banda de la Patrona enseña una regla que vale para cualquier foto de fondo:
**el velo se diseña contra la composición de la foto, no en abstracto**. Ahí la
gruta está al centro y la Virgen a la altura del 56 % del ancho, así que tanto un
velo parejo —el que había— como uno denso al centro la tapaban. La solución fue
correr el texto a la izquierda y abrir el velo hacia la derecha. Y el ancho del
texto va en **porcentaje**, `min(660px, 46%)`: con 660px fijos, en una pantalla
de 1024 el texto llegaba al 64 % del ancho, ya dentro de la zona transparente,
y el contraste caía a 2,5:1. Medir solo a 1440px no basta.

Sobre las **tres** fotos de fondo va un **velo blanco**, no azul: la parroquia lo
pidió así para que la fotografía se vea. Por eso el texto de esas bandas va
en `--azul` y `--azul-medio`, y sus botones son el relleno normal y
`.boton--linea-azul`. Son el hero de la portada, la banda de la Patrona y la
banda del 1%, esta última con la asamblea del domingo.

Los velos con **degradado horizontal** —más denso donde va el texto, más
transparente donde está el motivo— se vuelven en contra en el teléfono, porque
ahí el texto ocupa todo el ancho y termina cayendo sobre la parte clara. En el
quiebre de 760px hay que pasarlos a un degradado vertical parejo.

**El velo y el color del texto se ajustan juntos.** El texto de estas bandas va
en `--azul`, no en `--azul-medio`: con el azul medio no queda margen para
transparentar el velo sin bajar del mínimo AA. Antes de tocar la opacidad de un
velo hay que medir, porque el promedio engaña —lo que decide es el píxel más
oscuro bajo el texto—:

```bash
python3 herramientas/medir-velos.py     # ver el encabezado del archivo
```

El script compone el velo sobre la foto con la misma geometría del navegador.
Así se detectó que el horario de la portada estaba en 4,37:1 pese a *parecer*
legible. Hoy las tres bandas están entre 5,1 y 6,9:1. Si alguna vez se vuelve al velo oscuro, hay que devolver
también los textos a blanco y los botones a `--blanco` y `--linea-blanca`.

El hero de `index.html` y la banda de la Patrona son **fondo de sección**, en
`.hero` y `.banda-patrona` de `sitio.css`. Van a 1600px de ancho y con calidad
68, porque encima llevan un velo oscuro que tapa el detalle fino, y **tienen una
versión chica para el teléfono** (`-movil.jpg`, 900px) que se cambia en el
quiebre de 760px: pesan un tercio y en un celular no se nota la diferencia. Si
se agrega otro fondo de sección, conviene repetir ese par.

## Accesibilidad (requisito del cliente, no opcional)

- Cuerpo mínimo **17px**. Contraste AA (4.5:1) en todo texto pequeño.
- **Los colores del sitio son los medidos aquí, no los del documento de
  tipografía.** Su sección 3 reproduce la paleta del manual de identidad, y dos
  de esos valores no sirven para texto: el celeste `#6E9CC9` que propone para
  los antetítulos da **2,89:1** y el azul medio `#5C82AB` para datos y
  etiquetas da **4,01:1**, los dos bajo el mínimo que el propio documento exige
  en su sección 8. Siguen vigentes `--celeste: #5083B6` y
  `--azul-medio: #2C5F92`. Del manual sí se tomaron los dos grises de texto,
  porque mejoran: `--texto: #44536B` (7,79:1) y `--texto-3: #5C6F8A` (5,13:1).
  Si alguna vez se quiere el antetítulo en celeste de verdad, `#507191` es el
  mismo tono y llega a 5,11:1.

- **El celeste no es un color de texto.** Es la regla que más se repite en este
  archivo porque es la que más veces se rompió: `.antetitulo`, `.etiqueta-dato`,
  el ítem activo del menú, la barra de contacto y el botón llegaron todos a
  quedar bajo el mínimo por usarlo sobre blanco. Todo texto va en `--azul`,
  `--azul-medio` o los grises; el celeste se reserva para fondos, badges,
  bordes, subrayados y el anillo de foco.
- Hoy el sitio **no tiene ningún par de colores bajo el mínimo**: se midieron
  los trece pares en uso y el más justo es el gris de las aclaraciones sobre
  franja celeste, en 4,67:1.
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
