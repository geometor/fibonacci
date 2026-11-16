:title: CAPITULUM XII.7 NOTES — MATHEMATICAL & PHILOLOGICAL COMMENTARY
:layout: book
:order: 12
:tracks: English: cap_12-en | Latin: cap_12-la | Summary: cap_12-summary | Notes: cap_12-notes
:folio: boncompagni_1857_vol1_liber_abbaci:0289
:excerpt: Mathematical commentary on the Fibonacci recurrence, Binet's formula, Cassini's identity, and SymPy verification in geometor.fibonacci.

.. _cap-12-notes:
.. _unit-5-s4-notes:
.. _liber-abbaci-cap12-notes:

CAPITULUM XII.7 NOTES — MATHEMATICAL & PHILOLOGICAL COMMENTARY
==============================================================

.. rubric:: *From the Medieval Rabbit Enclosure to Binet's Formula, Kepler's Golden Ratio Limit, and Modern GEOMETOR Modeling*

:ref:`English Edition <cap-12-en>` · :ref:`Latin (1202/1228 / Boncompagni 1857) <cap-12-la>` · :ref:`Summary <cap-12-summary>`

----

.. _cap-12-s1-notes:

1. The Biological Context and Mathematical Modeling
---------------------------------------------------

The rabbit problem in Chapter XII, Part 7 of *Liber Abbaci* (*Boncompagni Vol. I, pp. 283–284*) stands as the first documented mathematical model of an expanding biological population. Fibonacci formulates four explicit axioms:

1. A single breeding pair of rabbits is enclosed in an isolated environment.
2. Every mature pair breeds another pair each month.
3. A newborn pair matures and begins bearing in the second month after its birth.
4. No mortality occurs during the one-year observation period.

Under these boundary conditions, the population progression is given by the recursive sum of the existing population and the reproductive cohort: $F_{n+1} = F_n + F_{n-1}$.

----

.. _cap-12-s2-notes:

2. Historical Reception: From Fibonacci to Kepler and Lucas
-----------------------------------------------------------

Curiously, Fibonacci himself did not explore the asymptotic ratio of the sequence, nor did he name it after himself. The historical rediscovery proceeded in stages:

* **Johannes Kepler ($1611$)**: In *Strena Seu de Nive Sexangula* (*On the Six-Cornered Snowflake*), Kepler observed that the ratio of consecutive terms in $1, 1, 2, 3, 5, 8, 13, \dots$ converges to the divine proportion $\tau = \frac{\sqrt{5}-1}{2}$ and governs the phyllotactic arrangement of leaves and seeds.
* **Albert Girard ($1634$)**: Stated the general recurrence $A_{n+2} = A_{n+1} + A_n$ in his edition of Simon Stevin's works.
* **Giovanni Domenico Cassini ($1680$)**: Discovered the determinant identity $F_{n-1}F_{n+1} - F_n^2 = (-1)^n$, which later formed the basis of the Lewis Carroll chessboard dissection paradox ($64 = 65$).
* **Édouard Lucas ($1876$)**: Formally bestowed the name **Fibonacci sequence** (*suite de Fibonacci*) upon Leonardo's numbers and developed the companion Lucas sequence $L_n = F_{n-1} + F_{n+1}$ ($2, 1, 3, 4, 7, 11, \dots$).

----

.. _cap-12-s3-notes:

3. Binet's Formula and Algebraic Roots
--------------------------------------

The characteristic equation of the recurrence is:

$$r^2 - r - 1 = 0 \implies r = \frac{1 \pm \sqrt{5}}{2}.$$

Letting $\phi = \frac{1 + \sqrt{5}}{2}$ and $\psi = \frac{1 - \sqrt{5}}{2} = -\frac{1}{\phi}$, the closed-form expression discovered by :person:`Jacques Philippe Marie Binet <binet>` ($1843$) gives:

$$F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} = \frac{1}{\sqrt{5}} \left[ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right].$$

Because $|\psi| \approx 0.618 < 1$, the term $\psi^n \to 0$ rapidly as $n \to \infty$, so $F_n = \left\lfloor \frac{\phi^n}{\sqrt{5}} + \frac{1}{2} \right\rfloor$ for all $n \ge 1$.

----

.. _cap-12-s4-notes:

4. SymPy Computational Modeling in GEOMETOR
-------------------------------------------

In ``geometor.fibonacci``, the sequence and its convergence to $\phi$ are verified symbolically using SymPy:

.. code-block:: python

   import sympy as sp
   from geometor.fibonacci import (
       fibonacci_rabbit_convergents,
       verify_cassini_identity,
   )

   # Compute first 12 rabbit sequence terms from Liber Abbaci
   terms = fibonacci_rabbit_convergents(12)
   # Assert final 12th month count matches Boncompagni p. 284
   assert terms[-1]["pairs"] == 377

   # Verify Cassini's identity for n=1..12
   assert verify_cassini_identity(12)

The connection between *Liber Abbaci* Cap. XII and *Practica Geometriae* Distinctio VIII is direct: the irrational segment $s_{10} = \frac{5}{\phi}$ and pentagon side $s_5$ constructed by ruler and compass in *Practica Geometriae* are the exact geometric realization of the algebraic ratio towards which Fibonacci's rabbits multiply.
