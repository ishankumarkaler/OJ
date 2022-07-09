// /** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../judge/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"), require("tailwindcss"), require("postcss")],
}
