:title: UNIT II — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
:layout: book

.. _unit-2-en:

UNIT II — DISTINCTIO III: MENSURATION OF FIELDS, HERON'S PROOF & CIRCLE BOUNDS
==============================================================================

.. rubric:: *Scalene Altitudes, the Euclidean Incenter Proof of Heron's Formula, Quadrilaterals, and the 96-gon Circle Measurement*

**Source Text**: :cite:`fibonacci:pg-3` (*Boncompagni Vol. II, pp. 30–110 · fol. 18v–67v*) · :ref:`Latin (1220 / Boncompagni 1862) <unit-2-la>` · :ref:`Summary <unit-2-summary>` · :ref:`GEOMETOR Notes <unit-2-notes>`

----

.. _unit-2-cathetus-en:

.. folio:: fol. 18v–24r
   :page: 30–39

Triangles by *Cathetus* and *Casus*
-----------------------------------

*Latin Locus*: :ref:`De Mensuratione Trigonorum (pp. 30–39) <unit-2-cathetus-la>` · *Commentary*: :ref:`Notes on (13, 14, 15) & Rational Trigonometry <unit-2-s1-notes>`

.. enunciation::

   Here begins the Third Distinction, on the measurement of all planar fields (*in mensuratione omnium camporum*); and first concerning triangles, which are the primary elements into which every rectilinear figure is resolved.

Every triangle is either orthogonal (right-angled), oxygonal (acute-angled), or amblygonal (obtuse-angled). In every triangle, the surface (:term:`embadum`) is equal to the product of half its perpendicular altitude (:term:`cathetus`) into the base on which it falls, or half the base into the whole *cathetus*. :just:`[I. 41] <I.41>`

When the three sides of an acute scalene triangle `.abg.` are known—for example, $ab = 13$ *perticae*, $ag = 15$ *perticae*, and base $bg = 14$ *perticae*—the surveyor finds first the projection (:term:`casus`) of the shorter side upon the base by :person:`Euclid <euclid>`'s theorem on acute triangles :just:`[II. 13] <II.13>`:

.. assertion:: [II. 13] <II.13>

   Subtract the square of $ab$ ($169$) from the sum of the squares of $bg$ ($196$) and $ag$ ($225$), leaving $252$; divide this remainder by twice the base $bg$ ($28$), yielding the greater *casus* $dg = 9$. Subtracting $9$ from $14$ leaves the lesser *casus* $bd = 5$. Then by the theorem of the right triangle :just:`[I. 47] <I.47>`, the square of the *cathetus* $ad$ is $ab^2 - bd^2 = 169 - 25 = 144$, whence $ad = 12$ *perticae*, and the *embadum* is $\frac{1}{2} \times 14 \times 12 = 84$ superficial *perticae*.

----

.. _unit-2-heron-en:

.. folio:: fol. 24v–25v
   :page: 40–41

Heron's Semiperimeter Rule & Fibonacci's Incenter Proof
-------------------------------------------------------

*Latin Locus*: :ref:`Regula et Demonstratio Campi Trigonij (pp. 40–41) <unit-2-heron-la>` · *Commentary*: :ref:`Notes on Heron & the Banū Mūsā Transmission <unit-2-s2-notes>`

.. enunciation::

   Without seeking the *cathetus*, to find the area (:term:`embadum`) of any triangle directly from its three known sides: add the three sides of the triangle together and take half of their sum; from this semiperimeter subtract each side of the triangle in order, keeping the three remainders; multiply the first remainder into the second, that product into the third, and the result into the semiperimeter itself; the square root of this final product is the area of the triangle.

For the triangle of sides $13, 14, 15$, the sum is $42$ and its half is $21$. Subtracting $13, 14, 15$ from $21$ leaves $8, 7, 6$; multiplying $21 \times 8 \times 7 \times 6 = 7{,}056$, its square root is $84$ superficial *perticae*. Now let this admirable rule of :person:`Heron <heron>` (:cite:`heron:metrica`, :cite:`banu-musa:verba`) be proved geometrically.

.. picture:: /_static/figures/heron_incenter_proof.svg
   :alt: Fibonacci's Incenter Proof of Heron's Formula
   :caption: Triangle < A B G > (13, 14, 15) with angle bisectors meeting at incenter T, equal perpendiculars / T H /, / T E /, / T Z / of inradius 4 to the sides, and base [ B L ] extended to L so BL equals the semiperimeter 21.

Let there be given any triangle :g:`ABG <heron_incenter_proof:< A B G >>`, and let two of its angles—namely at :g:`B <heron_incenter_proof:B>` and :g:`G <heron_incenter_proof:G>`—be bisected by the straight lines :g:`BT <heron_incenter_proof:[ B T ]>` and :g:`GT <heron_incenter_proof:[ G T ]>` meeting at :g:`T <heron_incenter_proof:T>`. :just:`[I. 9] <I.9>`

1. **Equal Inradii & Tangency Segments**: From :g:`T <heron_incenter_proof:T>` drop perpendiculars :g:`TH <heron_incenter_proof:/ T H />` upon the base, :g:`TE <heron_incenter_proof:/ T E />` upon side :g:`BE <heron_incenter_proof:[ B E ]>`, and :g:`TZ <heron_incenter_proof:/ T Z />` upon side :g:`GZ <heron_incenter_proof:[ G Z ]>`. :just:`[I. 12] <I.12>` Because right-angled triangles sharing hypotenuse :g:`BT <heron_incenter_proof:/ B T />` or :g:`GT <heron_incenter_proof:/ G T />` have equal acute angles at the bisected vertices, :just:`[I. 26] <I.26>` the three perpendiculars :g:`TH <heron_incenter_proof:/ T H />`, :g:`TE <heron_incenter_proof:/ T E />`, and :g:`TZ <heron_incenter_proof:/ T Z />` are :eq:`all equal to one another <heron_incenter_proof:/ T H / = heron_incenter_proof:/ T E / = heron_incenter_proof:/ T Z />`, and the circle :g:`(TH) <heron_incenter_proof:( T H )>` touches all three sides. :just:`[IV. 4] <IV.4>` Joining :g:`AT <heron_incenter_proof:/ A T />`, it likewise bisects the apex angle at :g:`A <heron_incenter_proof:A>`, giving three pairs of equal tangent segments ($BE = BH$, $HG = GZ$, $AE = AZ$).
2. **Extending the Base to the Semiperimeter**: Produce the base line :g:`BL <heron_incenter_proof:[ B L ]>` beyond :g:`G <heron_incenter_proof:G>` to :g:`L <heron_incenter_proof:L>` so that the added segment :g:`GL <heron_incenter_proof:/ G L />` equals $AE$ ($= AZ$). Since $BH + HG + GL = BH + GZ + AE$ is half the sum of all six tangent segments, the extended line $BL$ equals the **semiperimeter** $s$ of triangle :g:`ABG <heron_incenter_proof:< A B G >>` ($BL = 21$). Moreover, the three excesses $(s - a, s - b, s - c)$ appear directly as the segments on $BL$:

   $$GL = s - BG, \qquad BH = s - AG, \qquad HG = s - AB.$$

3. **Area by Triangulation Around the Incenter**: Triangle :g:`ABG <heron_incenter_proof:< A B G >>` is partitioned into three sub-triangles along :g:`AT <heron_incenter_proof:/ A T />`, :g:`BT <heron_incenter_proof:/ B T />`, and :g:`GT <heron_incenter_proof:/ G T />`, each having altitude equal to :g:`TH <heron_incenter_proof:/ T H />`. Therefore the *embadum* equals $\frac{1}{2} \cdot TH \cdot (\text{perimeter}) = TH \cdot BL$, and its square is $TH^2 \cdot BL^2$.
4. **Similarity via Cyclic Auxiliary Construction**: Erecting perpendiculars at :g:`A <heron_incenter_proof:A>` and :g:`B <heron_incenter_proof:B>` to obtain the supplementary cyclic quadrilateral with angle bisectors meeting at right angles, similar right triangles establish the proportion:

   $$BL : BH = HG : \text{auxiliary segment}, \qquad \text{whence} \quad TH^2 \cdot BL = GL \cdot BH \cdot HG.$$

   Multiplying both sides by $BL$ yields the sought equality:

   $$\Delta^2 = TH^2 \cdot BL^2 = BL \cdot GL \cdot BH \cdot HG = s(s - a)(s - b)(s - c).$$

.. qed::

   Which was to be demonstrated (*quod oportebat ostendere*).

----

.. _unit-2-quad-en:

.. folio:: fol. 34r–53v
   :page: 56–87

Quadrilaterals & Multi-Angular Polygons
---------------------------------------

*Latin Locus*: :ref:`De Campis Quadrilateris et Multangulis (pp. 56–87) <unit-2-quad-la>` · *Commentary*: :ref:`Notes on Quadrilaterals <unit-2-s3-notes>`

Moving from three-sided to four-sided and multi-sided fields, Leonardo classifies every quadrilateral systematically:

1. **Rhombi** (*Campi parte altera longiores sed non rectanguli / caput abscisi*): Measured through half the product of their perpendicular diagonals $e_1, e_2$, since $e_1^2 + e_2^2 = 4a^2$.
2. **Trapezoids** (*Caput abscisum*): Having parallel bases (*caput* $a$ and *basis* $b$) with known flank sides $c, d$. Drawing a line parallel to one flank reduces the figure to a parallelogram plus a known scalene triangle, giving the *cathetus* $h$ and exact area $\frac{a + b}{2} \cdot h$.
3. **General Quadrilaterals & Polygons**: Every general quadrilateral or multi-angular field is resolved into triangles by measuring one or more diagonals (*diametri*), warning surveyors explicitly against the false *agrimensor* rule of multiplying averages of opposite sides ($\frac{a+c}{2}\cdot\frac{b+d}{2}$), which holds **only** for rectangles!

----

.. _unit-2-circle-en:

.. folio:: fol. 54r–56v
   :page: 88–91

Archimedes' Circle Measurement Proved with Small Numbers
--------------------------------------------------------

*Latin Locus*: :ref:`De Mensuratione Circulorum (pp. 88–91) <unit-2-circle-la>` · *Commentary*: :ref:`Notes on the 96-gon Bounds & 864/275 <unit-2-s4-notes>`

.. enunciation::

   It must also be shown how it was discovered by the philosopher :person:`Archimedes <archimedes>` (:cite:`archimedes:circle`) that the circumference of every circle is three times its diameter and a seventh part more—since it is possible to demonstrate most fully with **small numbers** (*cum parvis numeris*) those things which he himself showed with large numbers.

.. picture:: /_static/figures/circle_96gon_bounds.svg
   :alt: Fibonacci's 96-gon Inscribed and Circumscribed Circle Bounds
   :caption: Circle ( C A ) on diameter [ C G ] through center C, with tangent / E Z / at A, 30-degree half-hexagon ray [ C Y ] cutting circle at Y, angle bisector [ C F ] cutting tangent at F, and inscribed chord / Y A / in semicircle triangle GYA.

1. **Circumscribed 96-gon Upper Bound**: Let circle :g:`(CA) <circle_96gon_bounds:( C A )>` have diameter $GA$ through center :g:`C <circle_96gon_bounds:C>` and :g:`G <circle_96gon_bounds:G>`, with perpendicular diameter through :g:`B <circle_96gon_bounds:B>` and :g:`D <circle_96gon_bounds:D>`, and tangent :g:`EZ <circle_96gon_bounds:/ E Z />` touching the circle at :g:`A <circle_96gon_bounds:A>`. :just:`[III. 16] <III.16>` Let angle $ECA$ be one-third of a right angle ($30^\circ$), so :g:`EZ <circle_96gon_bounds:/ E Z />` is the side of the circumscribed regular **hexagon** and $CE = 2\,EA$. Setting $EA = 15$ (or scaling to clear fractions at $CA = 720$), then $CA = \sqrt{CE^2 - EA^2} = \sqrt{675} < 26$.

   Bisecting angle $ECA$ successively four times by rays such as :g:`CF <circle_96gon_bounds:[ C F ]>`—passing from the **$6$-gon** to the **$12$-gon** (:g:`AF <circle_96gon_bounds:/ A F />`), **$24$-gon**, **$48$-gon**, and **$96$-gon**—each angle bisector divides the tangent base in the ratio of hypotenuse to radius :just:`[VI. 3] <VI.3>`:

   $$CA : AF = (CE + CA) : EA.$$

   Carrying out the four bisections with integer-and-fraction bounds scaled to diameter $d = 1440$ ($CA = 720$), Leonardo proves that the perimeter of the circumscribed $96$-gon bears to the diameter a ratio smaller than $1440 : 458\frac{1}{5}$:

   $$\frac{\text{Circumference}}{\text{Diameter}} < \frac{1440}{458\frac{1}{5}} = \frac{7200}{2291} \approx 3.1427324\dots < 3\frac{1}{7}.$$

2. **Inscribed 96-gon Lower Bound**: Conversely, in the semicircle on diameter $GA$, let :g:`YA <circle_96gon_bounds:/ Y A />` be the side of the inscribed hexagon ($YA = \text{radius}$), forming right triangle $GYA$ with leg :g:`GY <circle_96gon_bounds:/ G Y />` and altitude projections at :g:`M <circle_96gon_bounds:M>` (:g:`YM <circle_96gon_bounds:/ Y M />`, :g:`AM <circle_96gon_bounds:/ A M />`). :just:`[III. 31] <III.31>` Four successive chord bisections ($6 \to 12 \to 24 \to 48 \to 96$) establish that the inscribed $96$-gon perimeter exceeds the ratio $1440 : 458\frac{4}{9}$:

   $$\frac{\text{Circumference}}{\text{Diameter}} > \frac{1440}{458\frac{4}{9}} = \frac{6480}{2063} \approx 3.1410567\dots > 3\frac{10}{71}.$$

3. **Fibonacci's Own Mean Ratio ($864 : 275$) & Reduction to $22 : 7$**: Choosing the clean harmonic divisor $458\frac{1}{3}$ strictly between $458\frac{1}{5}$ and $458\frac{4}{9}$, Leonardo obtains his refined rational estimate:

   $$\frac{1440}{458\frac{1}{3}} = \frac{4320}{1375} = \frac{864}{275} = 3\frac{39}{275} \approx 3.141818\dots$$

   And diminishing the denominator $275$ by the minute fraction $\frac{1}{11}$ recovers the surveyor's Archimedean rule:

   $$\frac{864}{275 - \frac{1}{11}} = \frac{9504}{3024} = \frac{22}{7} = 3\frac{1}{7}.$$

   Hence the area (:term:`embadum`) of any circle equals half its circumference multiplied into half its diameter, or $\frac{11}{14}$ of the square on its diameter; and circular sectors (*sectores*) and segments (*portiones*) are measured by subtracting or adding the subtended isosceles triangle.
