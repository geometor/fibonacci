:title: UNIT III NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
:layout: book

.. _unit-3-notes:

UNIT III NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
================================================

.. rubric:: *Euclid's Lost On Divisions, Centroid X(2), and Exact Symbolic Constructions in geometor.fibonacci.divisions*

:ref:`English Edition <unit-3-en>` · :ref:`Latin (1220 / Boncompagni 1862) <unit-3-la>` · :ref:`Summary <unit-3-summary>`

----

.. _unit-3-s1-notes:

1. Reconstructing Euclid's Lost *On Divisions of Figures*
---------------------------------------------------------

Mentioned by :person:`Proclus <euclid>` in his *Commentary on Book I* (`geometor/proclus`), Euclid's *On Divisions of Figures* vanished in Greek antiquity. In $1851$, Franz Woepcke discovered an Arabic epitome in Paris (MS Suppl. ar. 952.2) giving the enunciations of $36$ propositions and proofs of only four; in $1915$, R. C. Archibald demonstrated (:cite:`euclid:divisions`) that **Leonardo Pisano's *Distinctio IV* ($1220$) preserves the missing Euclidean proofs**—translated from an unabridged Arabic or Greco-Latin archetype—together with Leonardo's own algebraic extensions to 3-, 4-, and 5-part consortium divisions.

In ``geometor.fibonacci.divisions.construct_triangle_side_point_division()``, the boundary-point construction on $(13, 14, 15)$ with $D = (5, 0)$ executes strictly via compass-and-straightedge primitives (`auto_intersect=False`):

* Base midpoint $E = (7, 0)$;
* Parallel $[EZ] \parallel [AD]$ meeting $[GA]$ at $Z = \left(\frac{19}{9}, \frac{60}{9}\right) = \left(\frac{19}{9}, \frac{20}{3}\right)$;
* Rational quadrance $Q(G, Z) = \frac{1225}{9} = \left(\frac{35}{3}\right)^2$, confirming $GZ = 11\frac{2}{3}$ and $\text{Area}(\triangle DZG) = \frac{1}{2} \times 9 \times \frac{28}{3} = 42 = \frac{1}{2}(84)$.

----

.. _unit-3-s2-notes:

2. Early Latin Proof of Median Concurrency at $X(2)$
----------------------------------------------------

Euclid's *Elements* never explicitly states that the three medians of a triangle concur! While :person:`Archimedes <archimedes>` used the center of gravity in *On the Equilibrium of Planes*, Leonardo's *Preparatoria* (Boncompagni Vol. II, pp. 112–113) gives a purely planar, non-mechanical similarity proof via the midline $EZ = \frac{1}{2} AB$—making *Practica Geometriae* a foundational landmark for Kimberling center `X(2)` (`geometor/etc`).

In ``construct_triangle_medians_centroid()``, for $B = (0, 0)$, $G = (14, 0)$, $A = (5, 12)$:

* $D = X(2) = \left(\frac{19}{3}, 4\right)$;
* Exact Rational Trigonometry quadrance ratios confirm $Q(A, D) = 4\,Q(D, E) = \frac{592}{9}$, $Q(B, D) = 4\,Q(D, Z) = \frac{505}{9}$, and $Q(G, D) = 4\,Q(D, T) = \frac{673}{9}$;
* Signed determinant areas verify $\Delta(DAB) = \Delta(DBG) = \Delta(DGA) = 28$.

----

.. _unit-3-s3-notes:

3. Quadratic Scaling Over $\mathbb{Q}(\sqrt{2})$ & Babylonian Root-Mean-Square
------------------------------------------------------------------------------

In ``construct_triangle_parallel_division()``, bisecting $\triangle(10, 14, 12)$ parallel to base $BG = 14$ places every constructed intersection in $\mathbb{Q}(\sqrt{2}, \sqrt{6})$ without a single floating-point operation:

* Semicircle mean proportional gives $AE = 5\sqrt{2}$ ($Q(A, E) = 50$), $AZ = 6\sqrt{2}$ ($Q(A, Z) = 72$), and parallel cut $EZ = 7\sqrt{2}$ ($Q(E, Z) = 98$), matching Boncompagni Vol. II, p. 119 digit for digit.

Likewise, ``trapezoid_parallel_division(top_base_a=7, bottom_base_b=17, height=10, p=1, q=1)`` recovers the ancient Babylonian surveyor's triad $(7, 13, 17)$ satisfying $7^2 + 17^2 = 2 \times 13^2$—linking Old Babylonian clay tablets (such as YBC 4675), Euclid's *On Divisions*, and medieval Pisan cadastral practice across three millennia.
