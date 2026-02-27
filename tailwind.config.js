/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    // Breakpoints do Elementor usam max-width, mas Tailwind usa min-width.
    // Elementor cascade: base(desktop) → tablet(max-1024) → mobile(max-767)
    // Tailwind equivalente: default=mobile, md=768+, lg=1025+, xl=1367+
    screens: {
      'sm': '640px',
      'md': '768px',     // Acima de mobile (Elementor: max-width:767px abaixo disso)
      'lg': '1025px',    // Acima de tablet (Elementor: max-width:1024px abaixo disso)
      'xl': '1367px',    // Acima de laptop (Elementor: max-width:1366px abaixo disso)
    },
    extend: {
      // Cores extraídas do Elementor JSON — organizadas por uso semântico
      colors: {
        'brand': {
          'cream': '#F0E9DE',
          'cream-light': '#FEF4DF',
          'cream-warm': '#FCF9F2',
          'orange': '#FEB45D',
          'orange-dark': '#BB7D34',
          'gold': '#FDC37C',
          'green': '#2F9C5A',
          'green-dark': '#244030',
          'green-darker': '#1C3124',
          'pink': '#EE5862',
          'pink-dark': '#CA2566',
          'magenta': '#B93060',
        },
        'text': {
          'primary': '#1C1E20',
          'secondary': '#363435',
          'muted': '#2A3036',
          'dark-brown': '#7D3F0A',
          'white': '#FFFFFF',
        },
        'bg': {
          'white': '#FFFFFF',
          'off-white': '#F9F9F9',
          'light-gray': '#F5F5F5',
          'dark': '#272727',
        },
        'scrollbar-track': '#EFEFF0',
        'scrollbar-thumb': '#FEB45D',
      },
      fontFamily: {
        'factul': ['Factul', 'sans-serif'],
        'lato': ['Lato', 'sans-serif'],
        'mulish': ['Mulish', 'sans-serif'],
        'inter': ['Inter', 'sans-serif'],
        'sans': ['Factul', 'Lato', 'Mulish', 'system-ui', 'sans-serif'],
      },
      spacing: {
        '5p': '5%',
        '10p': '10%',
        '15p': '15%',
        '17p': '17%',
        '20p': '20%',
        '35p': '35%',
        '140p': '140%',
      },
      maxWidth: {
        'elementor': '1140px',
      },
    },
  },
  plugins: [],
}
