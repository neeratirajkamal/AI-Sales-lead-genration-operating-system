/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          dark: "#0b0f19",
          card: "#121827",
          border: "#1e293b",
          gold: "#f59e0b",
          emerald: "#10b981",
          cyan: "#06b6d4",
          violet: "#8b5cf6",
          rose: "#f43f5e"
        }
      }
    },
  },
  plugins: [],
}
