/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ["index.html", "./frontend/src/doc.html"],
  theme: {
    extend: {
      fontFamily: {
        default: ['Inter var', ...defaultTheme.fontFamily.sans],
        display: "ui-sans-serif,system-ui,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;"
      },
    },
  },
  plugins: [],
}

