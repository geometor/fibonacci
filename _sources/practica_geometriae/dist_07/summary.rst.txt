:type: summary
:title: SUMMARY — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
:layout: book
:order: 7
:folio: boncompagni_1862_vol2_practica_geometriae:0209
:excerpt: Mathematical decomposition of the 12x12 shadow square, optical triangle similarity, and altimetric surveying.

.. _dist-07-summary:

SUMMARY — DISTINCTIO VII: SURVEYING WITH THE QUADRANS
=====================================================

.. rubric:: *Mathematical Apparatus and Altimetric Formulations*

:ref:`English Edition <dist-07-en>` · :ref:`Latin (1220 / Boncompagni 1862) <dist-07-la>` · :ref:`GEOMETOR Notes <dist-07-notes>`

----

Shadow Square Trigonometry
--------------------------

Let :math:`D` be the sighting apex, :math:`h_e` the eye height above the ground, :math:`D_{\text{base}}` the horizontal distance to the tower base, and :math:`H` the total height:

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Plumb Line Sighting
     - Puncta Reading
     - Altimetric Formula
   * - Diagonal (:math:`45^\circ`)
     - 12 puncta (:math:`DA` line)
     - :math:`H = D_{\text{base}} + h_e`
   * - Umbra Recta (:math:`p`)
     - :math:`p` puncta on horizontal side (:math:`p < 12`)
     - :math:`H = \frac{12}{p} \cdot D_{\text{base}} + h_e`
   * - Umbra Versa (:math:`v`)
     - :math:`v` puncta on vertical side (:math:`v < 12`)
     - :math:`H = \frac{v}{12} \cdot D_{\text{base}} + h_e`

----

Canonical Problem: Steep Tower Sighting
---------------------------------------

* **Given**: Distance to tower :math:`D_{\text{base}} = 40` perticae, observer eye-height :math:`h_e = 1` pertica, plumb line reading on *umbra recta* :math:`p = 8` puncta (out of 12).
* **Compute**:

  .. math::

     \text{Elevation} = \frac{12}{8} \times 40 = \frac{3}{2} \times 40 = 60 \text{ perticae}, \qquad H = 60 + 1 = 61 \text{ perticae}.
