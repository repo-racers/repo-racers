/** @type {import('tailwindcss').Config} */
import themer from "@tailus/themer";
module.exports = {
  content: [
    './**/*.html',
    // Add paths to all other files that use Tailwind CSS classes here
  ],
  plugins: [
    themer({
        palette: {
            extend : "nature"
        },
        radius: "smoothest",
        background: "light",
        border: "light",
        padding:"large",
        components: {
            button: {
                rounded : "2xl"
            }
        }
    })
  ],
  corePlugins: {
      preflight: false,
    }
}
