:title: NOTES — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
:layout: book
:order: 4
:tracks: English: dist_04-en | Latin: dist_04-la | Summary: dist_04-summary | Notes: dist_04-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0117
:excerpt: Scholarly commentary on Euclid's lost On Divisions, Savasorda's Hebrew treatise, Archimedes' statics, and SymPy verification.

.. _dist-04-notes:
.. _unit-3-notes:

NOTES — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
================================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-04-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-04-la>` · :ref:`Summary <dist-04-summary>`

----

.. _dist-04-s1-notes:
.. _unit-3-s1-notes:

Section 1: Euclid's Lost *On Divisions of Figures* (*De Divisionibus*)
----------------------------------------------------------------------

Distinctio IV is Leonardo's most historically significant transmission. :person:`Euclid <euclid>` composed a specialized treatise *On Divisions of Figures* (:math:`\Pi\epsilon\rho\grave{\iota}\ \delta\iota\alpha\iota\rho\acute{\epsilon}\sigma\epsilon\omega\nu\ \beta\iota\beta\lambda\acute{\iota}o\nu`), referenced by :person:`Proclus <proclus>` but lost in the original Greek. Leonardo's text preserved the Euclidean methods for medieval Europe alongside :person:`Abraham bar Hiyya <savasorda>` (Savasorda, *Hibbur ha-Meshihah ve-ha-Tishboret*, translated into Latin as *Liber Embadorum* in 1145 by :person:`Plato of Tivoli <plato-of-tivoli>`).

----

.. _dist-04-s2-notes:
.. _unit-3-s2-notes:

Section 2: Semicircle Mean Proportional & Euclid VI. 19
-------------------------------------------------------

To divide a triangle parallel to its base in ratio :math:`p : q`, Leonardo relies on [VI. 19]: similar plane figures have areas in the duplicate ratio of corresponding sides. The semicircle chord construction :math:`AL = \sqrt{AM \cdot AB}` solves the mean proportional :math:`AB : AL = AL : AM` mechanically using compass and straightedge, producing quadratic irrationals (:math:`\sqrt{50}, \sqrt{72}, \sqrt{98}`) with zero numerical floating-point error.

Exact symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import construct_triangle_parallel_division
   import sympy as sp

   par = construct_triangle_parallel_division(p=1, q=1, preset="10-14-12")
   assert par.ae_quadrance == sp.Integer(50)
   assert par.az_quadrance == sp.Integer(72)
   assert par.ez_quadrance == sp.Integer(98)
   assert sp.simplify(par.area_aez - par.area_ebgz) == 0

----

.. _dist-04-s3-notes:
.. _unit-3-s3-notes:

Section 3: Centroid Partition & Archimedes' Statics
---------------------------------------------------

The concurrency of the three medians at :math:`X(2)` and the resulting three equal area shares (:math:`\Delta_1 = \Delta_2 = \Delta_3 = \frac{1}{3} \Delta`) connects Euclidean geometry directly to :person:`Archimedes <archimedes>`' *On the Equilibrium of Planes* I. 14. Leonardo proves concurrency purely through planar Euclidean transformations, without requiring the center of gravity apparatus.
