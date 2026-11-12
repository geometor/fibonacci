:title: UNIT III — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
:layout: book

.. _unit-3-en:

UNIT III — DISTINCTIO IV: DIVISION OF PLANAR FIGURES AMONG CONSORTS
===================================================================

.. rubric:: *Euclid's Lost Treatise On Divisions Transmitted & Expanded: Triangles, Centroids, Parallels, Trapezoids, and Circles*

**Source Text**: :cite:`fibonacci:pg-4`, :cite:`euclid:divisions` (*Boncompagni Vol. II, pp. 110–148 · fol. 67v–92v*) · :ref:`Latin (1220 / Boncompagni 1862) <unit-3-la>` · :ref:`Summary <unit-3-summary>` · :ref:`GEOMETOR Notes <unit-3-notes>`

----

.. _unit-3-sidepoint-en:

.. folio:: fol. 67v–69r
   :page: 110–112

Dividing Triangles from a Vertex or Given Boundary Point
--------------------------------------------------------

*Latin Locus*: :ref:`De Divisione Trigonorum per Punctum in Latere (pp. 110–112) <unit-3-sidepoint-la>` · *Commentary*: :ref:`Notes on Euclid's On Divisions <unit-3-s1-notes>`

.. enunciation::

   Here ends the Third Distinction, and begins the Fourth: on the division of fields among co-heirs or partners (:term:`consortes`).

1. **Division from a Vertex into Any Given Ratio**: To divide a triangle `.abg.` from vertex `.a.` into two, three, or more equal or proportional shares, divide the opposite base `.bg.` in the same ratio :just:`[VI. 10] <VI.10>` and draw straight lines from `.a.` to the points of division; for triangles under the same altitude have the same ratio to one another as their bases. :just:`[VI. 1] <VI.1>`
2. **Equiangular Area-Ratio Lemma**: Before dividing from a point that is *not* a vertex, Leonardo proves from :person:`Euclid <euclid>` :just:`[VI. 23] <VI.23>` that if two triangles share an equal angle at `.g.`, the ratio of their areas is compounded of the ratios of the sides containing that equal angle—that is, $(gd \cdot gz) : (gb \cdot ga)$.
3. **Bisection from an Arbitrary Point on a Side** (*On Divisions* Prop. 4): Suppose two *consortes* wish to bisect a triangular field :g:`ABG <division_side_point:< A B G >>` by a straight boundary starting from a well, tree, or boundary stone at :g:`D <division_side_point:D>` on the base :g:`BE <division_side_point:[ B E ]>`, where :g:`D <division_side_point:D>` is *not* the midpoint.

.. picture:: /_static/figures/division_side_point.svg
   :alt: Bisecting a Triangle from an Arbitrary Point D on a Side
   :caption: Triangle < A B G > (13, 14, 15) bisected from point D (BD = 5, DG = 9) via midpoint E (BE = EG = 7): drawing [ E Z ] parallel to [ A D ] determines cut / D Z / (GZ = 11 2/3), making < D Z G > equal in area to quadrilateral < A B D Z >.

* **Construction**: Bisect the base at :g:`E <division_side_point:E>` and join the median :g:`AE <division_side_point:/ A E />` (which halves :g:`ABG <division_side_point:< A B G >>`). Join :g:`AD <division_side_point:[ A D ]>`, and through :g:`E <division_side_point:E>` draw :g:`EZ <division_side_point:[ E Z ]>` parallel to :g:`AD <division_side_point:[ A D ]>`, :just:`[I. 31] <I.31>` meeting side :g:`GZ <division_side_point:[ G Z ]>` at :g:`Z <division_side_point:Z>`. Draw the dividing boundary :g:`DZ <division_side_point:/ D Z />`.
* **Proof**: Triangles $ADE$ and $ADZ$ stand upon the same base :g:`AD <division_side_point:[ A D ]>` and between the same parallels :g:`AD <division_side_point:[ A D ]>` and :g:`EZ <division_side_point:[ E Z ]>`; therefore they are equal in area. :just:`[I. 37] <I.37>` Adding the common triangle $EDG$ (or replacing $ADE$ with $ADZ$), the triangular share :g:`DZG <division_side_point:< D Z G >>` equals the median half-triangle $AEG$, leaving the quadrilateral share :g:`ABDZ <division_side_point:< A B D Z >>` equal to the other half!
* **Numerical Rule**: Because :g:`EZ <division_side_point:[ E Z ]>` $\parallel$ :g:`AD <division_side_point:[ A D ]>`, $GD : GE = GA : GZ$. :just:`[VI. 2] <VI.2>` In the $(13, 14, 15)$ triangle with $BD = 5$, $DG = 9$, $GE = 7$, and $GA = 15$, we have $GZ = \frac{7 \times 15}{9} = 11\frac{2}{3}$ *perticae*, and both :g:`DZG <division_side_point:< D Z G >>` and :g:`ABDZ <division_side_point:< A B D Z >>` contain exactly $42$ superficial *perticae*.

----

.. _unit-3-centroid-en:

.. folio:: fol. 69r–74r
   :page: 112–120

Concurrency of Medians & Three-Consort Centroid Division
--------------------------------------------------------

*Latin Locus*: :ref:`Preparatoria de Concursu Linearum et Trium Consortum Divisione (pp. 112–120) <unit-3-centroid-la>` · *Commentary*: :ref:`Notes on Centroid X(2) & Interior Points <unit-3-s2-notes>`

.. picture:: /_static/figures/division_medians_centroid.svg
   :alt: Concurrency of Medians and Three-Consort Partition at Centroid D
   :caption: Triangle < A B G > with side midpoints E, Z, T and medians [ A D ], [ B D ], [ G D ] concurring at centroid D in 2:1 ratio, partitioning the field into three equal consort shares < D A B >, < D B G >, and < D G A >.

.. lemma::

   *Preparatoria*: In every triangle :g:`ABG <division_medians_centroid:< A B G >>`, the three straight lines drawn from the angles to the midpoints :g:`E <division_medians_centroid:E>`, :g:`Z <division_medians_centroid:Z>`, and :g:`T <division_medians_centroid:T>` of the opposite sides concur at a single point :g:`D <division_medians_centroid:D>`, where the segment toward each vertex is **double** the segment toward the midpoint ($AD = 2\,DE$, $BD = 2\,DZ$, $GD = 2\,DT$).

Joining $EZ$ parallel to $AB$, $AB = 2\,EZ$; :just:`[VI. 2] <VI.2>` hence in the alternate-angle similar triangles $ADB$ and $EDZ$, :g:`AD <division_medians_centroid:/ A D />` $= 2\,DE$ and :g:`BD <division_medians_centroid:/ B D />` $= 2\,DZ$. Repeating the same proof for median :g:`GT <division_medians_centroid:[ B T ]>` shows it must cut :g:`AD <division_medians_centroid:[ A D ]>` at the *very same* two-thirds point :g:`D <division_medians_centroid:D>`.

* **Partition Among Three Consorts**: If three *consortes* wish to share a triangular field :g:`ABG <division_medians_centroid:< A B G >>` with equal access to a central well or landmark at the centroid :g:`D <division_medians_centroid:D>`, draw the three boundaries :g:`AD <division_medians_centroid:/ A D />`, :g:`BD <division_medians_centroid:/ B D />`, and :g:`GD <division_medians_centroid:/ G D />`. Because $DE = \frac{1}{3} AE$, triangle :g:`DBG <division_medians_centroid:< D B G >>` is one-third of :g:`ABG <division_medians_centroid:< A B G >>`; likewise :g:`DAB <division_medians_centroid:< D A B >>` and :g:`DGA <division_medians_centroid:< D G A >>` are each one-third—so all three shares are equal ($28$ superficial *perticae* each in the $(13, 14, 15)$ field).
* **Through Any Given Interior or Exterior Point** (*pp. 113–117*): If the assigned well $P$ is *not* the centroid (or lies outside the field), Leonardo reduces the straight-line cut through $P$ cutting off a given fraction of area to hyperbolic application of areas :just:`[VI. 28–29] <VI.28>`, solving the resulting quadratic equation by Euclid II.5–6.

----

.. _unit-3-parallel-en:

.. folio:: fol. 73r–73v
   :page: 118–119

Dividing a Triangle Parallel to Its Base
----------------------------------------

*Latin Locus*: :ref:`Divisio Trigoni per Lineam Equidistantem Basi (p. 119) <unit-3-parallel-la>` · *Commentary*: :ref:`Notes on Quadratic Scaling & Trapezoids <unit-3-s3-notes>`

.. enunciation::

   To cut a given triangle :g:`ABG <division_parallel_base:< A B G >>` into two equal shares (or in any given ratio) by a straight line :g:`EZ <division_parallel_base:/ E Z />` drawn parallel to its base :g:`BG <division_parallel_base:[ B G ]>`. (*Euclid, On Divisions, Prop. 1 & 19*)

.. picture:: /_static/figures/division_parallel_base.svg
   :alt: Dividing a Triangle Parallel to Its Base via Semicircle Mean Proportional
   :caption: Triangle < A B G > (10, 14, 12) bisected parallel to base [ B G ]: adding / A D / = 1/2 BA = 5, erecting perpendicular / A K / to semicircle ( O1 B ) on BD (AK^2 = 50), and transferring arc ( A K ) to E gives / E Z / (EZ^2 = 98), dividing < A E Z > and < E B G Z > equally.

* **Geometric Construction & Proof**: Since :g:`EZ <division_parallel_base:[ E Z ]>` $\parallel$ :g:`BG <division_parallel_base:[ B G ]>`, triangle :g:`AEZ <division_parallel_base:< A E Z >>` is similar to :g:`ABG <division_parallel_base:< A B G >>`, so their areas stand in the duplicate ratio of their homologous sides: $\triangle ABG : \triangle AEZ = BA^2 : EA^2$. :just:`[VI. 19] <VI.19>` To make $\triangle AEZ = \frac{1}{2}\triangle ABG$, we require $BA^2 = 2\,EA^2$, i.e., $EA$ must be the **mean proportional** between $BA$ and $\frac{1}{2} BA$.

  Extend :g:`BE <division_parallel_base:[ B E ]>` beyond :g:`A <division_parallel_base:A>` by segment :g:`AD <division_parallel_base:/ A D />` $= \frac{1}{2} BA$. Describe the semicircle :g:`(O1B) <division_parallel_base:( O1 B )>` upon diameter $BD$, and erect at :g:`A <division_parallel_base:A>` the perpendicular :g:`AK <division_parallel_base:/ A K />` to meet the semicircle at :g:`K <division_parallel_base:K>`. By the semicircle mean-proportional property :just:`[VI. 13] <VI.13>`, $AK^2 = BA \cdot AD = \frac{1}{2} BA^2$. Transfer length :g:`AK <division_parallel_base:/ A K />` by circle :g:`(AK) <division_parallel_base:( A K )>` onto side :g:`BE <division_parallel_base:[ B E ]>` at :g:`E <division_parallel_base:E>` (so $AE = AK$), and draw :g:`EZ <division_parallel_base:/ E Z />` parallel to :g:`BG <division_parallel_base:[ B G ]>` meeting :g:`GZ <division_parallel_base:[ G Z ]>` at :g:`Z <division_parallel_base:Z>`. Then :g:`AEZ <division_parallel_base:< A E Z >>` and the residual trapezoid :g:`EBGZ <division_parallel_base:< E B G Z >>` are equal!

* **Surd Example on $(10, 14, 12)$**: Let $AB = 10$, $BG = 14$, and $AG = 12$. Then $AD = 5$, and the squares of the cut sides are exact integers even though the lengths themselves are quadratic surds:

  $$AE^2 = 10 \times 5 = 50, \qquad AZ^2 = \frac{1}{2} \times 144 = 72, \qquad EZ^2 = \frac{1}{2} \times 196 = 98.$$

----

.. _unit-3-trapezoid-en:

.. folio:: fol. 78r–92v
   :page: 126–148

Divisions of Quadrilaterals, Trapezoids & Circles
-------------------------------------------------

*Latin Locus*: :ref:`De Divisione Quadrilaterorum et Circulorum (pp. 126–148) <unit-3-trapezoid-la>` · *Commentary*: :ref:`Notes on the RMS Trapezoid Invariant <unit-3-s3-notes>`

1. **Trapezoid Divided Parallel to Its Bases** (*Caput Abscisum*): Let a trapezoid have upper base (*caput*) $a$ and lower base (*basis*) $b$. Completing the flank sides to their apex cone reduces the trapezoid to the difference of two similar triangles proportional to $b^2$ and $a^2$. :just:`[VI. 19] <VI.19>` Hence a parallel line of length $c$ dividing the trapezoid into upper and lower shares in ratio $p : q$ satisfies the **weighted root-mean-square law**:

   $$c^2 = \frac{q\,a^2 + p\,b^2}{p + q}, \qquad \text{and for bisection } (p = q = 1): \quad c = \sqrt{\frac{a^2 + b^2}{2}}.$$

   In the rational gromatic case $a = 7$, $b = 17$, the bisecting parallel chord is $c = \sqrt{\frac{49 + 289}{2}} = \sqrt{169} = 13$, cutting the altitude in ratio $(13 - 7) : (17 - 13) = 6 : 4 = 3 : 2$.
2. **General Quadrilaterals & Polygons**: Divided from any vertex or boundary point by first computing the total area via diagonals, isolating the triangle or sub-polygon containing the cut, and applying the side-point construction :ref:`above <unit-3-sidepoint-en>`.
3. **Circles, Semicircles & Segments** (*Euclid, On Divisions, Props. 28–29*): Circles are divided into equal rings by concentric circles whose radii follow the semicircle mean-proportional law ($r_k^2 = \frac{k}{n} R^2$), or divided by parallel chords separating a given circular segment plus or minus its subtended triangle.

.. qed::

   Here ends the Fourth Distinction on the division of fields among consorts.
