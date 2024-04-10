/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.html',
    // Add paths to all other files that use Tailwind CSS classes here
  ],
  corePlugins: {
      preflight: false,
    }
}
