:title: UNIT IV NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
:layout: book

.. _unit-4-notes:

UNIT IV NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
===============================================

.. rubric:: *From Fibonacci's Sphere of Diameter Six to Piero della Francesca and Luca Pacioli's De Divina Proportione*

:ref:`English Edition <unit-4-en>` · :ref:`Latin (1220 / Boncompagni 1862) <unit-4-la>` · :ref:`Summary <unit-4-summary>`

----

.. _unit-4-s1-notes:

1. Cube-Root Extraction & the $3a(a+1)+1$ Finite Difference
-----------------------------------------------------------

Why does Leonardo divide the cubic remainder $R = N - a^3$ by $3a(a+1) + 1$? Because the exact discrete difference between consecutive integer cubes is:

$$(a + 1)^3 - a^3 = 3a^2 + 3a + 1 = 3a(a + 1) + 1.$$

Thus linear interpolation of $x \mapsto x^3$ across the unit interval $[a, a+1]$ yields the exact secant lower bound $a + \frac{R}{3a(a+1)+1} < \sqrt[3]{a^3 + R} < a + \frac{R}{3a^2}$.

----

.. _unit-4-s2-notes:

2. The Egyptian–Euclidean Frustum Formula
-----------------------------------------

Leonardo's truncated-pyramid formula $V = \frac{h}{3}(B_1 + \sqrt{B_1 B_2} + B_2)$ generalizes the celebrated Moscow Mathematical Papyrus Problem $14$ ($V = \frac{h}{3}(a^2 + ab + b^2)$) from square bases to **any** pair of homothetic planar bases of areas $B_1, B_2$. Since linear similarity factor $\lambda = \sqrt{B_2 / B_1}$ implies $(1 - \lambda^3)/(1 - \lambda) = 1 + \lambda + \lambda^2$, multiplying by $\frac{1}{3} B_1 h$ immediately yields $\frac{h}{3}(B_1 + \sqrt{B_1 B_2} + B_2)$.

----

.. _unit-4-s3-notes:

3. Direct Lineage to Piero della Francesca & Luca Pacioli
---------------------------------------------------------

Modern scholarship (G. Arrighi, M. Clagett, E. Giusti) has established that *Distinctio VI* (Boncompagni Vol. II, pp. 190–202) is the **direct mathematical fountainhead** of Renaissance polyhedral geometry:

* :person:`Piero della Francesca <piero-della-francesca>` transcribed and vernacularized Leonardo's sphere-diameter-$6$ polyhedra calculations into his *Trattato d'abaco* and *Libellus de quinque corporibus regularibus* (c. $1480$);
* :person:`Luca Pacioli <pacioli>` incorporated those exact numerical derivations—retaining $e_{12} = \sqrt{15} - \sqrt{3}$, $af^2 = 6 - \sqrt{7\frac{1}{5}}$, and $hf^2 = 3 + \sqrt{7\frac{1}{5}}$—into *Summa de arithmetica* ($1494$) and *De Divina Proportione* ($1509$, :cite:`pacioli:divina`, cross-referenced in ``geometor/pacioli``).

In ``geometor.fibonacci.polyhedra_golden``, ``polyhedra_in_sphere(6)``, ``construct_sphere_polyhedra_section()``, and ``construct_dodecahedron_golden_chord()`` verify every single radical identity symbolically in SymPy:

* ``sp.simplify((sp.sqrt(15) - sp.sqrt(3))**2 - (18 - sp.sqrt(180))) == 0``;
* ``sp.simplify((V_12 / V_20)**2 - (5 + sp.sqrt(5)) / 6) == 0``, confirming :person:`Hypsicles <hypsicles>`' Book XIV volume ratio ($V_{12} / V_{20} = e_6 / e_{20}$).
