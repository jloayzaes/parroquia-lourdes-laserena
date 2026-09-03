# Handoff: Sitio web · Parroquia Nuestra Señora de Lourdes (La Serena)

## Overview
Sitio web parroquial público para la **Parroquia Nuestra Señora de Lourdes**, Arquidiócesis de La Serena (Chile). El objetivo es que cualquier persona —con énfasis explícito en **adultos mayores y usuarios con poca experiencia digital**— encuentre en segundos: horarios de Misa, confesiones, atención de Secretaría, sacramentos, servicios, capillas, pastorales, cómo aportar (1% a mi Iglesia) y cómo contactar a la parroquia.

Alcance de esta entrega: **9 pantallas** de escritorio, navegables, con menú de 8 botones y desplegables. Falta la versión móvil (ver "Pendientes").

## About the Design Files
Los archivos de este paquete son **referencias de diseño construidas en HTML** — prototipos que muestran el aspecto y el comportamiento buscados, **no código de producción para copiar y pegar**.

La tarea es **recrear estos diseños en el entorno del proyecto destino** (WordPress + tema propio, React/Next.js, Astro, etc.) usando sus patrones, componentes y librerías establecidas. Si aún no existe un entorno, elegir el más adecuado; para una parroquia que debe editar sus propios contenidos, la recomendación es un **CMS simple** (WordPress o similar) con campos editables para horarios, avisos, fichas de pastorales, sacramentos y contactos, tal como pide el brief del cliente ("contenido editable por la parroquia, sin intervención técnica").

El prototipo está implementado como un componente único con estado local (una SPA de una sola página con conmutación de pantallas). En producción **cada pantalla debe ser una URL real** (`/`, `/nuestra-parroquia/historia`, `/horarios`, `/sacramentos`, `/servicios`, `/certificados`, `/capillas`, `/pastorales`, `/1-por-ciento`), con navegación por enlaces y anclas reales (`#sac-confesion`, etc.).

## Fidelity
**Alta fidelidad (hifi).** Colores, tipografía, escalas, espaciados, estados hover y comportamiento están definidos y validados con el cliente. Recrear la UI con precisión.

Excepciones deliberadas:
- **Todas las fotografías son marcadores** (fondo rayado diagonal + etiqueta monoespaciada con la medida). La parroquia entregará fotos en HD.
- Los datos que la parroquia aún no confirmó aparecen marcados literalmente como `[POR COMPLETAR]` en color `#8FA3BC`. Deben quedar como campos vacíos del CMS, no como texto fijo.

---

## Design Tokens

### Colores
| Rol | Hex | Uso |
|---|---|---|
| Azul parroquial (marca) | `#1B3A61` | Títulos, texto destacado, pie de página, overlay del hero |
| Azul medio | `#2C5F92` | Texto sobre celeste claro, enlaces, textos de botón invertido, "PARROQUIA"/"LA SERENA" del encabezado |
| Celeste (acento principal) | `#6E9CC9` | Barra superior, botones, íconos, antetítulos, ítem activo del menú |
| Celeste claro (fondo) | `#EAF3FA` | Portadas de sección, franjas, badges de ícono, recuadros de Secretaría |
| Celeste muy claro | `#F6FAFD` | Fondo de fichas desplegadas |
| Celeste claro sobre azul | `#BBD4EA` | Antetítulos e íconos dentro del pie azul |
| Texto cuerpo | `#54637a` | Párrafos |
| Texto secundario | `#5a6879` / `#6c7a90` | Datos, bajadas |
| Pendiente | `#8FA3BC` | `[POR COMPLETAR]`, etiquetas de foto |
| Bordes | `#E4EDF5` | Bordes de tarjeta y separadores |
| Borde de campo | `#CFDDEA` | Inputs y selects |
| Blanco | `#FFFFFF` | Fondo general |
| Texto del pie | `#C4D3E5` | Párrafos sobre azul |
| Crédito del pie | `#8FA7C4` | Línea de copyright |

Regla de marca del cliente: **azul parroquial `#1B3A61`, azul claro `#5C82AB`, blanco**. El celeste `#6E9CC9` es la variante aprobada en revisión ("más celeste, más acogedor") y reemplaza a `#5C82AB` en la interfaz.

### Tipografía
Una sola familia: **Montserrat** (Google Fonts), pesos 200, 300, 400, 500, 600, 700.

| Estilo | Valores |
|---|---|
| Hero (portada) | 200 · 58px · line-height 1.06 · dos líneas, la segunda en 600 |
| Título de sección (portada de página) | 200 · 46px · 1.12 · palabra final en 600 |
| Título grande interior | 200 · 34-42px · 1.2 |
| Título de ficha | 600 · 26px · 1.3 |
| Título de tarjeta | 600 · 20-21px · 1.35 |
| Párrafo | 400 · 18-19px · 1.7-1.8 |
| Dato / texto de tarjeta | 400 · 17px · 1.55-1.7 |
| Antetítulo (eyebrow) | 500-600 · 13px · letter-spacing .30em · mayúsculas · `#6E9CC9` |
| Etiqueta de dato | 600 · 12px · letter-spacing .14em · mayúsculas · `#6E9CC9` |
| Menú | 500 · 13px · letter-spacing .08em · mayúsculas (activo 700) |
| Sub-ítem de desplegable | 500 · 16px · 1.4 |
| Botón | 700 · 13-15px · letter-spacing .10em · mayúsculas |
| Barra superior | 500 · 13px · letter-spacing .07em |
| Etiqueta de foto (marcador) | 400 · 11-12px · monoespaciada · `#8FA3BC` |

Mínimo de cuerpo: **17px** (decisión de accesibilidad, no bajar). Contraste mínimo AA (4.5:1) obligatorio: por eso "PARROQUIA" y "LA SERENA" del encabezado usan `#2C5F92` y no gris claro.

### Espaciado y forma
- Ancho de página: **1180px** centrado; padding lateral interior **36px** (contenido útil 1108px).
- Ritmo vertical entre bloques: **56-72px**; interior de tarjeta: **26-36px**.
- Gaps de grilla: 20-24px (tarjetas), 40-56px (columnas mayores).
- **Sin border-radius** en tarjetas ni botones (esquinas rectas); solo círculos perfectos en los badges de ícono (`border-radius:50%`).
- Bordes de 1px `#E4EDF5`. Sombra del contenedor de página: `0 0 60px rgba(27,58,97,.14)`.
- Franja del menú: bordes superior e inferior 1px; ítem activo con `box-shadow: inset 0 -3px 0 #6E9CC9`.
- Badge de ícono: círculo `#6E9CC9` de 88px (tarjetas del inicio), 76px (Horarios/Certificados), 72px (1%), 64px (fichas), 52px (encabezado de categoría); glifo blanco al ~50-55% del diámetro.

### Íconos
**Phosphor Icons, peso Thin** (`@phosphor-icons/web@2.1.1`, `/src/thin/style.css`), blancos sobre círculo celeste.
`church` (Misas/templos), `hands-praying` (Confesiones/ministerios), `clock` (Secretaría), `calendar-dots` + `clock` juntos (horario del encabezado), `hand-heart` (aporte, unción, servicio y misión), `envelope-simple` (correo), `map-pin` (dirección), `phone` (teléfono), `instagram-logo`, `drop` (Bautismo), `wine` (Primera Comunión), `fire` (Confirmación, pastoral juvenil), `heart` (Matrimonio), `users-three` (catequesis adultos, catequesis y formación), `flower` (Coronas de Caridad, música), `calendar-dots` (fiesta patronal), `lightning` / `hammer` (destinos del 1%), `plus` / `minus` (acordeón), `caret-down` (selects), `check` (confirmación de envío).

**Excepción:** el ícono de **Adoración al Santísimo** es un PNG dibujado a medida (`assets/icono-adoracion.png`, 256×256, transparente): un **ostensorio** en trazo blanco delgado sobre círculo celeste (hostia, aro, 16 rayos alternados largo/corto, tallo con nudo, pedestal escalonado). Se muestra a 88px y 76px. En producción conviene convertirlo a **SVG** con `stroke-width` equivalente (~3.4/256) para que escale sin pérdida.

---

## Screens / Views

Menú global (8 botones, en mayúsculas): **Inicio · Nuestra parroquia · Horarios · Sacramentos · Servicios · Certificados · Capillas · Pastorales**.

Cabecera común (las tres filas se repiten en todas las pantallas):
1. **Barra superior** celeste `#6E9CC9`, alto mínimo 44px, texto blanco 13px: izquierda "Av. Balmaceda 1596, La Serena" + "+56 9 9280 3442"; derecha "secretariaplourdes@gmail.com" + "Instagram" con su logo.
2. **Fila de marca** (fondo blanco, padding 22px 36px): a la izquierda el dibujo del templo en azul oscuro (`assets/marca-navy.png`, 66px de alto) + divisor vertical 1px `#DCE7F1` + lockup en tres líneas — "PARROQUIA" (600/13px/.26em/`#2C5F92`), "Nuestra Señora de **Lourdes**" (300/24px, "Lourdes" en 700), "LA SERENA" (600/13px/.22em/`#2C5F92`); a la derecha el par de íconos calendario+reloj y el horario de Secretaría en dos líneas (400/15px).
3. **Franja de menú**: flex, gap 30px, ítems 17px arriba/abajo, `white-space:nowrap`, activo en `#6E9CC9` 700 con subrayado inset. Al pasar el cursor: color `#1B3A61` y engrosado óptico con `text-shadow:0 0 .6px #1B3A61,0 0 .6px #1B3A61` (**no** `font-weight`, para que no se mueva el layout).

Pie común (fondo `#1B3A61`, padding 56px 36px, grilla 1.3fr 1fr 1fr, gap 44px):
- Col. 1: dibujo del templo en blanco (`assets/marca-blanco.png`, 54px, opacidad .9) + lockup ("PARROQUIA" / "Nuestra Señora de **Lourdes**" / "LA SERENA") + "Comunidad de la Arquidiócesis de La Serena."
- Col. 2: "INFORMACIÓN DE CONTACTO" y cuatro filas con ícono `#BBD4EA` de 24px: dirección, teléfono, correo, horario de Secretaría.
- Col. 3: "REDES SOCIALES" → solo Instagram (con logo).
- Línea final sobre borde `rgba(255,255,255,.18)`: "© 2026 Parroquia Nuestra Señora de Lourdes · Arquidiócesis de La Serena".

### 1. Inicio
**Propósito:** responder en segundos cuándo hay Misa, cuándo hay confesiones, cómo contactar a la Secretaría y dónde queda la parroquia.

Bloques, en orden:
1. **Hero** 530px de alto: marcador de foto (1180×530) + overlay `linear-gradient(90deg, rgba(27,58,97,.84) 0%, rgba(44,95,146,.62) 46%, rgba(110,156,201,.12) 100%)`. Sobre él, alineado a la izquierda (max-width 700px): título **"Celebración" / "Santa Misa"** (200/58px, segunda línea en 600), luego "Martes a sábado · **19:00 hrs.**" y "Domingo · **11:00 hrs.**" (300/23px/1.75, horas en 600), y dos botones: **"VER TODOS LOS HORARIOS"** (fondo blanco, texto `#2C5F92`, 700/14px, padding 20px 28px → navega a Horarios) y **"CÓMO LLEGAR"** (borde 1px blanco 80%, texto blanco).
2. **Franja del 1%** (`#EAF3FA`, padding 30px 36px, space-between): "1% a mi Iglesia: **tu aporte sostiene la misión y la vida de nuestra comunidad**" (300/26px) + botón **"CONOCE MÁS"** (`#6E9CC9`, blanco, 700/14px) → navega a la página del 1%.
3. **Tres accesos prioritarios** (grilla 3 columnas, centrado, gap 36px, badges de 88px): **Horarios de Misa** (`church`; "Santa Misa: martes a sábado / 19:00 hrs. / Domingo 11:00 hrs."; el título navega a Horarios) · **Confesiones** (`hands-praying`; "Martes y viernes / 17:00 a 18:45 hrs. / En el templo parroquial") · **Secretaría parroquial** (`clock`; "Martes a sábado / 10:00 a 13:00 hrs. / 16:00 a 19:00 hrs.").
4. **Segundo bloque de tres** (mismo patrón): **Adoración al Santísimo** (ostensorio PNG; "Un espacio de encuentro y oración junto al Señor. / Lunes a viernes 10:00 a 19:00 hrs. / Sábado 09:00 a 19:00 hrs.") · **Aporta a tu Parroquia** (`hand-heart`; texto del 1% + enlace "Aporta a tu Parroquia" → página del 1%) · **Comunícate con nosotros** (`envelope-simple`; teléfono, correo, dirección).
5. **Banda de la patrona** 360px: marcador de foto + overlay `linear-gradient(180deg, rgba(27,58,97,.78), rgba(44,95,146,.68))`; centrado: antetítulo "NUESTRA PATRONA", título "Nuestra Señora de **Lourdes**" (200/42px), bajada y botón **"CONOCE SU HISTORIA"** (borde blanco) → abre Nuestra parroquia en la pestaña *Nuestra Patrona*.
6. **Noticias y avisos**: antetítulo "VIDA PARROQUIAL", título "Noticias y **avisos**" (200/38px) y grilla 2×2 de 4 avisos (marcador de foto 200×152 a la izquierda + fecha en `#6E9CC9` 600/13px + título 600/20px + resumen 400/17px). Botón centrado **"VER MÁS NOTICIAS"**. Contenido de ejemplo: Adoración al Santísimo (días y horario), catequesis familiar 2026, Club Adulto Mayor, Misioneros del 1%.
7. **Dónde celebramos**: antetítulo, título "Parroquia, capillas y **santuario**", bajada "Además de la parroquia matriz, seis lugares de celebración en nuestro territorio." y grilla de 3×2 fichas con borde: nombre (600/18px) y dos filas con ícono `map-pin` (dirección) y `church` ("Santa Misa: …"), más enlace "VER UBICACIÓN →".

### 2. Nuestra parroquia (3 sub-páginas)
Portada de sección + **fila de pestañas** (borde inferior 1px; ítem activo `#1B3A61` 700 con subrayado inset `#6E9CC9`; 15px/.06em/mayúsculas): **Nuestra historia · Nuestra Patrona · Sacerdotes**. Cada pestaña es una página distinta (en producción, tres URLs) y el desplegable del menú entra directo a cada una.

**2.1 Nuestra historia** — dos marcadores de foto lado a lado (554×340: "el templo en los años 80" y "el templo hoy, mismo ángulo"); luego grilla `300px 1fr` con gap 56px: a la izquierda antetítulo, título "Más de seis décadas **de comunidad**" y una **línea de tiempo** (1958 primera piedra · 11 de mayo de 1961 fundación de la parroquia · 2011 cincuenta años · 2014 primera Capilla de Adoración Perpetua de la Arquidiócesis · 2025 sede de la Jornada Nacional de la Juventud); a la derecha los **siete párrafos** del texto histórico entregado por la parroquia (400/19px/1.8, max-width 74ch).

**2.2 Nuestra Patrona** — grilla `440px 1fr`: izquierda, marcador de foto de la gruta (440×420) y recuadro `#EAF3FA` con ícono `calendar-dots` + "DÍA DE CELEBRACIÓN / 11 de febrero"; derecha, antetítulo, título "Nuestra Señora de **Lourdes**", los párrafos del texto, la cita **«Yo soy la Inmaculada Concepción»** (300/30px con borde izquierdo 3px `#6E9CC9`, más su atribución 400/16px) y el cierre en **cursiva** 400/19px centrado sobre borde superior: "Nuestra Señora de Lourdes, **ruega por nosotros**".

**2.3 Sacerdotes** — antetítulo "PERSONAS A SU SERVICIO", título "Nuestros **sacerdotes**" y tres fichas (marcador de foto 356×300 + cargo en antetítulo + nombre 600/21px): **Pbro. Ariel Roldán Díaz** (Párroco) · **Pbro. Juan Carlos Álvarez S.** (Vicario parroquial, con la nota "Párroco de Nuestra Señora de las Mercedes de La Higuera") · **Pbro. Marcelo Gálvez Húmeres** (Vicario parroquial).

### 3. Horarios · "Celebración de la Santa Misa"
Portada de sección + grilla de 2 columnas con **7 tarjetas por templo**. La **parroquia matriz** ocupa las dos columnas (`grid-column: span 2`, borde `#6E9CC9`, foto 1108×210) e incluye el bloque **"CELEBRACIONES ESPECIALES"**: miércoles por los enfermos · jueves por las vocaciones · sábado por los niños y jóvenes · día 12 de cada mes Misa de San Carlo Acutis (en el horario del día que corresponda). Cada tarjeta lleva foto (542×170), nombre, dirección, bloque "SANTA MISA" con ícono `church` y horario (400/19px), y botones "VER UBICACIÓN" (borde `#6E9CC9`) y "CONOCER ESTA COMUNIDAD →" (que navega a Capillas).

Al final, tres tarjetas `#EAF3FA` con badge de 76px: **Confesiones** (martes y viernes 17:00 a 18:45, en el templo; "Fuera de ese horario, consulta en Secretaría") · **Adoración al Santísimo** (lunes a viernes 10:00-19:00, sábado 09:00-19:00) · **Secretaría parroquial** (martes a sábado, 10:00-13:00 y 16:00-19:00, +56 9 9280 3442).

**Datos de los siete templos** (dirección · Santa Misa), todos en La Serena:
| Templo | Dirección | Santa Misa |
|---|---|---|
| Parroquia Nuestra Señora de Lourdes | Av. Balmaceda 1596 | Martes a sábado 19:00 · Domingo 11:00 |
| Santuario Santa Teresa de los Andes | Av. Balmaceda 2774 | Domingo 11:00 |
| Capilla Sagrado Corazón de Jesús y María | La Colina 1674 | Sábado 17:30 |
| Capilla San Joaquín y Santa Ana | Alberto Arenas esq. Ernesto Molina Garmendia | Sábado 17:30 |
| Capilla Jesús de la Misericordia | Av. Guillermo Ulriksen 1771 | Domingo 12:30 |
| Capilla Corpus Christi | Av. Gabriel González Videla con Julio Díaz | Sábado 19:00 |
| Capilla Santiago Apóstol | Aguirre Valín con 1 de mayo | Domingo 09:30 |

### 4. Sacramentos
Portada de sección + **siete fichas completas apiladas** (sin clics: toda la información visible), alternando la foto a izquierda/derecha (columna de 360px que se estira al alto de la ficha con `align-self:stretch` + `min-height:340px`). Cada ficha: badge de 64px, título 600/26px, descripción 400/18px (max 62ch) y grilla 2×2 de datos — **Destinatarios · Requisitos · Documentos necesarios · Inscripción**.

Orden e íconos: **Bautismo** (`drop`) · **Primera Comunión** (`wine`) · **Confirmación** (`fire`) · **Matrimonio** (`heart`) · **Unción de los Enfermos** (`hand-heart`, etiqueta **"Solicitud y coordinación"** en vez de "Inscripción", con teléfono directo) · **Confesión** (`hands-praying`, etiqueta **"Horario habitual"**: martes y viernes 17:00 a 18:45 en el templo, sin inscripción previa) · **Catequesis adultos** (`users-three`, subtítulo "Camino de formación e iniciación cristiana"; aclara que sus requisitos son distintos de la Confirmación juvenil).

Requisitos y documentos: `[POR COMPLETAR]` en todas las fichas. Cierre: franja `#EAF3FA` "Inscripciones y **consultas**" con los datos de Secretaría.

Anclas para el desplegable: `sac-bautismo`, `sac-primera-comunion`, `sac-confirmacion`, `sac-matrimonio`, `sac-uncion`, `sac-confesion`, `sac-catequesis-adultos`.

### 5. Servicios
Portada de sección + tres fichas con foto lateral alternada:
- **Funerales y velatorios** (`church`): la parroquia acompaña a las familias y coordina las exequias; recuadro `#EAF3FA` "COORDINACIÓN EN SECRETARÍA PARROQUIAL" con horario, dirección, teléfono y correo. Requisitos `[POR COMPLETAR]`.
- **Intenciones de Misa** (`hands-praying`): se inscriben directamente antes de la celebración, sin trámite previo; grilla 2×2 — Miércoles (por los enfermos) · Otros días (por los difuntos) · Aporte (voluntario) · Dónde (antes de la Santa Misa). **No** remite a Secretaría.
- **Coronas de Caridad** (`flower`): qué son y cómo se solicitan, ambos `[POR COMPLETAR]`.

Anclas: `ser-funerales`, `ser-intenciones`, `ser-coronas`.

### 6. Solicitar certificados
Portada de sección + grilla `1fr 380px`.

Formulario en **tres bloques numerados** (círculo `#EAF3FA` de 38px con el número en `#2C5F92` 700/17px + título 600/22px; campos en grilla de 2 columnas, gap 22/24px):
1. **Datos del solicitante**: Nombre completo · RUT · Teléfono · Correo electrónico.
2. **Certificado solicitado**: `<select>` "¿Qué certificado necesita?" → Bautismo · Primera Comunión · Confirmación · Matrimonio.
3. **Datos de la persona que recibió el sacramento**: Nombre completo · RUT · Fecha de nacimiento · Fecha del sacramento · `<select>` "¿Dónde se celebró el sacramento?" (la parroquia, el santuario y las cinco capillas; **sin** opción "otra parroquia") · campo libre "Información que ayude a la búsqueda (opcional)".

Campos: `min-height:56px`, padding 16px, borde 1px `#CFDDEA`, texto 400/18px; label 600/15px `#1B3A61`; foco → borde `#6E9CC9`. Luego casilla de privacidad sobre fondo `#EAF3FA` ("Autorizo el uso de estos datos únicamente para gestionar mi solicitud de certificado") y botón **"ENVIAR SOLICITUD"** (`#6E9CC9`, 700/15px, padding 23px 34px) con la nota "Responderemos al correo indicado".

Columna derecha: ficha con badge `clock` — horario de Secretaría, dirección, teléfono, correo y la nota de que también puede solicitarse presencialmente.

**Estado de éxito** (reemplaza el formulario): badge `check` de 96px, "Solicitud **enviada**" (200/40px), explicación de que la solicitud llegó al correo de Secretaría y que se revisarán los libros parroquiales, recuadro `#EAF3FA` con teléfono/correo/horario y botón "VOLVER AL INICIO".

**Backend:** el envío debe llegar al correo **secretariaplourdes@gmail.com**, con acuse de recepción al solicitante, protección antispam y posibilidad de desactivar el formulario desde el administrador.

### 7. Capillas y Santuario
Portada de sección + **seis fichas** (santuario y cinco capillas) en filas alternadas: marcador de foto 460×300 a un lado y, al otro, nombre 600/26px, descripción `[POR COMPLETAR]`, grilla 2×2 de datos (**Dirección · Santa Misa · Coordinador/a · Horario de atención**, los dos últimos `[POR COMPLETAR]`) y botón **"VER UBICACIÓN"** (`#6E9CC9`). Cada fila se separa con borde inferior 1px.

Anclas: `cap-santuario`, `cap-sagrado-corazon`, `cap-san-joaquin`, `cap-misericordia`, `cap-corpus`, `cap-santiago`.

### 8. Pastorales y grupos
Portada de sección + grilla `308px 1fr` con gap 40px.

- **Índice lateral fijo** (`position:sticky; top:20px`, borde 1px): encabezado "CATEGORÍAS" y cinco filas (nombre 500/16px + número de grupos); la activa con fondo `#EAF3FA`, peso 700 y `box-shadow: inset 3px 0 0 #6E9CC9`.
- **Panel derecho**: encabezado de la categoría (badge 68px + título 200/34px + bajada con el total de grupos) y **tarjetas de grupo en dos columnas** (borde 1px, padding 26/28px): nombre 600/20px, descripción 400/17px y, sobre borde superior, el dato **Coordinador/a** (única ficha de datos; se eliminaron "Día, horario y lugar" y "Actividades").
- Al final del panel, con **el mismo ancho que la columna de tarjetas**, franja `#EAF3FA` (padding 26/28px, dos columnas): "¿Quieres ser parte de alguno de nuestros grupos?" (600/20px) + aviso de inscripciones en Secretaría de martes a sábado + datos de contacto (400/17px).

**Categorías y grupos (29 en total):**
1. **Catequesis y formación** (5): Catequesis bautismal · Catequesis de niños · Primera Comunión · Catequesis de Confirmación · Catequesis matrimonial · Catequesis adultos.
2. **Pastoral juvenil y vocacional** (3): Pastoral Juvenil KERYGMA · Pastoral Prejuvenil KAIROS · Pastoral de Acólitos San Carlo Acutis.
3. **Ministerios y espiritualidad** (8): Comunidad de Ministros Mandatados · Comunidad de Adoradores · Cursillo de Cristiandad · Renovación Carismática · Legión de María «María Madre del Salvador» · Taller de Oración Ignacio Larrañaga · Pastoral de Liturgia · Comunidad Waldo Alcalde.
4. **Servicio y misión** (6): Misioneros del 1% · Pastoral Social Santa Marta · Pastoral de Migrantes · Pastoral de Servidores · Pastoral de Redes Sociales · Club Adulto Mayor «Amanecer de Lourdes».
5. **Música y expresión religiosa** (7): Coro Aguinaldito (venezolano) · Coro Santa Bernardita · Coro de Pastoral Juvenil · Coro Matrimonio Rodríguez Gallardo · Coro Patricio Pastén · Solista Pilar Ángel · Baile Religioso Toba Guerreros de Dios. **Esta categoría no muestra línea de inscripción** (solo información).

**Contenido ya redactado** (el resto `[POR COMPLETAR]`): descripciones de Catequesis de Confirmación, Catequesis adultos, Catequesis de niños · Primera Comunión, Pastoral de Migrantes y Pastoral de Redes Sociales. Coordinadores confirmados, con la etiqueta **"Matrimonio coordinador"** en vez de "Coordinador/a": Pastoral de Migrantes → *Yxora Vacaro y Francisco Herrera*; Pastoral de Redes Sociales → *Jimena Ceballos y Joaquín Loayza*.

### 9. 1% a mi Iglesia
Cuatro bloques:
1. **Encabezado potente**: fondo `#1B3A61` con textura diagonal sutil (`repeating-linear-gradient(135deg, rgba(255,255,255,.05) 0 12px, rgba(255,255,255,0) 12px 24px)`), antetítulo "APORTA A TU PARROQUIA", título "1% a mi **Iglesia**" (200/56px), bajada "Un pequeño gesto que sostiene una gran misión." (300/24px) y botón blanco **"INSCRIBIRME AL 1%"** → `https://forms.gle/hzTBrMmzRcHZa6Zp8` (abre en pestaña nueva).
2. **Explicación breve** (grilla 1fr 1fr): dos párrafos (invitación libre y voluntaria; el 1% como referencia, sin monto obligatorio) y, al lado, recuadro `#EAF3FA` 300/26px: "Cada aporte, grande o pequeño, nos ayuda a seguir construyendo **una parroquia viva, acogedora y al servicio de toda la comunidad.**"
3. **"Tu aporte nos ayuda a"**: cuatro columnas con badge de 72px — mantener la parroquia y sus capillas (`church`) · cubrir gastos de funcionamiento como agua, luz y otros servicios (`lightning`) · realizar reparaciones y mantenciones (`hammer`) · sostener durante todo el año la labor pastoral y evangelizadora (`users-three`).
4. **Dos tarjetas lado a lado**: **Inscríbete** (borde 1px; inscripción online con el botón al formulario; inscripción presencial en Secretaría con su horario) y **Datos de transferencia** (fondo `#EAF3FA`; tabla sobre blanco — Destinatario: Parroquia Nuestra Sra. de Lourdes · Banco: BancoEstado · Tipo de cuenta: Cuenta corriente · N.º de cuenta: **12800002921** · Correo: **miunoporciento.plourdes@gmail.com**; y el aviso "En el asunto o comentario escribe **uno por ciento + tu nombre y apellido**. Ejemplo: uno por ciento María González").

---

## Interactions & Behavior
- **Menú**: clic en un botón cambia de pantalla y sube al inicio de la página. El ítem activo se marca en `#6E9CC9` 700 con subrayado inset.
- **Desplegables**: se abren al **hover** sobre el botón del menú (`onMouseEnter` / `onMouseLeave`), panel absoluto bajo el ítem (min-width 260px, fondo blanco, borde 1px `#E4EDF5`, sombra `0 20px 44px rgba(27,58,97,.18)`, padding vertical 8px, z-index 30). Los dos últimos ítems (Capillas, Pastorales) alinean el panel a la derecha para no salirse del ancho.
  - Tienen desplegable: Nuestra parroquia (3), Sacramentos (7), Servicios (3), Capillas (6), Pastorales (5). **Inicio, Horarios y Certificados no tienen.**
  - Al elegir un sub-ítem: Nuestra parroquia cambia de **sub-página**; Pastorales selecciona la **categoría** del índice; Sacramentos, Servicios y Capillas navegan y **desplazan hasta el ancla** correspondiente.
- **Hover de texto sin salto**: tanto en el menú como en los desplegables el marcado usa color + `text-shadow` doble (engrosado óptico). Nunca cambiar `font-weight` en hover: mueve el layout.
- **Desplazamiento a ancla**: en el prototipo se implementó con un bucle de `requestAnimationFrame` que **recalcula el destino en cada cuadro** (`getBoundingClientRect().top + scrollY - 24`) y se acerca por interpolación, terminando cuando el delta es < 2px en tres cuadros seguidos o a los 1400 ms. Motivo: al cambiar de pantalla el layout aún no está estable y una medición única deja el scroll en el lugar equivocado; además `scrollTo({behavior:'smooth'})` no funcionó en el entorno de previsualización. En producción, con URLs y anclas reales, basta `scroll-margin-top: 24px` + navegación nativa por hash.
- **Formulario de certificados**: campos e input reales; "Enviar solicitud" muestra el estado de éxito; volver al inicio lo reinicia.
- **Pestañas de Nuestra parroquia**: cambian de sub-página y suben al inicio.
- **CTA cruzados**: "Ver todos los horarios" y el título "Horarios de Misa" → Horarios; "Conocer esta comunidad" → Capillas; "Conoce más" (franja del 1%) y la tarjeta "Aporta a tu Parroquia" → 1% a mi Iglesia; "Conoce su historia" → Nuestra parroquia / Nuestra Patrona; el logotipo → Inicio.
- **Sin animaciones decorativas.** Transiciones: solo el desplazamiento a anclas.

## State Management
Estado del prototipo (una SPA con estado local):
| Estado | Valores | Efecto |
|---|---|---|
| `pantalla` | inicio · parroquia · horarios · sacramentos · servicios · certificados · capillas · pastorales · unopor | Pantalla visible |
| `subParroquia` | historia · patrona · sacerdotes | Sub-página de Nuestra parroquia |
| `catPastoral` | catequesis · juvenil · ministerios · servicio · musica | Categoría del índice de Pastorales |
| `menuAbierto` | id del botón o null | Panel desplegable visible |
| `enviado` | boolean | Formulario vs. estado de éxito en Certificados |

En producción, `pantalla` y `subParroquia` deben ser **rutas**; `catPastoral` puede ser ruta o parámetro (`/pastorales/ministerios`); `menuAbierto` y `enviado` son estado de UI local.

**Contenido que debe ser editable desde el CMS** (requerimiento explícito del cliente): horarios de Misa, confesiones, adoración y secretaría; avisos y noticias con fecha de vigencia; fichas de capillas y santuario (foto, descripción, dirección, coordinador, horarios); fichas de sacramentos (requisitos, documentos, inscripción); fichas de pastorales (descripción y coordinador); textos de historia y patrona; datos de contacto y de transferencia.

## Assets
En `assets/` (todos derivados del logotipo oficial que entregó la parroquia):
| Archivo | Qué es | Uso |
|---|---|---|
| `logo-horizontal.png` | Logotipo oficial completo (1400×809), fondo blanco | Referencia; no se usa en la maqueta final |
| `logo-sello.png` | Sello circular oficial (1400×1354) | Referencia / favicon |
| `marca-navy.png` | Dibujo del templo aislado, azul `#1B3A61`, **transparente** (1162×483) | Encabezado |
| `marca-celeste.png` | Igual, celeste `#5C82AB` | Variante |
| `marca-blanco.png` | Igual, blanco | Pie de página |
| `icono-adoracion.png` | Ostensorio en trazo delgado sobre círculo celeste (256×256, transparente) | Adoración al Santísimo |

Regla del cliente: **usar el logotipo tal como está** — sin cambiar sus colores, sin estirarlo, sin efectos, con espacio libre alrededor. Los archivos `marca-*.png` son recortes del dibujo del templo recoloreados a los colores de la marca, aprobados en revisión; el logotipo completo no debe alterarse.

Fuentes externas: Google Fonts (Montserrat) y `@phosphor-icons/web@2.1.1` (peso Thin) por CDN. En producción conviene **autoalojar** ambos.

## Accesibilidad (requisito del cliente, no opcional)
- Texto base cómodo (17px mínimo) y ampliable sin pérdida de contenido.
- Contraste AA (4.5:1) en todo texto pequeño; no comunicar estados solo con color.
- Botones grandes y separados, con nombres explícitos; en móvil, área táctil mínima de 44px.
- Jerarquía correcta de encabezados y texto alternativo en toda imagen informativa.
- Formularios con etiquetas visibles, ejemplos y mensajes de error comprensibles.
- Probar con adultos mayores antes de publicar.

## Pendientes
- **Versión móvil**: es el principal medio de consulta del público y aún no está diseñada. Definir menú hamburguesa/acordeón, hero de una columna, tarjetas apiladas, índice de Pastorales colapsable y campos de formulario a ancho completo.
- Fotografías reales en HD (parroquia, capillas, santuario, sacerdotes, grupos, gruta, dos tomas históricas del templo).
- Requisitos y documentos de cada sacramento; coordinadores y horarios de las capillas; descripciones de los grupos restantes; datos de Coronas de Caridad.
- Confirmar horario definitivo de Confesiones y de la Misa de San Carlo Acutis del día 12.
- Página de Contacto con mapa interactivo y botones "Llamar" / "Escribir" / "Cómo llegar" (hoy los datos viven en el inicio y en el pie).
- Sistema de noticias con fecha de vigencia y despublicación automática.

## Files
- `Maqueta Parroquia Lourdes.dc.html` — **la maqueta navegable completa** (las 9 pantallas, el menú con desplegables y el formulario). Referencia principal.
- `support.js` — runtime del entorno de prototipado (necesario solo para abrir el HTML; **no se migra**).
- `assets/` — logotipos e ícono descritos arriba.
- `Sitio Parroquia Lourdes.dc.html` — lienzo con las exploraciones de estilo iniciales (turnos descartados y el turno aprobado). Útil solo como historial de decisiones.

Los documentos de origen del cliente (informe de contenidos, estructura de navegación, textos de historia y del 1%) están en `uploads/` del proyecto.
