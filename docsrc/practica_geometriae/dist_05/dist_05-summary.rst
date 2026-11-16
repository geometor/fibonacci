:title: SUMMARY — DISTINCTIO V: EXTRACTION OF CUBE ROOTS
:layout: book
:order: 5
:tracks: English: dist_05-en | Latin: dist_05-la | Summary: dist_05-summary | Notes: dist_05-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0155
:excerpt: Mathematical decomposition of cube root extraction, spatial partition of (a+b)^3, and rational bounds for surd cube roots.

.. _dist-05-summary:

SUMMARY — DISTINCTIO V: EXTRACTION OF CUBE ROOTS
================================================

.. rubric:: *Mathematical Apparatus and Algorithmic Cube-Root Formulations*

:ref:`English Edition <dist-05-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-05-la>` · :ref:`GEOMETOR Notes <dist-05-notes>`

----

Binomial Spatial Partition of the Cube
--------------------------------------

The algebraic identity $(a + b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3$ corresponds to the eightfold geometric partition of a physical cube:

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Solid Element
     - Count & Dimensions
     - Geometric Interpretation
   * - **Primary Cube**
     - $1 \times (a \times a \times a)$
     - Cube on the initial tens/hundreds root $a^3$
   * - **Square Prisms**
     - $3 \times (a \times a \times b)$
     - Three square slabs of thickness $b$ on the three faces of $a^3$
   * - **Columnar Prisms**
     - $3 \times (a \times b \times b)$
     - Three oblong square columns filling the three corner edges
   * - **Corner Cube**
     - $1 \times (b \times b \times b)$
     - Small unit cube filling the final vertex corner $b^3$

----

Algorithmic Steps for Triad Extraction
--------------------------------------

1. **Partition**: Group digits into triads from right to left ($d_{3k-1} d_{3k-2} d_{3k-3}$).
2. **First Root $a$**: Find maximum integer $a$ such that $a^3 \le \text{highest triad}$.
3. **Remainder & Trial Divisor**: Compute $R = \text{triad} - a^3$. Bring down the next triad.
4. **Second Digit $b$**: Divide the brought-down remainder by trial divisor $300 a^2$.
5. **Deduction**: Verify and subtract $300 a^2 b + 30 a b^2 + b^3 = [3a(10a + b) + b^2]b$.

----

Rational Bounds for Surd Cubes
------------------------------

For integer $N = a^3 + R$ with $0 < R < 3a^2 + 3a + 1$:

$$\text{Root} \approx a + \frac{R}{3a^2 + 3a + 1} = a + \frac{R}{(a+1)^3 - a^3}.$$
