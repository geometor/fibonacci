:type: notes
:title: NOTES — DISTINCTIO I: PROLOGUE, PISAN METROLOGY & RECTANGULAR FIELDS
:layout: book
:order: 1
:folio: boncompagni_1862_vol2_practica_geometriae:0008
:excerpt: Philological and mathematical commentary on Fibonacci's prologue, Dominicus, Pisan metrology, and SymPy verification.

.. _dist-01-notes:
.. _unit-1-notes:

NOTES — DISTINCTIO I: PROLOGUE, PISAN METROLOGY & RECTANGULAR FIELDS
====================================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-01-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-01-la>` · :ref:`Summary <dist-01-summary>`

----

.. _dist-01-s1-notes:
.. _unit-1-s1-notes:

Section 1: The Dedication to Master Dominicus
---------------------------------------------

The recipient of *Practica Geometriae*, :person:`Master Dominicus <dominicus>` (*Dominicus magister*), was a prominent scholar and imperial notary in Pisa during the court visits of Emperor :person:`Frederick II <frederick-ii>`. Leonardo characterizes his work as harmonizing two traditions:

1. **Demonstrative Geometrical Theory**: Rooted in :person:`Euclid <euclid>`'s *Elements* (:cite:`euclid:elements`) and :person:`Archimedes <archimedes>`' circle quadrature.
2. **Lay Practical Measurement**: The operational practice of surveyors (*secundum vulgarem consuetudinem, quasi laicali more*).

----

.. _dist-01-s2-notes:
.. _unit-1-s2-notes:

Section 2: The Pisan 6 × 6 Pertica System
-----------------------------------------

Unlike modern metric or pure decimal systems, medieval Italian land mensuration utilized a mixed radix lattice. The Pisan system was governed by:

* :math:`1 \text{ pertica} = 6 \text{ pedes}`
* :math:`1 \text{ pes} = 18 \text{ unciae}` (points)
* :math:`1 \text{ pertica} = 108 \text{ unciae}`
* :math:`1 \text{ pertica superficialis} = 36 \text{ denarii} = 36 \text{ sq. pedes}`
* :math:`1 \text{ panorum} = 5\frac{1}{2} \text{ perticae} = 198 \text{ denarii}`
* :math:`1 \text{ stariorum} = 12 \text{ panora} = 66 \text{ perticae} = 2{,}376 \text{ denarii}`

Exact symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import PisanLinearMeasure, multiply_pisan_lengths, decompose_pisan_area
   import sympy as sp

   width = PisanLinearMeasure(perticae=7)
   depth = PisanLinearMeasure(perticae=9, pedes=2, unciae=sp.Rational(72, 7))
   prod = multiply_pisan_lengths(width, depth)
   assert prod.total_perticae == sp.Integer(66)
   assert prod.stariora == 1

----

.. _dist-01-s3-notes:
.. _unit-1-s3-notes:

Section 3: Geometric Algebra of Book II
---------------------------------------

Leonardo embeds :person:`Euclid <euclid>`'s Book II propositions directly into the surveyor's art. Proposition [II. 4] gives the algebraic basis for rectangular expansions :math:`(a + b)^2 = a^2 + 2ab + b^2`, while [II. 5–6] provide the geometric foundation for solving quadratic equations by completing the square without symbolic notation.
