0.1.0 (2026-11-12)
------------------

Initial scholarly Digital Scriptorium 4-track Book Codex and exact symbolic
``SymPy`` / ``geometor.model`` construction suite for **Leonardo Pisano
(Fibonacci): Practica Geometriae (1220)**, with foundational bridges from
*Flos* (1225) and *Liber Abaci* (1202/1228).

* **4-Track Synchronized Book Codex** (``docsrc/practica_geometriae/``):

  * Diplomatic public-domain Latin edition grounded in Baldassarre Boncompagni,
    *Scritti di Leonardo Pisano*, Vol. II (*Leonardi Pisani Practica Geometriae
    ed Opuscoli*, Rome, 1862) and Vol. I (*Il Liber Abbaci*, Rome, 1857).
  * Original GEOMETOR English translations, structural summaries, and symbolic
    commentary across 5 synchronized units (20 ``:layout: book`` RST files)
    covering the Prologue to Master Dominicus, Pisan agrarian metrology, all
    eight *Distinctiones*, *Flos* (1225), and *Liber Abaci* Cap. XII.
  * Runtime ``geometor.fibonacci.sphinx_ext`` registering the
    ``Latin (1220 / Boncompagni 1862)`` companion track and offline-safe local
    intersphinx bindings across sister GEOMETOR repositories.

* **Exact Symbolic Geometry Engine** (``src/geometor/fibonacci/``):

  * ``mensuration.py``: Pisan *pertica* / *stariorum* ($66$ *perticae*) algebra,
    Heron polynomial identity over $\mathbb{Z}[x, y, z]$, Euclidean incenter
    proof on $(13, 14, 15)$ ($T = (6, 4)$, $r = 4$, $\Delta = 84$), and
    Fibonacci's 96-gon circle bounds ($\frac{6480}{2063} < \pi < \frac{7200}{2291}$,
    mean $\frac{864}{275}$).
  * ``divisions.py``: Exact compass-and-straightedge reconstructions of Euclid's
    lost *On Divisions of Figures* (*Distinctio IV*)—boundary-point cuts
    ($GZ = \frac{35}{3}$), semicircle mean-proportional parallel cuts on
    $(10, 14, 12)$ ($AE^2 = 50, AZ^2 = 72, EZ^2 = 98$), median concurrency at
    centroid $X(2)$, and Babylonian/Euclidean trapezoid root-mean-square chords.
  * ``polyhedra_golden.py``: Exact radical metrics and Euclid XIII.18 section
    for all five Platonic solids in sphere diameter $d = 6$, Hypsicles Book XIV
    volume ratio $\sqrt{\frac{5 + \sqrt{5}}{6}}$, golden chord division
    ($\sqrt{15} - \sqrt{3}$), *Distinctio VIII* pentagon/decagon in $d = 10$ via
    *census census* quartic $x^4 + 3125 = 125x^2$, *Quadrans* optical surveying,
    *Flos* sexagesimal cubic ($1; 22, 7, 42, 33, 4, 40$) and *congruum* of $5$,
    and *Liber Abaci* rabbit convergents to $\phi$.
  * ``render.py`` & ``scripts/build_figures.py``: 10 theme-adaptive interactive
    ``.euclid-graphic`` SVGs with 3-vertex midpoint paths and bidirectional
    ``:g:`` / ``:eq:`` highlighting.

* **Scholarly Apparatus & Demos** (``resources/``, ``demos/``, ``tests/``):

  * Complete JSON registries (``sources_manifest.json``, ``concordance.json``,
    ``persons.json``, ``citations.json``, ``glossary.json``) powering hover
    cards and cross-canon concordance tables.
  * Runnable Rich CLI demonstrations and full ``pytest`` verification suite.
