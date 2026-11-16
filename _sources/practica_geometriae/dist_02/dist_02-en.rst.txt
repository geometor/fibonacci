:title: DISTINCTIO II — EXTRACTION OF SQUARE ROOTS
:layout: book
:order: 2
:tracks: English: dist_02-en | Latin: dist_02-la | Summary: dist_02-summary | Notes: dist_02-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0025
:excerpt: Finding square roots of integers, fractions, and surds in Hindu-Arabic numerals and Pisan subunits.

.. _dist-02-en:
.. _unit-1-dist2-en:

DISTINCTIO II — EXTRACTION OF SQUARE ROOTS
==========================================

.. rubric:: *On the Finding of Square Roots (De Inventione Radicum) in Integers, Fractions, and Agrarian Units*

**Source Text**: :cite:`fibonacci:pg-2` (*Boncompagni Vol. II, pp. 18–30 · fol. 11v–18v*) · :ref:`Latin (1220 / Boncompagni 1862) <dist-02-la>` · :ref:`Summary <dist-02-summary>` · :ref:`GEOMETOR Notes <dist-02-notes>`

----

.. _dist-02-roots-en:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0025
   :page: 18–30

Finding Square Roots in Theory and Practice
-------------------------------------------

*Latin Locus*: :ref:`Distinctio II (pp. 18–30) <dist-02-la>` · *Commentary*: :ref:`Notes on Square-Root Extraction <dist-02-s1-notes>`

.. enunciation::

   Here begins the second distinction, on the finding of square roots of numbers, both integers and fractions, as well as metrological subdivisions.

Because diagonals of rectangles, altitudes of triangles, and sides of regular figures frequently fall upon numbers that are non-square (*numeri non quadrati*), the surveyor must know how to extract square roots both in Hindu-Arabic positional digits (as taught more fully in *Liber Abaci*) and in Pisan subdivisions.

1. **Exact Positional Algorithm**: Drawing upon $(10a + b)^2 = 100a^2 + 20ab + b^2$ :just:`[II. 4] <II.4>`, group the digits in pairs from the right. Subtract the greatest square $a^2$ from the highest pair, double the root found ($20a$) as divisor for the remainder, determine the next digit $b$ such that $(20a + b)b$ does not exceed the remainder, and continue through all pairs.
2. **First & Second Rational Approximations for Surds**: When a remainder $r = N - a^2 > 0$ remains after the integer part $a$, the root lies strictly between $a + \frac{r}{2a + 1}$ and $a + \frac{r}{2a}$. Taking $a_1 = a + \frac{r}{2a}$, its square exceeds $N$ by $\left(\frac{r}{2a}\right)^2$; subtracting $\frac{(r / 2a)^2}{2 a_1}$ yields a second rational convergent accurate to small fractions of an *uncia*:

   $$a_2 = a_1 - \frac{a_1^2 - N}{2 a_1}.$$

3. **Roots of Agrarian Fractions**: To find the side of a square plot whose area is $\frac{2}{3}$ of a superficial *pertica*, reduce $\frac{2}{3}$ *pertica* to unit squares: $\frac{2}{3} \times 36 = 24$ *denarii* (square *pedes*), or $24 \times 324 = 7{,}776$ square *unciae*. Since $88^2 = 7{,}744$ and $88$ linear *unciae* equal $4$ *pedes* and $16$ *unciae* (with remainder $32$, giving $\frac{32}{176} = \frac{2}{11}$ *uncia*), the side of the square plot is $4$ *pedes* and $16\frac{2}{11}$ *unciae*.

.. qed::

   Thus the surveyor is equipped with both geometrical demonstration and arithmetical root extraction before entering upon the measurement of all planar fields.
