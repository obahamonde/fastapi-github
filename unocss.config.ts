import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup,
} from 'unocss'

export default defineConfig({
  shortcuts: [
    ['scale', 'hover:scale-110 hover:transition-all duration-200 ease-in-out'],
    ['cp', 'cursor-pointer'],
    ['rf', 'rounded-full'],
    ['col', 'flex flex-col'],
    ['row', 'flex flex-row'],
    ['center', 'items-center justify-center'],
    ['start', 'items-start justify-start'],
    ['end', 'items-end justify-end'],
    ['tr', 'top-0 right-0'],
    ['br', 'bottom-0 right-0'],
    ['bl', 'bottom-0 left-0'],
    ['tl', 'top-0 left-0'],
    ['sh-sm', 'shadow-sm'],
    ['sh-md', 'shadow-md'],
    ['sh-lg', 'shadow-lg'],
    ['sh-xl', 'shadow-xl'],
    ['sh-2xl', 'shadow-2xl'],
    ['scale', 'hover:scale-110 hover:transition-all duration-200 ease-in-out'],
    ['grid2', 'grid grid-cols-2'],
    ['grid3', 'grid grid-cols-3'],
    ['grid4', 'grid grid-cols-4'],
    ['grid5', 'grid grid-cols-5'],
    ['grid6', 'grid grid-cols-6'],
    ['btn-get', 'bg-secondary text-light hover:bg-accent hover:text-warning shadow-accent hover:shadow-light shadow-md px-4 py-2'],
    ['btn-get', 'bg-warning text-secondary shadow-info hover:bg-success hover:text-secondary hover:shadow-light shadow-md px-4 py-2'],
    ['btn-del', 'bg-danger text-white shadow-warning hover:bg-warning hover:text-white hover:shadow-danger shadow-md px-2 py-1'],
    ['btn-circle', 'rf p-1 m-1 cp scale'],
    ['text-menu', 'text-xs text-center dark:text-white text-accent p-1'],
    ['hero', ' text-success z-50 ml-16 shadow-light p-4 text-2xl font-bold font-sans font-thin'],
    ['title', 'text-3xl  font-bold font-sans font-thin'],
    ['nav-link', 'text-accent dark:text-warning text-lg'],
    ['slide-up', 'animate-slide-in-up animate-duration-300'],
    ['slide-down', 'animate-slide-in-down animate-duration-300'],
    ['slide-left', 'animate-slide-in-left animate-duration-300'],
    ['slide-right', 'animate-slide-in-right animate-duration-300'],
    ['fade-in', 'animate-fade-in animate-duration-300'],
    ['fade-in-up', 'animate-fade-in-up animate-duration-300'],
    ['fade-in-down', 'animate-fade-in-down animate-duration-300'],
    ['fade-in-left', 'animate-fade-in-left animate-duration-300'],
    ['fade-in-right', 'animate-fade-in-right animate-duration-300'],
    ['spin-in-up', 'animate-spin-in-up animate-duration-300'],
    ['spin-in-down', 'animate-spin-in-down animate-duration-300'],
    ['spin-in-left', 'animate-spin-in-left animate-duration-300'],
    ['spin-in-right', 'animate-spin-in-right animate-duration-300'],
    ['no-outline', 'outline-none focus:outline-none hover:outline-none'],
    ['toast', ' tr mt-16 row rounded-lg  shadow-primary sh-lg z-50 fixed p-4'],
    ['btn-get', 'dark:invert m-2 bg-primary text-light rounded-lg shadow-success hover:bg-success hover:text-accent hover:shadow-primary shadow-md px-4 py-2 cp hover:scale-110 hover:transition-all duration-200 ease-in-out hover:cursor-pointer'],
    ['btn-del', 'dark:invert m-2 bg-danger text-light rounded-lg shadow-warning hover:bg-warning hover:text-danger hover:shadow-danger shadow-md px-4 py-2 cp hover:scale-110 hover:transition-all duration-200 ease-in-out hover:cursor-pointer'],
    ['btn-post', 'dark:invert m-2 bg-success text-info rounded-lg shadow-primary hover:bg-primary hover:text-light hover:shadow-success shadow-md px-4 py-2 cp hover:scale-110 hover:transition-all duration-200 ease-in-out hover:cursor-pointer'],
    ['btn-put', 'dark:invert m-2 bg-warning text-light rounded-lg shadow-info hover:bg-info hover:text-light hover:shadow-warning shadow-md px-4 py-2 cp hover:scale-110 hover:transition-all duration-200 ease-in-out hover:cursor-pointer']],
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
      warn: true,
    }),
    presetTypography(),
    presetWebFonts({
      fonts: {
        sans: 'DM Sans',
        serif: 'DM Serif Display',
        mono: 'DM Mono',
        script: 'Merienda',
      },
    }),
  ],
  transformers: [
    transformerDirectives(),
    transformerVariantGroup(),
  ],
  safelist: 'prose prose-sm m-auto text-left'.split(' '),
  theme: {
    colors: {
      primary: '#5957FC',     // get primary light
      secondary: '#008080',   // post secondary success
      accent: '#240A4A',      // put warning accent
      success: '#21FDAD',    // delete danger warning
      warning: '#FEAD05',
      danger: '#F00A0A',
      info: '#121212',
      light: '#ffffff',
    },

  },
  rules: [
    [
      /^x(\d+)$/, ([, d]) => ({
        height: `${d}rem`,
        width: `${d}rem`,
      }),
    ],
    [/^[bg|border|color|fill|outline|shadow|text]-(.*)$/, ([, attr, color], { theme }) => {
      if (color in theme.colors) {
        switch (attr) {
          case 'bg':
            return {
              backgroundColor: theme.colors[color]
            }
          case 'border':
            return {
              borderColor: theme.colors[color]
            }
          case 'color':
            return {
              color: theme.colors[color]
            }
          case 'fill':
            return {
              fill: theme.colors[color]
            }
          case 'outline':
            return {
              outlineColor: theme.colors[color]
            }
          case 'shadow':
            return {
              shadowColor: theme.colors[color]
            }
          case 'text':
            return {
              color: theme.colors[color]
            }
        }
      }
    }]
  ]
})