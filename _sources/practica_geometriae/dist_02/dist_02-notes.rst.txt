:title: NOTES — DISTINCTIO II: EXTRACTION OF SQUARE ROOTS
:layout: book
:order: 2
:tracks: English: dist_02-en | Latin: dist_02-la | Summary: dist_02-summary | Notes: dist_02-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0025
:excerpt: Philological and mathematical commentary on square root algorithms, Heronian convergence, and SymPy exact rational evaluation.

.. _dist-02-notes:
.. _unit-1-s4-notes:

NOTES — DISTINCTIO II: EXTRACTION OF SQUARE ROOTS
=================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-02-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-02-la>` · :ref:`Summary <dist-02-summary>`

----

.. _dist-02-s1-notes:

Section 1: The Positional and Heronian Convergence Lineage
----------------------------------------------------------

Leonardo's square root method in Distinctio II represents a synthesis of three ancient traditions:

1. **Indian and Arabic Positional Arithmetic**: Derived from :person:`al-Khwārizmī <al-khwarizmi>` and Indian dust-board reckoning, utilizing digit pairing from the units place.
2. **Heronian Mean Iteration**: Formulated in :person:`Hero of Alexandria <heron>`'s *Metrica* I. 8 (:cite:`heron:metrica`):

   .. math::

      x_{n+1} = \frac{1}{2}\left(x_n + \frac{N}{x_n}\right).

3. **Duodecimal Pisan Scaling**: Exact integer scaling into *denarii* (:math:`36 = 6^2`) and square *unciae* (:math:`324 = 18^2`), ensuring that irrational roots can be expressed to arbitrary precision in native surveyor's subdivisions.

Exact verification in SymPy:

.. code-block:: python

   import sympy as sp

   def fibonacci_sqrt_step(n, a1):
       return a1 - (a1**2 - n) / (2 * a1)

   N = sp.Integer(10)
   a0 = sp.Integer(3)
   a1 = a0 + sp.Rational(1, 6)  # 19/6
   a2 = fibonacci_sqrt_step(N, a1)
   assert a2 == sp.Rational(721, 228)
   assert abs(float(a2) - float(sp.sqrt(10))) < 3e-5
