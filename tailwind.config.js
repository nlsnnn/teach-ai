/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./app/templates/**/*.html",
      "./app/**/templates/**/*.html",
      "./app/**/*.py",
    ],
    theme: {
      extend: {
        colors: {
          primary: {
            50: "#fef6ee",
            100: "#fdead7",
            200: "#fbd0ae",
            300: "#f8af7b",
            400: "#f48344",
            500: "#f15e1e",
            600: "#e24414",
            700: "#bc3213",
            800: "#962917",
            900: "#792416",
          },
          secondary: {
            50: "#f0fdf4",
            100: "#dcfce7",
            200: "#bbf7d0",
            300: "#86efac",
            400: "#4ade80",
            500: "#22c55e",
            600: "#16a34a",
            700: "#15803d",
            800: "#166534",
            900: "#14532d",
          },
        },
      },
    },
    plugins: [],
  }