:title: UNIT IV — DISTINCTIO V–VI: CUBE ROOTS, SOLIDS & THE FIVE REGULAR POLYHEDRA
:layout: book

.. _unit-4-en:

UNIT IV — DISTINCTIO V–VI: CUBE ROOTS, SOLIDS & THE FIVE REGULAR POLYHEDRA
==========================================================================

.. rubric:: *Cube-Root Extraction, Stereometry of Pyramids & Spheres, and the Five Platonic Solids in Sphere Diameter Six*

**Source Text**: :cite:`fibonacci:pg-5`, :cite:`fibonacci:pg-6` (*Boncompagni Vol. II, pp. 148–202 · fol. 92v–130v*) · :ref:`Latin (1220 / Boncompagni 1862) <unit-4-la>` · :ref:`Summary <unit-4-summary>` · :ref:`GEOMETOR Notes <unit-4-notes>`

----

.. _unit-4-dist5-en:

.. folio:: fol. 92v–99r
   :page: 148–159

Distinctio V — On the Finding of Cube Roots (*De Radicibus Cubicis*)
--------------------------------------------------------------------

*Latin Locus*: :ref:`Distinctio V (pp. 148–159) <unit-4-dist5-la>` · *Commentary*: :ref:`Notes on Cubic Binomial Extraction <unit-4-s1-notes>`

.. enunciation::

   Here begins the Fifth Distinction, on finding cube roots (*de radicibus cubicis inveniendis*), needful for the duplication and comparison of corporeal solids.

Just as square-root extraction rests upon the gnomon $(a + b)^2 = a^2 + 2ab + b^2$, cube-root extraction rests upon the solid dissection of a cube cut into two parts $a$ and $b$:

$$(a + b)^3 = a^3 + 3a^2 b + 3a b^2 + b^3 = a^3 + 3ab(a + b) + b^3.$$

Grouping Hindu-Arabic digits in **triads** ($10^3 = 1{,}000$) from the right, Leonardo subtracts the greatest cube $a^3$ from the leading triad, forms the trial divisor $300 a^2$, determines the next digit $b$ so that $300 a^2 b + 30 a b^2 + b^3$ does not exceed the remainder, and for non-cubic integers $N = a^3 + R$ supplies the rational fractional bound:

$$\sqrt[3]{a^3 + R} \approx a + \frac{R}{3a(a + 1) + 1},$$

followed by multiplication and division of cubic radicals ($\sqrt[3]{p}\cdot\sqrt[3]{q} = \sqrt[3]{pq}$).

----

.. _unit-4-solids-en:

.. folio:: fol. 99v–121v
   :page: 159–190

Distinctio VI (Part 1) — Columns, Pyramids, Frustums & the Sphere
-----------------------------------------------------------------

*Latin Locus*: :ref:`De Dimensione Corporum (pp. 159–190) <unit-4-solids-la>` · *Commentary*: :ref:`Notes on Stereometry & Archimedes' Sphere <unit-4-s2-notes>`

A solid *pertica* (*pertica corporalis*) contains $6 \times 6 \times 6 = 216$ cubic *pedes*. Proceeding from :person:`Euclid <euclid>` Books XI–XII (:cite:`euclid:elements`) and :person:`Archimedes <archimedes>`' *On the Sphere and Cylinder* (:cite:`archimedes:sphere`), Leonardo demonstrates the fundamental stereometric laws:

1. **Prisms & Circular Columns (Cylinders)**: Solid measure equals the planar :term:`embadum` of the base multiplied into the perpendicular height (:term:`cathetus`). :just:`[XI. 31, XII. 11] <XII.11>`
2. **Pyramids & Cones**: Every pyramid (triangular, quadrangular, or multi-angular) and every circular cone is **one-third** of the prism or cylinder sharing the same base and altitude: $V = \frac{1}{3} B h$. :just:`[XII. 7, 10] <XII.7>`
3. **Truncated Pyramids & Conical Frustums** (*Pyramis caput abscisa*): If a pyramid or cone is cut parallel to its base, leaving lower base area $B_1$, upper top area $B_2$, and perpendicular height $h$, its exact volume is one-third the height multiplied into the sum of the two bases and their geometric mean:

   $$V = \frac{h}{3}\!\left(B_1 + \sqrt{B_1 B_2} + B_2\right).$$

4. **The Sphere**: Following :person:`Archimedes <archimedes>` (:cite:`archimedes:sphere`) and the :person:`Banū Mūsā <banu-musa>` (:cite:`banu-musa:verba`), every sphere is **two-thirds** of its circumscribed cylinder (whose base diameter and height both equal the sphere's diameter $d$), and its surface area equals **four times** its greatest circle ($4 \pi r^2 = \pi d^2$). Hence $V_{\text{sphere}} = \frac{1}{6}\pi d^3 \approx \frac{11}{21} d^3$.

----

.. _unit-4-polyhedra-en:

.. folio:: fol. 122r–130v
   :page: 190–202

Distinctio VI (Part 2) — The Five Regular Polyhedra in Sphere Diameter Six
--------------------------------------------------------------------------

*Latin Locus*: :ref:`De Quinque Corporibus Regularibus in Spera (pp. 190–202) <unit-4-polyhedra-la>` · *Commentary*: :ref:`Notes on Euclid XIII, Hypsicles XIV & Pacioli <unit-4-s3-notes>`

.. enunciation::

   To find the sides, surfaces, altitudes, and solid volumes of the five regular bodies of :person:`Euclid <euclid>`'s thirteenth book—namely the **tetrahedron** (4 triangular bases), **cube** (6 square bases), **octahedron** (8 triangular bases), **dodecahedron** (12 pentagonal bases), and **icosahedron** (20 triangular bases)—inscribed within a sphere of given rational diameter $d = 6$. :just:`[XIII. 13–18] <XIII.18>`

.. picture:: /_static/figures/euclid_xiii_sphere_polyhedra.svg
   :alt: Master Construction of the Five Regular Polyhedra in Sphere Diameter 6 (Euclid XIII.18)
   :caption: Euclid XIII.18 master semicircle ( O A ) on sphere diameter AI = 6 (center O, trisection AK = 2): tetrahedron edge / B I / (Q = 24), octahedron edge / A C / (Q = 18), cube edge / A B / (Q = 12), golden cut N giving dodecahedron edge / A N / (Q = 18 - sqrt(180)), and / M I / giving icosahedron edge (Q = 18 - sqrt(64 4/5)).

Let the sphere diameter $AI = 6$ lie along :g:`AK <euclid_xiii_sphere_polyhedra:[ A K ]>` with center :g:`O <euclid_xiii_sphere_polyhedra:O>` ($AO = OI = 3$) and great circle :g:`(OA) <euclid_xiii_sphere_polyhedra:( O A )>`. Cut $AI$ at :g:`K <euclid_xiii_sphere_polyhedra:K>` so that $AK = \frac{1}{3} AI = 2$ and $KI = 4$; erect perpendiculars :g:`KB <euclid_xiii_sphere_polyhedra:/ K B />` and :g:`OC <euclid_xiii_sphere_polyhedra:/ O C />` to meet the semicircle at :g:`B <euclid_xiii_sphere_polyhedra:B>` and :g:`C <euclid_xiii_sphere_polyhedra:C>`. :just:`[XIII. 18] <XIII.18>`

1. **Regular Tetrahedron** (*Pyramis quatuor basium triangularium*, :just:`[XIII. 13] <XIII.13>`):
   Since $BI^2 = AI \cdot KI = \frac{2}{3} d^2$, the tetrahedron edge is :g:`BI <euclid_xiii_sphere_polyhedra:/ B I />` with $e_4^2 = 6 \times 4 = 24$ ($e_4 = \sqrt{24} = 2\sqrt{6}$). Its altitude is $h_4 = 4$, base area $\sqrt{108} = 6\sqrt{3}$, and solid volume $V_4 = \frac{1}{3} \times 4 \times 6\sqrt{3} = 8\sqrt{3} = \sqrt{192}$.
2. **Cube** (*Cubus sex basium quadratarum*, :just:`[XIII. 15] <XIII.15>`):
   Since $AB^2 = AI \cdot AK = \frac{1}{3} d^2$, the cube edge is :g:`AB <euclid_xiii_sphere_polyhedra:/ A B />` with $e_6^2 = 6 \times 2 = 12$ ($e_6 = \sqrt{12} = 2\sqrt{3}$), and its solid volume is $V_6 = 12\sqrt{12} = 24\sqrt{3} = \sqrt{1{,}728} = 3\,V_4$.
3. **Regular Octahedron** (*Octaedrum octo basium triangularium*, :just:`[XIII. 14] <XIII.14>`):
   Since $AC^2 = AO^2 + OC^2 = \frac{1}{2} d^2$, the octahedron edge is :g:`AC <euclid_xiii_sphere_polyhedra:/ A C />` with $e_8^2 = 9 + 9 = 18$ ($e_8 = \sqrt{18} = 3\sqrt{2}$). Composed of two square pyramids of base $e_8^2 = 18$ and combined height $d = 6$, its volume is the **exact rational integer** $V_8 = \frac{1}{3} \times 18 \times 6 = 36$.

----

.. _unit-4-dodeca-en:

.. folio:: fol. 125v–130v
   :page: 196–202

Extreme and Mean Ratio: The Dodecahedron & Icosahedron
------------------------------------------------------

*Latin Locus*: :ref:`Modus Dividendi Lineam Media et Extrema Proportione (pp. 196–202) <unit-4-dodeca-la>` · *Commentary*: :ref:`Notes on the Golden Chord & Hypsicles Book XIV <unit-4-s3-notes>`

To construct the **dodecahedron**, each pentagonal face is crowned upon an inscribed cube whose edge ($e_6 = \sqrt{12}$) serves as the **pentagonal chord (diagonal)** :g:`BE <dodecahedron_golden_chord:[ B G ]>`. Since in every regular pentagon the diagonal and side stand in :term:`extreme and mean ratio <media-et-extrema-proportio>` :just:`[XIII. 8, 17] <XIII.17>`, Leonardo inserts an explicit constructive chapter (*Modus dividendi lineam media et extrema proportione*, p. 196):

.. picture:: /_static/figures/dodecahedron_golden_chord.svg
   :alt: Dividing the Cube Edge BE in Extreme and Mean Ratio for the Dodecahedron Edge
   :caption: Cube edge BE = 2*sqrt(3) divided in extreme and mean ratio: erecting / E C / = 1/2 BE = sqrt(3) via midpoint M and circle ( E M ), cutting hypotenuse [ B D ] (BC = sqrt(15)) with circle ( C E ) at D, and transferring ( B D ) to G yields dodecahedron edge / B G / = / A B / = / A E / = sqrt(15) - sqrt(3).

* **Golden-Section Construction**: Let the given chord $BE = \sqrt{12} = 2\sqrt{3}$ be bisected at :g:`M <dodecahedron_golden_chord:M>`, and by circle :g:`(EM) <dodecahedron_golden_chord:( E M )>` erect at :g:`E <dodecahedron_golden_chord:E>` the perpendicular :g:`EC <dodecahedron_golden_chord:/ E C />` $= EM = \sqrt{3}$. :just:`[II. 11, VI. 30] <VI.30>` Join the hypotenuse :g:`BC <dodecahedron_golden_chord:[ B D ]>`, whose square is $BE^2 + EC^2 = 12 + 3 = 15$, so $BC = \sqrt{15}$. With center :g:`C <dodecahedron_golden_chord:C>` and radius $CE = \sqrt{3}$, describe circle :g:`(CE) <dodecahedron_golden_chord:( C E )>` cutting :g:`BC <dodecahedron_golden_chord:[ B D ]>` at :g:`D <dodecahedron_golden_chord:D>`, leaving $BD = \sqrt{15} - \sqrt{3}$. With center :g:`B <dodecahedron_golden_chord:B>` and radius $BD$, describe arc :g:`(BD) <dodecahedron_golden_chord:( B D )>` cutting $BE$ at :g:`G <dodecahedron_golden_chord:G>`.
* **Dodecahedron Edge (*Apotome*)**: Both :g:`BG <dodecahedron_golden_chord:/ B G />` (and :g:`AN <euclid_xiii_sphere_polyhedra:/ A N />` on :g:`AB <euclid_xiii_sphere_polyhedra:/ A B />` in the sphere diagram) and the pentagonal sides :g:`AB <dodecahedron_golden_chord:/ A B />` and :g:`AE <dodecahedron_golden_chord:/ A E />` of :g:`ABE <dodecahedron_golden_chord:< A B E >>` are :eq:`equal to the greater golden segment <dodecahedron_golden_chord:/ B G / = dodecahedron_golden_chord:/ A B / = dodecahedron_golden_chord:/ A E />`, an irrational :term:`recisum` (*apotome*):

  $$e_{12} = \sqrt{15} - \sqrt{3}, \qquad e_{12}^2 = 18 - 6\sqrt{5} = 18 - \sqrt{180}.$$

  Leonardo computes the pentagon circumradius squared $af^2 = 6 - \sqrt{7\frac{1}{5}}$ and perpendicular in-sphere squared from the sphere center to each pentagonal face $hf^2 = 9 - af^2 = 3 + \sqrt{7\frac{1}{5}}$, summing the $12$ pentagonal pyramids into $V_{12} = 30\sqrt{3} + 6\sqrt{15} = \sqrt{2{,}700} + \sqrt{540}$.

* **Regular Icosahedron & Hypsicles' Book XIV Ratio**: Erecting $IL = AO = 3$ tangent at $I$ so ray $OL$ cuts the lower semicircle at :g:`M <euclid_xiii_sphere_polyhedra:M>` along :g:`OM <euclid_xiii_sphere_polyhedra:/ O M />` :just:`[XIII. 16] <XIII.16>`, chord :g:`MI <euclid_xiii_sphere_polyhedra:/ M I />` is the **icosahedron edge** (a *minor* irrational line):

  $$e_{20}^2 = 18 - \frac{18}{5}\sqrt{5} = 18 - \sqrt{64\frac{4}{5}}, \qquad V_{20} = 18\sqrt{10 + 2\sqrt{5}}.$$

  Invoking :person:`Hypsicles <hypsicles>`' Book XIV theorem that the dodecahedron and icosahedron inscribed in the same sphere stand to one another as the cube edge $e_6$ to the icosahedron edge $e_{20}$:

  $$\frac{V_{12}}{V_{20}} = \frac{e_6}{e_{20}} = \sqrt{\frac{12}{18 - \frac{18}{5}\sqrt{5}}} = \sqrt{\frac{5 + \sqrt{5}}{6}}.$$

.. qed::

   Here ends the Sixth Distinction on the dimension of solid bodies.
