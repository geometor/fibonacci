:title: SUMMARY — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
:layout: book
:order: 3
:tracks: English: dist_03-en | Latin: dist_03-la | Summary: dist_03-summary | Notes: dist_03-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0037
:excerpt: Mathematical decomposition of Heron's incenter proof, triangle cathetus calculations, quadrilateral formulas, and the 96-gon circle bounds.

.. _dist-03-summary:
.. _unit-2-summary:

SUMMARY — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
==============================================================================

.. rubric:: *Geometric Decompositions, Incenter Trigonometry, and Archimedean Circle Bounds*

:ref:`English Edition <dist-03-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-03-la>` · :ref:`GEOMETOR Notes <dist-03-notes>`

----

Structured Proof Decomposition: Heron's Formula
-----------------------------------------------

* **Given**: Triangle $ABG$ with integer sides $a = 14$, $b = 15$, $c = 13$, semiperimeter $s = 21$.
* **Construct**:
  1. Angle bisectors $BT$, $GT$ meeting at incenter $T(6, 4)$.
  2. Perpendiculars $TH = TE = TZ = r = 4$ touching sides $BG$, $AB$, $AG$.
  3. Produce base $BG$ to $L$ such that $GL = AZ = 6$, giving $BL = s = 21$.
  4. Auxiliary perpendiculars creating cyclic similarity $BL : BH = HG : \text{aux}$.
* **Demonstrate**:
  
  $$\Delta^2 = (r \cdot s)^2 = s(s - a)(s - b)(s - c) = 21 \times 7 \times 6 \times 8 = 7{,}056 \implies \Delta = 84.$$

----

Archimedean 96-gon Bounds Decomposition
---------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Estimate Type
     - Exact Fraction
     - Decimal Approximation
   * - **Archimedes Lower**
     - $\frac{223}{71}$
     - $3.140845\dots$
   * - **Fibonacci Inscribed 96-gon**
     - $\frac{6480}{2063}$
     - $3.141057\dots$
   * - **True Pi ($\pi$)**
     - $\dots$
     - $3.14159265\dots$
   * - **Fibonacci Harmonic Mean**
     - $\frac{864}{275}$
     - $3.141818\dots$
   * - **Fibonacci Circumscribed 96-gon**
     - $\frac{7200}{2291}$
     - $3.142732\dots$
   * - **Archimedes Upper**
     - $\frac{22}{7}$
     - $3.142857\dots$

----

Classification of Planar Figures
--------------------------------

1. **Orthogonal Triangles**: $\Delta = \frac{1}{2} a b$.
2. **Acute Scalene Triangles**: Cathetus $h = \sqrt{c^2 - \text{casus}^2}$ via [II. 13].
3. **Obtuse Triangles**: Cathetus via [II. 12].
4. **Rhombi**: $\Delta = \frac{1}{2} e_1 e_2$.
5. **Trapezoids**: $\Delta = \frac{a + b}{2} h$.
6. **Circles**: $\Delta = \frac{1}{2} r C = \frac{11}{14} d^2$.
