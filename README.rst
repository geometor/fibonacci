==================
GEOMETOR Fibonacci
==================

**Scholarly Four-Track Digital Scriptorium Codex & Exact Symbolic Constructions for Leonardo Pisano (Fibonacci): Practica Geometriae (1220), Liber Abaci (1202/1228), and Flos (1225)**

``geometor-fibonacci`` unites a folio-verified, four-track **Book Codex**
(``:layout: book``) of Leonardo Pisano's *Practica Geometriae* (1220)—grounded
in Baldassarre Boncompagni's public-domain critical Latin edition (*Scritti di
Leonardo Pisano*, Rome, 1857–1862)—with **100% exact symbolic algebra** and
constructive proofs built on `SymPy <https://www.sympy.org/>`_ and
``geometor.model``.

Key Highlights
==============

1. **Four-Track Synchronized Book Codex** (``docsrc/practica_geometriae/``):

   * **English** (``-en.rst``) — Original scholarly English translation authored
     directly from Boncompagni's 1857/1862 Latin folios.
   * **Latin (1220 / Boncompagni 1862)** (``-la.rst``) — Diplomatic Latin text
     preserving Fibonacci's Pisan metrology, Greco-Arabic geometric notation
     (``.a.b.g.``, *embadum*, *cathetus*, *casus*), and algebraic terminology
     (*res*, *census*, *census census*).
   * **Summary** (``-summary.rst``) — Structural synopses and invariant tables.
   * **Notes** (``-notes.rst``) — Historical, philological, and exact symbolic
     commentary linking Fibonacci to ``euclid``, ``elements``, ``heron``,
     ``archimedes``, ``pacioli``, ``divine``, ``phyllotaxis``, ``etc``, and
     ``wildberger``.

2. **Exact Symbolic Constructive Engine** (``src/geometor/fibonacci/``):

   * **Mensuration & Circle Bounds** (``mensuration.py``): Pisan $6 \times 6$
     *pertica* / $66$-*pertica* *stariorum* arithmetic, Euclidean incenter proof
     of Heron's formula on $(13, 14, 15)$, and Fibonacci's small-number 96-gon
     Archimedean circle bounds ($\pi_{\text{Fib}} = \frac{864}{275}$).
   * **Divisions of Planar Figures** (``divisions.py``): Reconstructions of
     Euclid's lost *On Divisions* (*Distinctio IV*)—boundary-point cuts,
     semicircle mean-proportional parallel cuts over $\mathbb{Q}(\sqrt{2})$,
     median concurrency at centroid $X(2)$, and trapezoid RMS chords.
   * **Regular Polyhedra, Algebra & Golden Convergence** (``polyhedra_golden.py``):
     All five Platonic solids in sphere diameter $d = 6$, Hypsicles' Book XIV
     ratio $\sqrt{\frac{5+\sqrt{5}}{6}}$, *Distinctio VIII* pentagon/decagon in
     $d = 10$ ($x^4 + 3125 = 125x^2$), *Quadrans* optical surveying, the *Flos*
     sexagesimal cubic ($x^3 + 2x^2 + 10x = 20$), and *Liber Abaci* Ch. 12
     rabbit convergents to $\phi = \frac{1+\sqrt{5}}{2}$.
   * **10 Interactive ``.euclid-graphic`` SVGs** (``docsrc/_static/figures/``):
     Generated reproducibly by ``scripts/build_figures.py`` with bidirectional
     ``:g:`` and ``:eq:`` hover/click highlighting.

Quick Start
===========

Run inside the Python 3.13 ``uv`` workspace environment:

.. code-block:: bash

   # Run Rich CLI overview & demo scripts
   python3 demos/mensuration_demo.py
   python3 demos/divisions_demo.py
   python3 demos/polyhedra_golden_demo.py

   # Regenerate all 10 interactive .euclid-graphic SVGs
   python3 scripts/build_figures.py

   # Run verification gates & build the Sphinx Book Codex
   pytest
   ruff check src scripts demos tests
   publish build

Provenance & License
====================

* **Historical Source Texts**: 100% Public Domain — Baldassarre Boncompagni,
  *Scritti di Leonardo Pisano, matematico del secolo decimoterzo*, Vol. I (*Il
  Liber Abbaci*, Rome, 1857) and Vol. II (*Leonardi Pisani Practica Geometriae
  ed Opuscoli*, Rome, 1862, edited from Biblioteca Apostolica Vaticana, Cod.
  Urb. Lat. 292).
* **Translations, Symbolic Code & Diagrams**: Original work authored for the
  GEOMETOR initiative under the MIT License.
