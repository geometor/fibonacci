:title: NOTES — DISTINCTIO VIII: SUBTILITATES GEOMETRICAE & FLOS (1225)
:layout: book
:order: 8
:tracks: English: dist_08-en | Latin: dist_08-la | Summary: dist_08-summary | Notes: dist_08-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0214
:excerpt: Philological commentary on Abu Kamil's algebra, Ptolemy's theorem, Euclid Book X irrationals, and the imperial court contest of 1225.

.. _dist-08-notes:
.. _unit-5-notes:

NOTES — DISTINCTIO VIII: SUBTILITATES GEOMETRICAE & FLOS (1225)
===============================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-08-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-08-la>` · :ref:`Summary <dist-08-summary>`

----

.. _dist-08-s2-notes:
.. _unit-5-s2-notes:

Section 1: The Influence of Abū Kāmil's *On the Pentagon and Decagon*
---------------------------------------------------------------------

Leonardo's algebraic treatment of the pentagon is directly modeled on the 9th-century Egyptian master :person:`Abū Kāmil Shujāʿ ibn Aslam <abu-kamil>` (*Kitāb fī al-jabr wa-al-muqābala* and *On the Pentagon and Decagon*). By setting $x$ for the side, $x^2$ for :term:`census`, and $x^4$ for *census census*, Leonardo introduces the earliest complete Latin demonstration of a biquadratic algebraic equation applied to classical Euclidean geometry.

Exact symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import construct_pentagon_decagon_in_circle, solve_pentagon_ptolemy_quartic, PHI
   import sympy as sp

   pent = construct_pentagon_decagon_in_circle()
   alg_side, alg_diag = solve_pentagon_ptolemy_quartic(10)
   assert sp.simplify(alg_side - pent.pentagon_side) == 0
   assert sp.simplify(alg_diag / alg_side - PHI) == 0

----

.. _dist-08-s3-notes:
.. _unit-5-s3-notes:

Section 2: The 1225 Imperial Mathematical Contest in Pisa
---------------------------------------------------------

In 1225, Emperor :person:`Frederick II <frederick-ii>` visited Pisa with his court philosopher :person:`Master John of Palermo <john-of-palermo>`. John proposed two famous challenge problems:

1. **The Congruum Problem**: Solved by Fibonacci using the congruum identity $C = 4mn(m^2 - n^2)$ with generator pair $(m, n) = (5, 4)$, yielding $C = 720$ and the rational solution $x = \frac{41}{12}$.
2. **The Cubic Equation**: $x^3 + 2x^2 + 10x = 20$. Leonardo's geometric proof that this equation has no solution among the rational numbers or the quadratic irrationals of Euclid's Book X represents the high-water mark of medieval European algebra, three centuries before Cardano and Tartaglia.

Symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import flos_congruum_squares, flos_sexagesimal_cubic
   import sympy as sp

   cong_a, cong_x, cong_b = flos_congruum_squares()
   assert cong_x**2 - 5 == cong_a**2
   assert cong_x**2 + 5 == cong_b**2

   cubic = flos_sexagesimal_cubic()
   assert cubic.rational_root == sp.Rational(1_596_577_777, 1_166_400_000)
   assert float(cubic.abs_root_error.evalf()) < 4e-11
