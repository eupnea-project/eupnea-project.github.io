export default {
  title: "The Eupnea Project",
  description: "Boot a full Linux system and gain complete control over your device WITHOUT modifying the firmware.",
  themeConfig: {
    sidebar: [
      {
        text: "📜 Depthboot instructions",
        items: [
          { text: "Requirements", link: "/depthboot/requirements" },
          { text: "Build instructions", link: "/depthboot/build-instructions" },
          { text: "Audio", link: "/depthboot/audio" },
          { text: "Optional features", link: "/depthboot/optional" },
        ]
      },
      {
        text: "🔨 Compile instructions",
        items: [
          { text: "Compile the Eupnea kernel", link: "/compile/kernel" },
          { text: "Compile EupneaOS", link: "/compile/eupneaos" },
          // { text: "Compile Depthboot", link: "/depthboot/requirements" },
        ]
      },
      {
        text: "📖 Chromebook quirks",
        items: [
          { text: "Sleep bootlock", link: "/eupnea/bootlock" },
          { text: "Depthcharge", link: "/eupnea/depthcharge" },
          { text: "SWAP(ZRAM)", link: "/eupnea/ram-extensions" },
        ]
      },
      {
        text: "📖 Project documentation",
        items: [
          { text: "Eupnea Kernels", link: "/development/kernels" },
        ]
      },
      {
        text: "🌐 External docs",
        items: [
          { text: "UEFI/rw_legacy", link: "https://mrchromebox.tech/#bootmodes" },
          { text: "Depthcharge", link: "https://libreboot.org/docs/depthcharge/" },
          { text: "Linux on pre-coreboot Chromebooks", link: "https://github.com/nh2/chrubuntu-anyos" },
          { text: "Linux on arm Chromebooks", link: "https://github.com/Maccraft123/Cadmium" },
        ]
      },
      {
        text: "🟢 Distro + DE status",
        link: "https://docs.google.com/spreadsheets/d/1-zIX8lWEXVcO71xCuzvZpHvCUizrU7csKfJusqB2CYM"
      },
      {
        text: "GitHub (source code)",
        link: "https://github.com/eupnea-linux/eupnea-builder"
      }
    ]
  },
}