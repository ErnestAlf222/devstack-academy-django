/** @type {import('tailwindcss').Config} */

// Los colores leen variables CSS definidas en tailwind/input.css (:root).
// Así el modo oscuro (prefers-color-scheme) solo cambia las variables y las
// utilidades como bg-surface, text-ink o border-line se adaptan solas.
// "<alpha-value>" permite usar opacidad: bg-primary/15, border-line/60, etc.
const token = (name) => `rgb(var(--c-${name}) / <alpha-value>)`;

module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        bg: token('bg'),                    // fondo de página
        surface: token('surface'),          // tarjetas, header, sidebar
        surface2: token('surface2'),        // hover, campos, fondos sutiles
        line: token('line'),                // bordes finos (tarjetas)
        'line-strong': token('line-strong'),// bordes de inputs y botones ghost
        ink: token('ink'),                  // texto principal
        muted: token('muted'),              // texto secundario
        primary: token('primary'),          // acción principal (azul)
        'primary-strong': token('primary-strong'), // texto/enlaces azules (AA)
        'primary-soft': token('primary-soft'),     // fondos azul muy claro (#e8f0fe)
        'primary-tint': token('primary-tint'),     // tinte azul medio (#d2e3fc)
        'on-primary': token('on-primary'),  // texto sobre botón primario
        mint: token('mint'),                // acento secundario (iconos, estados)
        'mint-ink': token('mint-ink'),      // texto menta (AA)
        'mint-soft': token('mint-soft'),    // fondo menta suave
        'amber-soft': token('amber-soft'),  // fondo ámbar suave (chips, iconos)
        'amber-ink': token('amber-ink'),    // texto ámbar (AA)
        star: token('star'),                // estrellas de valoración
      },
      fontFamily: {
        sans: [
          '"Plus Jakarta Sans"',
          'system-ui',
          '-apple-system',
          '"Segoe UI"',
          'sans-serif',
        ],
      },
      transitionTimingFunction: {
        smooth: 'cubic-bezier(.22, .8, .3, 1)',
      },
      backgroundImage: {
        // Banner hero del dashboard: azul primario a azul profundo, sutil
        hero: 'linear-gradient(135deg, #1a73e8 0%, #1557b0 100%)',
      },
      boxShadow: {
        // Sombras de varias capas, definidas en :root (cambian en modo oscuro)
        card: 'var(--shadow-card)',
        'card-hover': 'var(--shadow-hover)',
        pop: 'var(--shadow-pop)',
      },
      keyframes: {
        rise: {
          '0%': { opacity: '0', transform: 'translateY(12px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
      animation: {
        // "backwards": aplica el estado inicial durante el delay y suelta el
        // transform al terminar, para que el hover (-translate-y) funcione.
        rise: 'rise .45s cubic-bezier(.22, .8, .3, 1) backwards',
      },
    },
  },
  plugins: [],
};
