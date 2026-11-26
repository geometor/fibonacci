:title: NOTES — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
:layout: book
:order: 3
:tracks: English: dist_03-en | Latin: dist_03-la | Summary: dist_03-summary | Notes: dist_03-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0037
:excerpt: Scholarly commentary on Heron's formula, the Banu Musa Arabic transmission, Archimedes' circle quadrature, and SymPy verification.

.. _dist-03-notes:
.. _unit-2-notes:

NOTES — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
============================================================================

.. rubric:: *Philological Commentary, Classical Lineage, and Exact Symbolic Verification*

:ref:`English Edition <dist-03-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-03-la>` · :ref:`Summary <dist-03-summary>`

----

.. _dist-03-s1-notes:
.. _unit-2-s1-notes:

Section 1: The (13, 14, 15) Scalene Benchmark & Rational Trigonometry
---------------------------------------------------------------------

Triangle :math:`(13, 14, 15)` is the canonical medieval Heronian triangle. Its perpendicular altitude splits base :math:`14` into rational segments :math:`5` and :math:`9`, creating two adjacent integer right triangles :math:`(5, 12, 13)` and :math:`(9, 12, 15)`. Leonardo uses this rational decomposition to demonstrate both the Euclidean *casus* method [II. 13] and the semiperimeter product rule.

----

.. _dist-03-s2-notes:
.. _unit-2-s2-notes:

Section 2: The Transmission of Heron's Proof via the Banū Mūsā
--------------------------------------------------------------

While the formula :math:`\Delta = \sqrt{s(s-a)(s-b)(s-c)}` originated with :person:`Hero of Alexandria <heron>` (*Metrica* I. 8), Hero's Greek text was lost to medieval Europe until Schöne's 1896 discovery in Constantinople. Leonardo received the proof through :person:`Gerard of Cremona <gerard-of-cremona>`'s 12th-century Latin translation of the *Verba Filiorum* of the :person:`Banū Mūsā <banu-musa>` (:cite:`banu-musa:verba`). Leonardo's exposition is clearer than the Arabic-Latin translation, emphasizing the incenter :math:`T` and the semiperimeter line :math:`BL`.

Symbolic verification in `geometor.fibonacci`:

.. code-block:: python

   from geometor.fibonacci import heron_area_exact, construct_heron_incenter_proof

   s, exc, sq, area = heron_area_exact(13, 14, 15)
   assert s == 21
   assert exc == (8, 7, 6)
   assert area == 84

   proof = construct_heron_incenter_proof()
   assert proof.incenter_t.x == 6
   assert proof.incenter_t.y == 4
   assert proof.inradius == 4

----

.. _dist-03-s3-notes:
.. _unit-2-s3-notes:

Section 3: Quadrilateral Fallacies & Agromensorial Caution
----------------------------------------------------------

Leonardo issues a sharp warning against Roman *agrimensores* who computed quadrilateral areas by :math:`\frac{a+c}{2} \cdot \frac{b+d}{2}`. He proves by [I. 28] and [I. 41] that this formula is strictly an upper bound, yielding exact results if and only if the quadrilateral is rectangular.

----

.. _dist-03-s4-notes:
.. _unit-2-s4-notes:

Section 4: The 96-gon Bounds & Fibonacci's Ratio 864 : 275
----------------------------------------------------------

In demonstrating :person:`Archimedes <archimedes>`' circle bounds (:cite:`archimedes:circle`), Leonardo avoids large 5-digit square roots by scaling diameter :math:`d = 1440` (:math:`r = 720`). His harmonic mean:

.. math::

   \frac{1440}{458\frac{1}{3}} = \frac{864}{275} \approx 3.141818\dots

yields an approximation whose error is under :math:`0.007\%`, closer to :math:`\pi` than Archimedes' upper bound :math:`\frac{22}{7} \approx 3.142857`.
