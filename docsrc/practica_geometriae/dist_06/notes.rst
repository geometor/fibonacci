:type: notes
:title: NOTES — DISTINCTIO VI: SOLID MENSURATION & THE FIVE REGULAR POLYHEDRA
:layout: book
:order: 6
:folio: boncompagni_1862_vol2_practica_geometriae:0165
:excerpt: Philological commentary on Euclid Book XIII, Piero della Francesca, Luca Pacioli, and SymPy exact verification.

.. _dist-06-notes:
.. _unit-4-notes:

NOTES — DISTINCTIO VI: SOLID MENSURATION & THE FIVE REGULAR POLYHEDRA
======================================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-06-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-06-la>` · :ref:`Summary <dist-06-summary>`

----

.. _dist-06-s2-notes:
.. _unit-4-s2-notes:

Section 1: Archimedes' *On the Sphere and Cylinder*
---------------------------------------------------

The ratio of the sphere to the circumscribed cylinder (:math:`2 : 3`) was discovered by :person:`Archimedes <archimedes>` (:cite:`archimedes:sphere`), who requested it engraved upon his tombstone. Leonardo incorporates the result directly into Pisan cubic metrology (:math:`1 \text{ pertica corporalis} = 216 \text{ cubic feet}`).

----

.. _dist-06-s3-notes:
.. _unit-4-s3-notes:

Section 2: The Direct Source of Piero della Francesca & Luca Pacioli
--------------------------------------------------------------------

Distinctio VI (pp. 190–202) is the fountainhead of Renaissance polyhedral geometry. :person:`Piero della Francesca <piero-della-francesca>` transcribed Leonardo's calculations into his *Libellus de quinque corporibus regularibus* (c. 1482), using the identical sphere of diameter :math:`6`. :person:`Luca Pacioli <pacioli>` then translated Piero's text into Italian and published it in *De Divina Proportione* (Venice, 1509), accompanied by the 60 solid plates drawn by :person:`Leonardo da Vinci <leonardo>`.

Exact symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import polyhedra_in_sphere, verify_hypsicles_xiv_ratio
   import sympy as sp

   solids = polyhedra_in_sphere(6)
   assert solids["tetrahedron"].edge_sq == 24
   assert solids["cube"].edge_sq == 12
   assert solids["octahedron"].volume == 36
   assert sp.simplify(solids["dodecahedron"].edge - (sp.sqrt(15) - sp.sqrt(3))) == 0

   xiv = verify_hypsicles_xiv_ratio(6)
   assert sp.simplify(xiv**2 - (5 + sp.sqrt(5)) / 6) == 0
