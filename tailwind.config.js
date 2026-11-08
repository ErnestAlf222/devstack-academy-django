/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        bg: '#0b0a12',
        surface: '#14121f',
        surface2: '#1b1830',
        accent: '#a48fff',
        deep: '#1d1438',
        ink: '#f3f1fb',
        muted: '#b4aecb',
        star: '#f5c451',
      },
      fontFamily: {
        sans: ['Inter', 'Segoe UI', 'system-ui', '-apple-system', 'sans-serif'],
      },
      transitionTimingFunction: {
        smooth: 'cubic-bezier(.22, .8, .3, 1)',
      },
      boxShadow: {
        card: '0 10px 30px rgba(0, 0, 0, 0.35)',
        'card-hover':
          '0 22px 45px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(164, 143, 255, 0.25), 0 0 40px rgba(164, 143, 255, 0.18)',
      },
      backgroundImage: {
        glow: 'radial-gradient(900px 420px at 85% -10%, rgba(164, 143, 255, 0.14), transparent 60%)',
        'side-fade': 'linear-gradient(180deg, #100e1b 0%, #0b0a12 100%)',
      },
      keyframes: {
        rise: {
          '0%': { opacity: '0', transform: 'translateY(28px) scale(.97)' },
          '100%': { opacity: '1', transform: 'translateY(0) scale(1)' },
        },
      },
      animation: {
        // "backwards": aplica el estado inicial durante el delay y suelta el
        // transform al terminar, para que el hover (-translate-y-2) funcione.
        rise: 'rise .7s cubic-bezier(.22, .8, .3, 1) backwards',
      },
    },
  },
  plugins: [],
};
