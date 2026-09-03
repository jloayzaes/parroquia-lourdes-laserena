# Sitio web · Parroquia Nuestra Señora de Lourdes (La Serena)

Sitio estático construido a partir del handoff de Claude Design
(`design_handoff_sitio_parroquia_lourdes/`). Son archivos HTML, CSS y JavaScript
puros: **no hay que compilar ni instalar nada**.

La carpeta que se publica es `sitio/`. Todo lo demás en este proyecto es
material de trabajo.

---

## Qué contiene

```
sitio/
├── index.html              Inicio
├── historia.html           Nuestra parroquia · Nuestra historia
├── patrona.html            Nuestra parroquia · Nuestra Patrona
├── sacerdotes.html         Nuestra parroquia · Sacerdotes
├── horarios.html           Horarios de Misa
├── avisos.html             Avisos de la parroquia
├── sacramentos.html        Sacramentos (7 fichas)
├── servicios.html          Servicios (3 fichas)
├── certificados.html       Solicitud de certificados (formulario)
├── capillas.html           Capillas y Santuario (6 fichas)
├── pastorales.html         Pastorales y grupos (5 categorías, 29 grupos)
├── uno-por-ciento.html     1% a mi Iglesia
└── assets/
    ├── css/sitio.css       Toda la apariencia del sitio
    ├── js/sitio.js         Menú, categorías de pastorales y formulario
    └── img/                Logotipos e ícono de Adoración
```

Cada pantalla del prototipo es ahora **una página real con su propia
dirección**, como pedía el handoff. A las nueve del diseño se sumó **Avisos**,
que no estaba en el prototipo. Las tres pestañas de «Nuestra parroquia»
son tres páginas; las categorías de Pastorales viven en una sola página y se
pueden enlazar directamente (`pastorales.html#ministerios`).

## Ver el sitio

Doble clic en `sitio/index.html`. Se abre en el navegador y funciona completo,
sin servidor.

Para verlo como lo verá el público (con un servidor local):

```bash
python3 -m http.server 8123 --directory sitio
```

Y luego abrir `http://localhost:8123`.

## Publicarlo en internet

Cualquier hosting estático sirve. De más simple a más flexible:

1. **Netlify Drop** — entrar a `app.netlify.com/drop` y arrastrar la carpeta
   `sitio/`. Queda en línea en segundos, gratis y con HTTPS. Para actualizar,
   se arrastra de nuevo.
2. **Cloudflare Pages** o **GitHub Pages** — gratis, y se actualizan solos si el
   proyecto está en un repositorio de Git.
3. **Hosting propio** — subir el contenido de `sitio/` por FTP a la carpeta
   pública del servidor.

Después hay que apuntar el dominio de la parroquia al hosting elegido.

---

## Cómo editar el contenido

Los textos están dentro de los archivos `.html`. Se abren con cualquier editor
de texto plano (Visual Studio Code, Bloc de notas, TextEdit en modo texto).

### Publicar un aviso

Los avisos —cambios de horario, celebraciones especiales, inscripciones— van en
`avisos.html`. Ese archivo trae, justo antes de la lista, un comentario con las
instrucciones paso a paso: se copia un bloque `<article class="aviso">` completo,
se pega arriba de los demás y se cambian fecha, título y texto.

La portada muestra los **cuatro avisos más recientes** y los tiene copiados
aparte, así que un aviso importante conviene ponerlo en los dos archivos.

### Cambiar un horario o un dato de contacto

Buscar el texto tal como aparece en pantalla y reemplazarlo. **Ojo:** los datos
de contacto y el horario de Secretaría se repiten en varias páginas (barra
superior, cabecera y pie). Al cambiar uno, conviene buscar y reemplazar en las
11 páginas a la vez.

Datos que hoy se repiten en todas las páginas:

- `Av. Balmaceda 1596, La Serena`
- `+56 9 9280 3442` (y el enlace `tel:+56992803442`)
- `secretariaplourdes@gmail.com`
- `Secretaría: martes a sábado` / `10:00 a 13:00 y 16:00 a 19:00 hrs.`

### Completar la información pendiente

Todo lo que la parroquia aún no confirmó aparece marcado así:

```html
<span class="pendiente">[POR COMPLETAR]</span>
```

Para completarlo, se borra ese fragmento y se escribe el texto real. Por
ejemplo, los requisitos del Bautismo en `sacramentos.html`:

```html
<!-- antes -->
<p class="valor-dato"><span class="pendiente">[POR COMPLETAR]</span></p>

<!-- después -->
<p class="valor-dato">Certificado de nacimiento del niño o niña.</p>
```

Queda pendiente en: requisitos y documentos de los siete sacramentos,
descripción de Coronas de Caridad, descripciones y coordinadores de las capillas,
y las descripciones de los grupos que aún no las entregan.

### Reemplazar las fotografías

Las fotos son marcadores rayados con la medida indicada. Cada uno se ve así:

```html
<div class="foto" style="--alto:300px" aria-hidden="true">FOTO PRINCIPAL<br>Capilla Corpus Christi<br>460×300</div>
```

Se reemplaza el bloque completo por una imagen real, con su texto alternativo:

```html
<img class="capilla__foto" src="assets/img/capilla-corpus-christi.jpg"
     alt="Fachada de la Capilla Corpus Christi" width="460" height="300">
```

La imagen se guarda en `assets/img/`. Conviene exportarla al doble del tamaño
indicado (para pantallas retina) y comprimirla en JPG de buena calidad, para que
la página siga cargando rápido.

En el Hero de `index.html` y en la banda de la Patrona la foto es el fondo de la
sección; ahí se agrega en el CSS, en `.hero` y `.banda-patrona`, cambiando
`background: var(--rayado)` por la imagen.

### Cambiar colores o tipografías

Todo está en `assets/css/sitio.css`, en el bloque `:root` del comienzo. Cambiar
un color ahí lo cambia en todo el sitio.

---

## Conectar el formulario de certificados

Hoy el formulario **no envía nada**: al pulsar «Enviar solicitud» avisa en
pantalla que aún no está conectado y pide escribir o llamar a la Secretaría.
Es deliberado, para que ninguna solicitud se pierda en silencio.

Para conectarlo con el correo de la Secretaría, sin servidor propio:

1. Abrir `sitio/assets/js/sitio.js` y escribir la dirección del servicio en la
   línea del comienzo:

   ```js
   var ENDPOINT_CERTIFICADOS = "https://formsubmit.co/ajax/secretariaplourdes@gmail.com";
   ```

2. Publicar el sitio y enviar el formulario **una vez**.
3. Llegará un correo de confirmación a `secretariaplourdes@gmail.com`. Hay que
   abrirlo y pulsar el enlace de activación.

Desde ese momento cada solicitud llega a ese correo. FormSubmit es gratuito e
incluye protección antispam. Si más adelante se prefiere otro servicio
(Formspree, Web3Forms o un backend propio), basta cambiar esa misma línea: el
formulario envía todos los campos por `POST` y espera una respuesta correcta.

Para **desactivar** el formulario temporalmente, se vuelve a dejar la línea
vacía (`var ENDPOINT_CERTIFICADOS = "";`).

---

## Decisiones tomadas respecto del handoff

- **Versión móvil**: quedó pendiente en el diseño y se resolvió aquí sobre el
  mismo sistema visual — menú desplegable con acordeón, una sola columna,
  tarjetas apiladas, formulario a ancho completo y áreas táctiles de 56 px. Los
  quiebres están al final de `sitio.css`, comentados.
- **Botones «Ver ubicación» y «Cómo llegar»**: ahora abren Google Maps con la
  dirección de cada templo.
- **Teléfonos y correos**: son enlaces reales (`tel:` y `mailto:`), para que en
  el celular baste tocarlos.
- **Anclas de Capillas**: en el prototipo estaban puestas en lugares equivocados
  (el ancla de una capilla caía dentro de la ficha anterior). Aquí cada ficha
  tiene su propia ancla correcta.
- **Categoría «Música y expresión religiosa»**: no muestra la línea de
  inscripción, como indica el informe de contenidos.
- **Ancho completo**: el sitio ocupa toda la pantalla. El contenido se detiene
  en 1400px para que las líneas de texto sigan siendo legibles en monitores
  grandes; ese valor es la variable `--ancho-contenido`, al inicio de `sitio.css`.
- **Accesibilidad**: texto base de 17 px, jerarquía correcta de encabezados,
  enlace «Ir al contenido» para teclado, foco visible, etiquetas en todos los
  campos del formulario y textos alternativos en las imágenes.
- **Imágenes de marca**: se redujeron de 3,3 MB a unos 400 KB sin pérdida
  visible, y se generó el favicon a partir del sello oficial. El logotipo no se
  alteró en color ni en proporción.
- **Instagram**: la barra superior y el pie enlazan a
  `instagram.com/lourdes_laserena`, en pestaña nueva.
- **Crédito de autoría**: «Desarrollado por QworkLab» (enlace a `qworklab.cl`)
  cierra el pie, a la derecha de la línea de copyright. En el celular se apila
  bajo ella.

## Lo que falta

- **Fotografías reales** (ver más arriba).
- **Vigencia de los avisos**: hoy se agregan y se borran a mano, y hay que
  mantener sincronizada la portada con `avisos.html`. Si la parroquia empieza a
  publicar avisos seguido, este es el punto donde un CMS ligero empieza a rendir.
- **Página de Contacto** con mapa incrustado (hoy los datos viven en el Inicio,
  la barra superior y el pie).
- **Imagen para compartir enlaces**: cuando el sitio tenga dominio, agregar la
  etiqueta `og:image` que está indicada como comentario en el `<head>`.
- Confirmar el horario definitivo de Confesiones y de la Misa de San Carlo
  Acutis del día 12.
