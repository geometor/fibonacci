:type: notes
:title: NOTES — DISTINCTIO VIII: SUBTILITATES GEOMETRICAE & FLOS (1225)
:layout: book
:order: 8
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

Leonardo's algebraic treatment of the pentagon is modeled on :person:`Abū Kāmil Shujāʿ ibn Aslam <abu-kamil>` (*On the Pentagon and Decagon*). Setting :math:`x` for *res*, :math:`x^2` for :term:`census`, and :math:`x^4` for *census census*, he gives the earliest complete Latin demonstration of a biquadratic equation in Euclidean geometry.

Exact symbolic verification in ``geometor.fibonacci``:

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

In 1225, Emperor :person:`Frederick II <frederick-ii>` visited Pisa with court philosopher :person:`Master John of Palermo <john-of-palermo>`, who proposed two challenges:

1. **The Congruum Problem**: Solved using :math:`C = 4mn(m^2 - n^2)` with :math:`(m, n) = (5, 4)`, yielding :math:`C = 720` and :math:`x = \frac{41}{12}`.
2. **The Cubic Equation**: :math:`x^3 + 2x^2 + 10x = 20`, proven irreducible over Euclid Book X quadratic irrationals.

Symbolic verification in ``geometor.fibonacci``:

.. code-block:: python

   from geometor.fibonacci import flos_congruum_squares, flos_sexagesimal_cubic
   import sympy as sp

   cong_a, cong_x, cong_b = flos_congruum_squares()
   assert cong_x**2 - 5 == cong_a**2
   assert cong_x**2 + 5 == cong_b**2

   cubic = flos_sexagesimal_cubic()
   assert cubic.rational_root == sp.Rational(1_596_577_777, 1_166_400_000)
   assert float(cubic.abs_root_error.evalf()) < 4e-11

**Textual Witness Note**: Boncompagni Vol. II, pp. 207–224 (fol. 134r–146r) contains *Distinctio VIII*; p. 218 preserves the rubric noting the triangle problems belong after the equilateral-triangle problem in the preceding quire. Pages 227–234 contain the *Flos* prologue to Cardinal R., the congruum, and the cubic proof.
