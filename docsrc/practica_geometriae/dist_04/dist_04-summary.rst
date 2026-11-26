:title: SUMMARY — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
:layout: book
:order: 4
:tracks: English: dist_04-en | Latin: dist_04-la | Summary: dist_04-summary | Notes: dist_04-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0117
:excerpt: Mathematical decomposition of Euclid's On Divisions, side-point bisection, semicircle mean proportional, and centroid partition.

.. _dist-04-summary:
.. _unit-3-summary:

SUMMARY — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
==================================================================

.. rubric:: *Mathematical Apparatus and Exact Symbolic Decompositions*

:ref:`English Edition <dist-04-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-04-la>` · :ref:`GEOMETOR Notes <dist-04-notes>`

----

Taxonomy of Field Division Constructions
----------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Division Problem
     - Geometric Method
     - Exact Metric / Coordinate Solution
   * - **Vertex Partition**
     - Ratio of opposite base [VI. 1]
     - :math:`\Delta_1 : \Delta_2 = b_1 : b_2`
   * - **Boundary Point** :math:`D`
     - Parallel transversal [I. 37]
     - :math:`GZ = \frac{BG \cdot AG}{2 \cdot DG} = \frac{14 \times 15}{2 \times 9} = \frac{35}{3} = 11\frac{2}{3}`
   * - **Centroid** :math:`X(2)`
     - Concurrency of three medians
     - :math:`D = \left(\frac{19}{3}, 4\right)`, :math:`\Delta_1 = \Delta_2 = \Delta_3 = 28`
   * - **Base Parallel Cut**
     - Semicircle mean proportional [VI. 19]
     - :math:`AE^2 = 50`, :math:`AZ^2 = 72`, :math:`EZ^2 = 98`
   * - **Trapezoid RMS Cut**
     - Duplicate ratio of apex completion
     - :math:`c = \sqrt{\frac{a^2 + b^2}{2}} = \sqrt{\frac{49 + 289}{2}} = 13`
   * - **Circles & Portions**
     - Concentric radius or sector bisection
     - :math:`r_{\text{cut}} = \frac{R}{\sqrt{2}}`

----

Canonical Problem: Side-Point Division on :math:`(13, 14, 15)`
--------------------------------------------------------------

* **Given**: Scalene triangle :math:`ABG` (:math:`ab = 13, bg = 14, ag = 15`, area :math:`84`) and boundary point :math:`D` on base :math:`BG` with :math:`BD = 5, DG = 9`.
* **Construct**: Draw :math:`BT \parallel AD` meeting :math:`AG` produced at :math:`T`. Bisect :math:`TG` at :math:`Z`. Draw cut line :math:`DZ`.
* **Demonstrate**: :math:`\Delta(DZG) = \frac{1}{2} \Delta(TDG) = \frac{1}{2} \Delta(ABG) = 42`, leaving quadrilateral :math:`ABDZ = 42`.
