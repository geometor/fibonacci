:type: notes
:title: NOTES — DISTINCTIO V: EXTRACTION OF CUBE ROOTS
:layout: book
:order: 5
:folio: boncompagni_1862_vol2_practica_geometriae:0155
:excerpt: Philological and mathematical commentary on cube-root algorithms, the Liber Abaci connection, and SymPy evaluation.

.. _dist-05-notes:
.. _unit-4-s1-notes:

NOTES — DISTINCTIO V: EXTRACTION OF CUBE ROOTS
==============================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-05-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-05-la>` · :ref:`Summary <dist-05-summary>`

----

.. _dist-05-s1-notes:

Section 1: The Connection to *Liber Abaci* Chapter XIV
------------------------------------------------------

In his opening sentences, Leonardo explicitly notes that he had already authored a comprehensive treatise on cube roots in the *Liber Abaci* (Chapter XIV, *De reperiendis radicibus quadratis et cubitis*), which he incorporates here so that *Practica Geometriae* may stand as a completely self-contained work.

The mathematical lineage traces back to:

1. **Euclid's Elements Book XI**: Spatial definitions of the cube, parallelepiped, and corporeal solids.
2. **Hero of Alexandria**: *Metrica* III. 20, providing the earliest known rational approximation for non-cube numbers.
3. **Arabic Algebra**: :person:`al-Khwārizmī <al-khwarizmi>` and Indian astronomers who perfected positional triad extraction on sand boards.

Symbolic verification in SymPy:

.. code-block:: python

   import sympy as sp

   def fibonacci_cube_approx(N):
       a = int(N**(1/3))
       R = N - a**3
       denom = 3 * a * (a + 1) + 1
       return sp.Rational(a) + sp.Rational(R, denom)

   # Approximation for cube root of 30: 3^3 = 27, R = 3
   root_30 = fibonacci_cube_approx(30)
   assert root_30 == 3 + sp.Rational(3, 37)  # 114/37 ≈ 3.081
   assert abs(float(root_30)**3 - 30) < 0.3
