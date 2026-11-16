:title: DISTINCTIO V — EXTRACTION OF CUBE ROOTS
:layout: book
:order: 5
:tracks: English: dist_05-en | Latin: dist_05-la | Summary: dist_05-summary | Notes: dist_05-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0155
:excerpt: Positional cube-root extraction from (a + b)^3 and rational approximation formulas for surd cube roots.

.. _dist-05-en:
.. _unit-4-dist5-en:

DISTINCTIO V — EXTRACTION OF CUBE ROOTS
=======================================

.. rubric:: *On the Finding of Cube Roots (De Radicibus Cubicis Inveniendis) in Theory and Practice*

**Source Text**: :cite:`fibonacci:pg-5` (*Boncompagni Vol. II, pp. 148–158 · fol. 92v–100r*) · :ref:`Latin (1220 / Boncompagni 1862) <dist-05-la>` · :ref:`Summary <dist-05-summary>` · :ref:`GEOMETOR Notes <dist-05-notes>`

----

.. _dist-05-roots-en:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0155
   :page: 148–158

Positional Extraction of Cube Roots
-----------------------------------

*Latin Locus*: :ref:`Distinctio V (pp. 148–158) <dist-05-la>` · *Commentary*: :ref:`Notes on Cube-Root Extraction <dist-05-s1-notes>`

.. enunciation::

   Here begins the fifth distinction, on finding cube roots. Since according to the promises made in the beginning of this work I must treat of cube roots, of which I inserted a special treatise in the *Book of Calculation* (*Liber Abaci*), I have thought good to rewrite the same here, so that having continued the above distinctions I may more easily arrive at the end of the work.

A cube number is that which arises from the multiplication of three equal numbers, or from any square number multiplied into its root. For example, $8$ and $27$: for $8$ arises from $2 \times 2 \times 2$, or from $4$ into its root $2$; and $27$ arises from three $3$s, or from $9$ into its root $3$. The cube root of $8$ is $2$, and of $27$ is $3$. Numbers which are not cubes cannot have rational cube roots in numbers, and their roots are called surd (*surdae*).

1. **Positional Grouping by Triads**: Just as in square roots digits are taken in pairs from the right, so in cube roots digits are grouped in **triads** (*ternarii*):
   * A number of $1, 2, 3$ digits has a root of $1$ digit;
   * A number of $4, 5, 6$ digits has a root of $2$ digits;
   * A number of $7, 8, 9$ digits has a root of $3$ digits; and so on.
2. **Decomposition via the Binomial Cube**: Drawing upon the spatial partition of the cube:

   $$(a + b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3 = a^3 + [3a(a + b) + b^2]b.$$

   Subtract the greatest cube $a^3$ from the highest triad; the remainder is divided by the trial divisor $3a^2$ (or $300a^2$) to determine the next digit $b$.
3. **Rational Approximation for Non-Cubes**: When a remainder $R = N - a^3 > 0$ remains after extracting the integer cube part $a$, Leonardo formulates the rational convergent:

   $$\sqrt[3]{a^3 + R} \approx a + \frac{R}{3a(a + 1) + 1} = a + \frac{R}{3a^2 + 3a + 1}.$$

   Since $(a + 1)^3 - a^3 = 3a^2 + 3a + 1$, the denominator is the exact difference between the successive integer cubes, bounding the fractional part strictly within $[0, 1)$.

.. qed::

   Equipped with cube root extraction, the geometer is prepared to measure corporeal solids and the regular polyhedra inscribed in a sphere.
