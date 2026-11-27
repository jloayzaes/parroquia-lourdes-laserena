# Tipografía del sitio web · Parroquia Nuestra Señora de Lourdes

> Instrucciones para Claude Code. Decisión tomada el 26 de noviembre de 2026: el sitio usa **Nunito Sans como única familia tipográfica**, en la línea de Vatican News (que usa Museo Sans, de pago; Nunito Sans es su equivalente libre). Este archivo reemplaza a Montserrat **solo en el sitio web**. Colores, composición y tono siguen el *Manual de identidad visual v1.0*.

## 1. Regla principal

- Una sola familia: **Nunito Sans** (Google Fonts, licencia OFL, gratuita).
- El contraste lo da el **grosor**, no otra fuente: los títulos van en 300 con una palabra clave en 700, y los antetítulos en 600 con espaciado amplio.
- Grosores que se cargan: **300, 400, 600 y 700**. No cargar otros.
- **Excepción:** el logotipo es siempre la imagen SVG oficial (símbolo + nombre). Nunca se reescribe el nombre de la parroquia en Nunito Sans ni en otra fuente como sustituto del logo.

## 2. Carga de la fuente (Next.js 15, App Router)

Usar `next/font/google`, que aloja la fuente en el propio sitio (sin peticiones a Google desde el navegador y sin saltos de diseño al cargar).

```tsx
// app/fonts.ts
import { Nunito_Sans } from "next/font/google";

export const nunitoSans = Nunito_Sans({
  subsets: ["latin", "latin-ext"],
  weight: ["300", "400", "600", "700"],
  style: ["normal", "italic"],
  display: "swap",
  variable: "--font-nunito-sans",
});
```

```tsx
// app/layout.tsx
import { nunitoSans } from "./fonts";
import "./globals.css";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es-CL" className={nunitoSans.variable}>
      <body className="font-sans text-texto bg-white antialiased">{children}</body>
    </html>
  );
}
```

## 3. Tokens en Tailwind

### Tailwind v4 (`globals.css`)

```css
@import "tailwindcss";

@theme {
  --font-sans: var(--font-nunito-sans), system-ui, -apple-system, "Segoe UI", sans-serif;

  /* Paleta del manual */
  --color-navy: #1B3A61;
  --color-celeste: #6E9CC9;
  --color-azul-medio: #5C82AB;
  --color-gris-azulado: #8FA3BC;
  --color-celeste-palido: #EAF3FA;
  --color-gris-fondo: #E9EDF2;
  --color-linea: #E4EDF5;
  --color-texto: #44536B;

  /* Escala tipográfica */
  --text-antetitulo: 0.8125rem;   /* 13px */
  --text-dato: 0.875rem;          /* 14px */
  --text-cuerpo: 1.125rem;        /* 18px */
  --text-tarjeta: 1.3125rem;      /* 21px */
  --text-seccion: 2rem;           /* 32px */
  --text-titulo: 2.75rem;         /* 44px */

  --radius: 0;                    /* esquinas rectas en todo el sitio */
}

/* Números siempre alineados: horarios, fechas, teléfonos */
body { font-variant-numeric: lining-nums tabular-nums; }
```

### Tailwind v3 (si el proyecto aún usa `tailwind.config.ts`)

```ts
import type { Config } from "tailwindcss";
import { fontFamily } from "tailwindcss/defaultTheme";

export default {
  theme: {
    extend: {
      fontFamily: { sans: ["var(--font-nunito-sans)", ...fontFamily.sans] },
      colors: {
        navy: "#1B3A61", celeste: "#6E9CC9", "azul-medio": "#5C82AB",
        "gris-azulado": "#8FA3BC", "celeste-palido": "#EAF3FA",
        "gris-fondo": "#E9EDF2", linea: "#E4EDF5", texto: "#44536B",
      },
      borderRadius: { DEFAULT: "0", none: "0" },
    },
  },
} satisfies Config;
```

## 4. Jerarquía tipográfica

| Nivel | Grosor | Tamaño escritorio / móvil | Interlineado | Detalle |
|---|---|---|---|---|
| Antetítulo | 600 | 13 px / 12 px | 1.4 | MAYÚSCULAS, `tracking-[.25em]`, color celeste |
| Título mayor (portada) | 300, palabra clave en 700 | 44 px / 32 px | 1.1 | Navy, `text-balance`, `tracking-[-0.01em]` |
| Título de sección | 300 | 32 px / 26 px | 1.2 | Navy |
| Título de tarjeta / subtítulo | 700 | 21 px / 19 px | 1.25 | Navy |
| Cuerpo | 400 | 18 px / 17 px | 1.65 | Color `#44536B`, máximo ~70 caracteres por línea (`max-w-[65ch]`) |
| Dato / etiqueta (horarios, direcciones, menú) | 600 | 14 px / 14 px | 1.4 | Navy o azul medio |
| Cifra destacada (hora de misa) | 600 | 24 px / 22 px | 1.1 | Navy, `whitespace-nowrap` |
| Nota / texto secundario | 400 | 13 px / 13 px | 1.5 | `#5C6F8A` (no usar `#8FA3BC` sobre blanco para texto: no alcanza contraste 4.5:1) |
| Cita bíblica | 300 itálica | 20 px / 18 px | 1.35 | Navy; referencia en 600, 14 px |
| Botón | 600 | 14 px | 1 | Sin mayúsculas, sin bordes redondeados, área mínima 44 px de alto |

## 5. Componentes de texto (clases sugeridas)

Crear estos componentes en `components/typography/` para que nadie tenga que recordar la escala:

```tsx
// components/typography/index.tsx
import { cn } from "@/lib/utils";

export const Antetitulo = ({ className, ...p }: React.HTMLAttributes<HTMLParagraphElement>) => (
  <p className={cn("text-[12px] md:text-antetitulo font-semibold uppercase tracking-[.25em] text-celeste", className)} {...p} />
);

export const TituloMayor = ({ className, ...p }: React.HTMLAttributes<HTMLHeadingElement>) => (
  <h1 className={cn("text-[32px] md:text-titulo font-light leading-[1.1] tracking-[-0.01em] text-navy text-balance [&_strong]:font-bold", className)} {...p} />
);

export const TituloSeccion = ({ className, ...p }: React.HTMLAttributes<HTMLHeadingElement>) => (
  <h2 className={cn("text-[26px] md:text-seccion font-light leading-[1.2] text-navy text-balance", className)} {...p} />
);

export const TituloTarjeta = ({ className, ...p }: React.HTMLAttributes<HTMLHeadingElement>) => (
  <h3 className={cn("text-[19px] md:text-tarjeta font-bold leading-[1.25] text-navy", className)} {...p} />
);

export const Parrafo = ({ className, ...p }: React.HTMLAttributes<HTMLParagraphElement>) => (
  <p className={cn("text-[17px] md:text-cuerpo leading-[1.65] text-texto max-w-[65ch]", className)} {...p} />
);

export const Dato = ({ className, ...p }: React.HTMLAttributes<HTMLSpanElement>) => (
  <span className={cn("text-dato font-semibold text-navy whitespace-nowrap", className)} {...p} />
);
```

Uso de la palabra clave en el título:

```tsx
<Antetitulo>Bienvenidos</Antetitulo>
<TituloMayor>Una comunidad de <strong>fe</strong> al servicio de La Serena</TituloMayor>
```

## 6. Reglas que se deben respetar

1. **Ritmo de cada bloque:** antetítulo celeste → título liviano → párrafo → dato o llamada a la acción.
2. **Sin otras fuentes.** No agregar serif, script ni fuentes decorativas. Si algún día se quiere un toque solemne, se decide aparte y se actualiza este archivo.
3. **Sin mayúsculas sostenidas** fuera del antetítulo. Botones, menús y títulos van en minúsculas normales.
4. **Sin grosores 800/900** ni cursivas fuera de las citas bíblicas.
5. **Esquinas rectas** en tarjetas, botones, campos e imágenes. Separaciones con líneas de 1 px `#E4EDF5`.
6. **Íconos** de trazo fino (Phosphor, variante Thin) en celeste. Nunca emoji.
7. **Información práctica completa y en orden:** día, hora, lugar. Ejemplo: «Domingo 14 de diciembre, 11:00 hrs., en el templo parroquial.»
8. **Contraste:** todo texto sobre blanco debe cumplir 4.5:1 (navy, `#44536B` y `#5C6F8A` cumplen; celeste `#6E9CC9` solo en antetítulos e íconos, nunca para párrafos).

## 7. Datos fijos para el pie de página

```
Parroquia Nuestra Señora de Lourdes · Arquidiócesis de La Serena
Av. Balmaceda 1596, La Serena · +56 9 9280 3442 · secretariaplourdes@gmail.com
Secretaría: martes a sábado, 10:00 a 13:00 y 16:00 a 19:00 hrs.
```

## 8. Lista de verificación antes de dar por terminada una página

- [ ] Solo se carga Nunito Sans (revisar la pestaña Network: ninguna otra fuente).
- [ ] Los títulos usan 300 y la palabra clave 700; ningún título en 400.
- [ ] Los horarios usan números alineados y no se cortan en dos líneas.
- [ ] Ningún párrafo supera ~70 caracteres por línea en escritorio.
- [ ] En 360 px de ancho no hay desbordes horizontales y el menú se apila.
- [ ] Ningún elemento tiene `rounded-*` distinto de `rounded-none`.
- [ ] El logo es la imagen SVG oficial, no texto.
