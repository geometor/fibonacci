:title: GEOMETOR • fibonacci
:layout: landing

Leonardo Pisano (Fibonacci)
===========================

.. rubric:: *Practica Geometriae (1220), Liber Abaci (1202/1228) & Flos (1225) — Digital Scriptorium Codex & Exact Symbolic Constructions*

Welcome to **GEOMETOR Fibonacci** (``geometor-fibonacci``), a synchronized four-track Digital Scriptorium Book Codex and exact symbolic ``SymPy`` / ``geometor.model`` construction suite dedicated to :person:`Leonardo Pisano <fibonacci>` (*c.* 1170 – *c.* 1245). Grounded directly in :person:`Baldassarre Boncompagni <boncompagni>`'s public-domain critical Latin editions (*Scritti di Leonardo Pisano*, Vol. I, 1857; Vol. II, 1862), this repository unites Fibonacci's Latin *littera*, original GEOMETOR English translations, interactive ``.euclid-graphic`` geometric diagrams, and 100% exact algebraic verification.

.. picture:: /_static/figures/euclid_xiii_sphere_polyhedra.svg

----

The Four-Track Book Codex & Symbolic Engine
-------------------------------------------

* **Synchronized Four-Track Book Codex** (:doc:`practica_geometriae/index`):
  Read all eight *Distinctiones* of *Practica Geometriae* (1220)—together with Fibonacci's 1225 *Flos* cubic and *Liber Abaci* Ch. 12 rabbit recurrence—across four synchronized tracks: **English (GEOMETOR Translation)**, **Latin (1220 / Boncompagni 1862)**, **Summary**, and **Scholarly & Mathematical Notes**.
* **Preserving Euclid's Lost *On Divisions of Figures*** (:doc:`practica_geometriae/unit-3/unit-3-en`):
  Exact straightedge-and-compass :class:`~geometor.model.Model` reconstructions of *Distinctio IV* (*De divisione camporum inter consortes*), dividing triangles from boundary points, parallel to the base via semicircle mean proportionals, and into three equal shares at the centroid $X(2)$.
* **The Five Regular Polyhedra & Extreme and Mean Ratio** (:doc:`practica_geometriae/unit-4/unit-4-en`):
  Exact radical-tower inscriptions of the tetrahedron, cube, octahedron, dodecahedron ($e_{12} = \sqrt{15} - \sqrt{3}$), and icosahedron in a sphere of diameter $6$, forming the direct historical bridge from Euclid Books XIII–XIV to :person:`Piero della Francesca <piero-della-francesca>` and :person:`Luca Pacioli <pacioli>`'s *De Divina Proportione* (1509).
* **Exact Symbolic Python Demonstrations** (:doc:`demos/index` & :doc:`modules/index`):
  Runnable Python 3.13 modules verifying Pisan *pertica* metrology, Heron's incenter proof, Fibonacci's 96-gon circle bounds ($\pi \approx \frac{864}{275}$), Ptolemy's *census census* pentagon quartic ($x^4 + 3125 = 125x^2$), the *Flos* sexagesimal cubic ($1;22,7,42,33,4,40$), and Cassini's alternating convergence $F_{n+1}/F_n \to \phi$.

.. toctree::
   :maxdepth: 2
   :caption: Demonstrations, API & Log

   demos/index
   modules/index
   changelog
   log/index
