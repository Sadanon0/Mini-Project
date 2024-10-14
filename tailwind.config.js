/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './static/**/*.css',
    './**/*.py',
  ],
  theme: {
    extend: {
      fontFamily: {
        niramit: ['Niramit', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
