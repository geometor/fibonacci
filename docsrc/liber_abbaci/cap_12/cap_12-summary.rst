:title: CAPITULUM XII.7 SUMMARY — THE RABBIT SEQUENCE & RECURRENCE
:layout: book
:order: 12
:tracks: English: cap_12-en | Latin: cap_12-la | Summary: cap_12-summary | Notes: cap_12-notes
:folio: boncompagni_1857_vol1_liber_abbaci:0289
:excerpt: Summary of the rabbit recurrence relation, monthly population growth, Cassini's identity, and convergence to the golden ratio.

.. _cap-12-summary:
.. _liber-abbaci-cap12-summary:

CAPITULUM XII.7 SUMMARY — THE RABBIT SEQUENCE & RECURRENCE
==========================================================

.. rubric:: *Structural Synopsis of Boncompagni Vol. I, pp. 283–284 (fol. 124r)*

:ref:`English Edition <cap-12-en>` · :ref:`Latin (1202/1228 / Boncompagni 1857) <cap-12-la>` · :ref:`GEOMETOR Notes <cap-12-notes>`

----

Overview
--------

In Capitulum XII, Part 7 of *Liber Abbaci*, Fibonacci formulates the earliest recorded mathematical model of biological population growth. Under the idealized assumptions of monthly reproduction and a one-month maturation lag, the number of rabbit pairs follows the second-order linear recurrence relation :math:`F_{n+1} = F_n + F_{n-1}`, generating the sequence :math:`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377`.

Month-by-Month Population Model
-------------------------------

.. list-table:: Monthly Population Dynamics Over One Solar Year
   :header-rows: 1
   :widths: 15 15 15 20 35

   * - Month (:math:`n`)
     - Mature Pairs
     - Newborn Pairs
     - Total Pairs (:math:`F_n`)
     - Successive Ratio (:math:`F_n / F_{n-1}`)
   * - **0 (Start)**
     - 1
     - 0
     - **1**
     - —
   * - **1**
     - 1
     - 1
     - **2**
     - :math:`2 / 1 = 2.000000`
   * - **2**
     - 2
     - 1
     - **3**
     - :math:`3 / 2 = 1.500000`
   * - **3**
     - 3
     - 2
     - **5**
     - :math:`5 / 3 \approx 1.666667`
   * - **4**
     - 5
     - 3
     - **8**
     - :math:`8 / 5 = 1.600000`
   * - **5**
     - 8
     - 5
     - **13**
     - :math:`13 / 8 = 1.625000`
   * - **6**
     - 13
     - 8
     - **21**
     - :math:`21 / 13 \approx 1.615385`
   * - **7**
     - 21
     - 13
     - **34**
     - :math:`34 / 21 \approx 1.619048`
   * - **8**
     - 34
     - 21
     - **55**
     - :math:`55 / 34 \approx 1.617647`
   * - **9**
     - 55
     - 34
     - **89**
     - :math:`89 / 55 \approx 1.618182`
   * - **10**
     - 89
     - 55
     - **144**
     - :math:`144 / 89 \approx 1.617978`
   * - **11**
     - 144
     - 89
     - **233**
     - :math:`233 / 144 \approx 1.618056`
   * - **12**
     - 233
     - 144
     - **377**
     - :math:`377 / 233 \approx 1.618026`

Mathematical Properties of the Recurrence
-----------------------------------------

1. **Linear Recurrence**:

   .. math::

      F_{n+1} = F_n + F_{n-1}, \quad \text{with } F_1 = 1, \; F_2 = 2.

2. **Cassini's Identity (1680)**:

   .. math::

      F_{n-1} F_{n+1} - F_n^2 = (-1)^n.

   *Example for* :math:`n = 6`: :math:`13 \times 34 - 21^2 = 442 - 441 = +1`.

3. **Convergence to the Golden Ratio**:

   .. math::

      \lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \phi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887\dots

   The successive rational ratios :math:`\frac{F_{n+1}}{F_n}` oscillate strictly above and below :math:`\phi`, providing the best rational convergents to the extreme and mean ratio of *Practica Geometriae* Distinctio VIII.
