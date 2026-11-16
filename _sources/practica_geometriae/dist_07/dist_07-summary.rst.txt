:title: SUMMARY — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
:layout: book
:order: 7
:tracks: English: dist_07-en | Latin: dist_07-la | Summary: dist_07-summary | Notes: dist_07-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0209
:excerpt: Mathematical decomposition of the 12x12 shadow square, optical triangle similarity, and altimetric surveying.

.. _dist-07-summary:

SUMMARY — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
=====================================================

.. rubric:: *Mathematical Apparatus and Altimetric Formulations*

:ref:`English Edition <dist-07-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-07-la>` · :ref:`GEOMETOR Notes <dist-07-notes>`

----

Shadow Square Trigonometry
--------------------------

Let $D$ be the sighting apex, $h_e$ the eye height above the ground, $D_{\text{base}}$ the horizontal distance to the tower base, and $H$ the total height:

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Plumb Line Sighting
     - Puncta Reading
     - Altimetric Formula
   * - **Diagonal ($45^\circ$)**
     - $12$ puncta ($DA$ line)
     - $H = D_{\text{base}} + h_e$
   * - **Umbra Recta ($p$)**
     - $p$ puncta on horizontal side ($p < 12$)
     - $H = \frac{12}{p} \cdot D_{\text{base}} + h_e$
   * - **Umbra Versa ($v$)**
     - $v$ puncta on vertical side ($v < 12$)
     - $H = \frac{v}{12} \cdot D_{\text{base}} + h_e$

----

Canonical Problem: Steep Tower Sighting
---------------------------------------

* **Given**: Distance to tower $D_{\text{base}} = 40$ perticae, observer eye-height $h_e = 1$ pertica, plumb line reading on *umbra recta* $p = 8$ puncta (out of $12$).
* **Compute**:
  
  $$\text{Elevation} = \frac{12}{8} \times 40 = \frac{3}{2} \times 40 = 60 \text{ perticae}.$$
  $$H = 60 + 1 = 61 \text{ perticae}.$$
