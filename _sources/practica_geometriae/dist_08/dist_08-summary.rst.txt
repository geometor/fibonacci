:title: SUMMARY — DISTINCTIO VIII: SUBTILITATES GEOMETRICAE & FLOS (1225)
:layout: book
:order: 8
:tracks: English: dist_08-en | Latin: dist_08-la | Summary: dist_08-summary | Notes: dist_08-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0214
:excerpt: Mathematical decomposition of the regular decagon and pentagon, Abu Kamil's quartic, and the Flos cubic equation.

.. _dist-08-summary:
.. _unit-5-summary:

SUMMARY — DISTINCTIO VIII: SUBTILITATES GEOMETRICAE & FLOS (1225)
=================================================================

.. rubric:: *Mathematical Apparatus, Algebraic Equations, and Imperial Challenge Solutions*

:ref:`English Edition <dist-08-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-08-la>` · :ref:`GEOMETOR Notes <dist-08-notes>`

----

Exact Metrics in Circle Diameter :math:`d = 10` (:math:`r = 5`)
---------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Inscribed Figure
     - Exact Algebraic Expression
     - Numerical Value
   * - **Hexagon Side** (:math:`s_6`)
     - :math:`r = 5`
     - :math:`5.000000\dots`
   * - **Decagon Side** (:math:`s_{10}`)
     - :math:`\sqrt{31\frac{1}{4}} - 2\frac{1}{2} = \frac{5(\sqrt{5} - 1)}{2}`
     - :math:`3.0901699\dots`
   * - **Pentagon Side** (:math:`s_5`)
     - :math:`\sqrt{62\frac{1}{2} - \sqrt{781\frac{1}{4}}} = \frac{5\sqrt{10 - 2\sqrt{5}}}{2}`
     - :math:`5.8778525\dots`
   * - **Pentagon Diagonal** (:math:`d_5`)
     - :math:`s_5 \cdot \phi = \frac{5\sqrt{10 + 2\sqrt{5}}}{2}`
     - :math:`9.5105651\dots`

----

The Algebraic Quartic of Abū Kāmil
----------------------------------

* **Equation**: :math:`x^4 + 3{,}125 = 125\,x^2`.
* **Roots in Census** (:math:`x^2`):

  .. math::

     x^2 = \frac{125 \pm \sqrt{125^2 - 4 \times 3{,}125}}{2} = 62\frac{1}{2} \pm \sqrt{781\frac{1}{4}}.

  The lesser root gives the pentagon side :math:`s_5^2 = 62\frac{1}{2} - \sqrt{781\frac{1}{4}}`; the greater root gives the diagonal :math:`d_5^2 = 62\frac{1}{2} + \sqrt{781\frac{1}{4}}`.

----

Additional Subtleties in Distinctio VIII
----------------------------------------

* **Circumscribed Polygons** (:math:`d = 10`): Pentagon side :math:`\sqrt{500 - \sqrt{200{,}000}}`, decagon side :math:`\sqrt{100 - \sqrt{8{,}000}}`.
* **Pentagon in Square & Triangle Problems** (:math:`s = 10`): Pentagon in square gives :math:`x^2 + 400 = (40 + \sqrt{800})x`; square (and pentagon :math:`adefg`) in equilateral triangle gives :math:`x = 20\sqrt{3} - 30 \approx 4.641`.
* **Indeterminate Squares**: Finding :math:`x^2 + 5 = y^2` via *res*, proportion, and odd-sum progression.

----

Solutions to the Imperial Court Challenges (*Flos*, 1225)
---------------------------------------------------------

1. **The Congruum of 5**:

   .. math::

      \left(\frac{41}{12}\right)^2 - 5 = \left(\frac{31}{12}\right)^2 = \frac{961}{144}, \qquad \left(\frac{41}{12}\right)^2 + 5 = \left(\frac{49}{12}\right)^2 = \frac{2401}{144}.

2. **The Sexagesimal Cubic Root**:

   .. math::

      x^3 + 2x^2 + 10x = 20 \implies x = \frac{1{,}596{,}577{,}777}{1{,}166{,}400{,}000} \approx 1.36880810785322\dots
