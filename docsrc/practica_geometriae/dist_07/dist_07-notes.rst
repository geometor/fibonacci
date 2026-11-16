:title: NOTES — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
:layout: book
:order: 7
:tracks: English: dist_07-en | Latin: dist_07-la | Summary: dist_07-summary | Notes: dist_07-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0209
:excerpt: Philological and mathematical commentary on the medieval quadrans, shadow scales, and optical triangle similarity.

.. _dist-07-notes:
.. _unit-5-s1-notes:

NOTES — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
===================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-07-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-07-la>` · :ref:`Summary <dist-07-summary>`

----

.. _dist-07-s1-notes:

Section 1: The Quadrans Shadow Scale & Arabic Astrolabes
--------------------------------------------------------

The $12 \times 12$ *puncta* shadow scale (*scala altimetrica* or *quadratum umbrae*) on the back of the medieval astrolabe and quadrant derives from Islamic astronomy (al-Khwārizmī, al-Battānī). Leonardo calls the instrument both :term:`quadrans` and *oroscopus*. By defining:

* *Umbra recta* (horizontal shadow, cotangent scale): for angles between $45^\circ$ and $90^\circ$;
* *Umbra versa* (vertical shadow, tangent scale): for angles between $0^\circ$ and $45^\circ$;

the surveyor computes elevations purely through rational proportions of the $12$-point scale without trigonometric tables.

Exact symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import construct_quadrans_surveying

   quad = construct_quadrans_surveying()
   # Validates zero floating-point operations in model construction
