window.MathJax = {
  loader: { load: ["[tex]/physics"] },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { "[+]": ["physics"] },
    macros: {
      // LaTeX kernel text symbols that MathJax's TeX input doesn't define
      dag: "\\dagger",
      ddag: "\\ddagger",
      // bm package equivalent: \bm{x} renders as bold math (\boldsymbol)
      bm: ["\\boldsymbol{#1}", 1]
    }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => { 
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})
