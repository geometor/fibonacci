:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _about-fibonacci:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

*GEOMETOR fibonacci* reconstructs the mathematical corpus of :person:`Leonardo Pisano <fibonacci>` (*c.* 1170 – *c.* 1245), widely known as Fibonacci, focusing primarily on his monumental 1220 treatise *Practica Geometriae* alongside foundational passages from *Liber Abaci* (1202/1228) and the cubic solution in *Flos* (1225). Writing in medieval Pisa after traveling throughout North Africa, Egypt, Syria, and Greece, Leonardo synthesized Arabic algebraic techniques with Euclidean axiomatic rigor. His work preserves the primary Latin transmission of Euclid's lost monograph *On Divisions of Figures* (Distinctio IV), Archimedean polygon-bounding techniques for circle quadrature, Heron's incenter proof of triangular area, and Euclidean regular polyhedra inscriptions linked to the golden ratio.

Every distinctio, field division case, surveying problem, and geometric construction has been extracted into addressable semantic elements. Grounded in :person:`Baldassarre Boncompagni <boncompagni>`'s nineteenth-century critical Latin text (*Scritti di Leonardo Pisano*, Vol. I, 1857; Vol. II, 1862), each unit is presented across four synchronized tracks: diplomatic Latin (*littera*), an original GEOMETOR English translation, a pedagogical summary, and detailed scholarly notes. Historical geometric figures have been reconstructed as calibrated, resolution-independent vector graphics, and every calculation—from Pisan agrarian metrology to polynomial approximations—is verified to exact symbolic truth in :mod:`sympy`.

This edition forms a crucial connective nexus across the GEOMETOR library. It directly bridges the classical Greek foundations of :cite:`Euclid's Elements <euclid_elements>` and Heron of Alexandria's *Metrica* with the Renaissance resurgence of perspective and golden ratio geometry in :person:`Piero della Francesca <piero-della-francesca>` and :person:`Luca Pacioli <pacioli>`'s *De Divina Proportione* (1509). By transforming medieval algorithmic geometry into executable symbolic workflows, this edition recovers the deductive lineage uniting ancient Greece, medieval Islam, and the Italian Renaissance.

The GEOMETOR Mission
--------------------

Founded and directed by **phi ARCHITECT**, the GEOMETOR initiative is dedicated to the systematic digitization, symbolic formalization, and multi-medium re-articulation of classical geometric and axiomatic literature across 2,300+ years of mathematical history. GEOMETOR bridges historical philology and modern computational geometry through three structural pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and lossy optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of classical, Renaissance, and modern mathematical treatises. Enunciations, geometric constructions, proof steps, axiomatic justifications, marginal citations, primary-source folios (rendered dynamically through ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams are converted into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Eliminating floating-point approximation errors entirely, GEOMETOR anchors geometric constructions and center proofs in 100% exact symbolic algebra via :mod:`sympy` and Rational Trigonometry invariants (quadrance, spread, cross-ratio) evaluated over exact algebraic number fields. Every center, line concurrence, circle intersection, and tangency condition is verified to exact symbolic zero.

Repurposing Knowledge Across Mediums
    Extracted semantic and algebraic models are mobilized across synchronized multi-track Book Codices and EPUB 3 editions via ``photon-platform/publish``, computable deductive canons (:mod:`geometor.elements`, :mod:`geometor.etc`, :mod:`geometor.pappus`, :mod:`geometor.divine`), interactive SVG laboratories (:mod:`geometor.explorer`), high-definition visual broadcasts, and neuro-symbolic program synthesis engines (:mod:`geometor.seer`) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition is established upon the standard nineteenth-century philological monument and verified against medieval codices:

Archival & Published Sources
    * **Baldassarre Boncompagni (ed.)**: *Scritti di Leonardo Pisano matematico del secolo decimoterzo*, Vol. I: *Il Liber Abbaci* (Roma: Tipografia delle Scienze Matematiche e Fisiche, 1857); Vol. II: *La Practica Geometriae ed opuscoli* (*Flos*, *Epistola ad Theodorum*, *Liber Quadratorum*) (Roma, 1862).
    * **Manuscript Witnesses**: Biblioteca Apostolica Vaticana (MS Urb. Lat. 292; Pal. Lat. 1343); Biblioteca Nazionale Centrale di Firenze (MS Conv. Soppr. C. 1. 2616).

Digital Scriptorium Methodology
    * **Four-Track Synchronized Codex**: Readers can inspect each section across parallel tracks: GEOMETOR English translation, diplomatic Boncompagni Latin, synopsis, and scholarly apparatus.
    * **Exact Symbolic Verification**: All field divisions, area formulas, and polyhedral circumradius invariants are computed symbolically via :mod:`geometor.fibonacci.divisions`, :mod:`geometor.fibonacci.mensuration`, and :mod:`geometor.fibonacci.polyhedra_golden`.
    * **Apparatus & Biographical Register**: Detailed cross-references are provided in :doc:`/practica_geometriae/people/index` for historical actors and :doc:`/practica_geometriae/bibliography` for primary and secondary literature.
