:type: summary
:title: SUMMARY — DISTINCTIO II: EXTRACTION OF SQUARE ROOTS
:layout: book
:order: 2
:folio: boncompagni_1862_vol2_practica_geometriae:0025
:excerpt: Mathematical decomposition of Hindu-Arabic square-root extraction, rational convergents, and agrarian root calculations.

.. _dist-02-summary:

SUMMARY — DISTINCTIO II: EXTRACTION OF SQUARE ROOTS
===================================================

.. rubric:: *Mathematical Apparatus and Algorithmic Root Formulations*

:ref:`English Edition <dist-02-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-02-la>` · :ref:`GEOMETOR Notes <dist-02-notes>`

----

Positional Extraction Decomposition
-----------------------------------

* **Identity**: :math:`(10a + b)^2 = 100a^2 + 20ab + b^2 = 100a^2 + (20a + b)b`.
* **Digit Pairs**: For :math:`N = d_{2k-1} d_{2k-2} \dots d_1 d_0`:

  1. Determine greatest integer :math:`a` such that :math:`a^2 \le d_{2k-1} d_{2k-2}`.
  2. Compute remainder :math:`R_1 = d_{2k-1} d_{2k-2} - a^2`.
  3. Form trial divisor :math:`20a`; find maximum digit :math:`b` such that :math:`(20a + b)b \le 100 R_1 + d_{2k-3} d_{2k-4}`.
  4. Recurse until all digit pairs are exhausted.

----

Rational Convergents for Non-Square Integers
--------------------------------------------

For :math:`N = a^2 + r` with :math:`0 < r < 2a + 1`:

1. **Lower Bound**:

   .. math::

      a_{\text{low}} = a + \frac{r}{2a + 1}.

2. **Upper Bound (Hero-Fibonacci First Step)**:

   .. math::

      a_1 = a + \frac{r}{2a}.

3. **Second Iterative Correction (Newton-Raphson Step)**:

   .. math::

      a_2 = a_1 - \frac{a_1^2 - N}{2a_1} = \frac{1}{2}\left(a_1 + \frac{N}{a_1}\right).

----

Root Extraction in Pisan Subunits
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Agrarian Area
     - Reduction to Subunits
     - Resulting Linear Side
   * - :math:`\frac{2}{3}` superficial pertica
     - :math:`24` denarii (:math:`7{,}776` sq. unciae)
     - :math:`88\frac{2}{11}` unciae = :math:`4\text{ft } 16\frac{2}{11}\text{in}`
   * - :math:`1` stariorum (:math:`66` perticae)
     - :math:`2{,}376` denarii (:math:`769{,}824` sq. unciae)
     - :math:`8\text{p } 0\text{ft } 13\frac{3}{4}\text{in}`
