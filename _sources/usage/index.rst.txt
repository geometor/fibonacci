:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Four-Track Codex & Exact Symbolic Constructions

The GEOMETOR edition of Leonardo Pisano's :cite:`*Practica Geometriae* <boncompagni_1862>` unites archival fidelity to Baldassarre Boncompagni's 1862 critical Latin edition with synchronized modern translations and exact constructive geometry.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Every unit across the five codex sections provides synchronized parallel tracks accessible directly from the reading header:
   
   * **English Translation:** Direct modern English translation preserving historical Pisan terminology and Euclidean deductive structure.
   * **Latin Witness:** Verbatim Latin text from :person:`Baldassarre Boncompagni <boncompagni>`'s 1862 Rome edition (*Scritti di Leonardo Pisano*, Vol. II).
   * **Summary:** Chapter summaries, formal propositions, and structural overview.
   * **Scholarly & Mathematical Notes:** Detailed commentary on Pisan agrarian metrology, mathematical lemmas, and historical transmission.

2. Primary-Source Folio Milestones
   Marginal page and folio markers (such as ``[p. 1]``, ``[fol. 18v]``, ``[p. 110]``) link directly to high-resolution folio scans in the repository's archival assets. Clicking header **Folio** badges opens the corresponding Boncompagni scan.

3. Interactive Diagrams & Deductive Links
   All geometric figures are rendered as scalable, theme-adaptive ``.euclid-graphic`` SVGs:
   
   * Triangles, division points, and inscribed Platonic solids adapt dynamically to light and dark reader modes.
   * Terms like :term:`pertica`, :term:`cathetus`, and :term:`media et extrema proportio <media-et-extrema-proportio>` link into the technical glossary.
   * Citations connect directly to foundational sources including :cite:`Euclid's *Elements* <euclid_elements>`, :cite:`Heron's *Metrica* <heron_metrica>`, and :cite:`Pacioli's *De Divina Proportione* <pacioli_1509>`.

4. Full-Text Search with In-Page Highlighting
   Use the sidebar search bar to query the complete Latin transcriptions, English translations, and critical apparatus. Clicking any result automatically opens the section with the search term highlighted in context.

5. Faceted Navigation & Collection Views
   Browse mathematical units, topics, and historical figures via the sidebar taxonomy. Collection pages provide **Cards**, **Banners**, and **List** layout switches.

6. People, Bibliography & Glossary Tooltips
   Hovering over any historical person (:person:`Leonardo Pisano <fibonacci>`, :person:`Master Dominicus <dominicus>`, :person:`Frederick II <frederick-ii>`, :person:`Luca Pacioli <pacioli>`), citation (:cite:`boncompagni_1862`), or term (:term:`stariorum`, :term:`congruum`, :term:`quadrans`) surfaces rich tooltip cards.

----

Command-Line & Python Verification API
--------------------------------------

All constructions, Pisan metrological decompositions, and Platonic solid radical towers are executable locally via Python.

Running Demonstrations
~~~~~~~~~~~~~~~~~~~~~~

Run the exact symbolic demonstration scripts directly from the repository root:

.. code-block:: bash

   # Verify Pisan pertica metrology, Heron's incenter proof & 96-gon circle bounds
   python3 demos/mensuration_demo.py

   # Verify Euclidean triangle field divisions and 3-consort centroid partition
   python3 demos/divisions_demo.py

   # Inscribe the five Platonic solids in a sphere of diameter 6
   python3 demos/polyhedra_golden_demo.py

Python API Usage
~~~~~~~~~~~~~~~~

Import the symbolic engine directly into interactive Python or Jupyter notebooks:

.. code-block:: python

   import sympy as sp
   from geometor.fibonacci import (
       construct_heron_incenter_proof,
       polyhedra_in_sphere,
       fibonacci_circle_bounds,
   )

   # Exact Heron incenter construction on (13, 14, 15)
   proof = construct_heron_incenter_proof()
   assert proof.area == sp.Integer(84)
   assert proof.inradius == sp.Integer(4)

   # Five Platonic solids in a sphere of diameter 6
   solids = polyhedra_in_sphere(6)
   print("Dodecahedron edge:", solids["dodecahedron"].edge)
   print("Dodecahedron volume:", solids["dodecahedron"].volume)
