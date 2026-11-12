:title: UNIT V — DISTINCTIO VII–VIII, FLOS (1225) & LIBER ABACI CONVERGENCE TO PHI
:layout: book

.. _unit-5-en:

UNIT V — DISTINCTIO VII–VIII, *FLOS* (1225) & *LIBER ABACI* CONVERGENCE TO $\phi$
=================================================================================

.. rubric:: *Optical Surveying with the Quadrans, Geometrical Subtleties of the Pentagon, the Flos Cubic, and the Rabbit Recurrence*

**Source Text**: :cite:`fibonacci:pg-7`, :cite:`fibonacci:pg-8`, :cite:`fibonacci:flos`, :cite:`boncompagni:1857` (*Boncompagni Vol. II, pp. 202–247 & Vol. I, pp. 283–284*) · :ref:`Latin (1220 / Boncompagni 1862) <unit-5-la>` · :ref:`Summary <unit-5-summary>` · :ref:`GEOMETOR Notes <unit-5-notes>`

----

.. _unit-5-dist7-en:

.. folio:: fol. 130v–134r
   :page: 202–207

Distinctio VII — Surveying Heights & Distances with the *Quadrans*
------------------------------------------------------------------

*Latin Locus*: :ref:`Distinctio VII — De Altitudinibus et Quadrante (pp. 202–207) <unit-5-dist7-la>` · *Commentary*: :ref:`Notes on Optical Similar Triangles <unit-5-s1-notes>`

.. enunciation::

   Here begins the Seventh Distinction, on finding the heights of elevated things, the depths of wells and valleys, and planar distances, with and without the instrument called the **quadrant** (:term:`quadrans`, *quem quidem oroscopum vocant*).

.. picture:: /_static/figures/quadrans_surveying.svg
   :alt: Optical Surveying with the Quadrans Shadow Square (12 x 12 Puncta)
   :caption: The quadrans shadow square < D H A I > of 12 x 12 puncta with quarter-circle limb ( D I ), 45-degree diagonal [ A B ], umbra recta [ I P ], umbra versa [ A H ], and plumb line / D P / cutting umbra recta at P = 8 puncta (ray [ D C ]).

1. **Without an Astrolabe or Quadrant**: Set up a vertical gnomon or rod of known height, or place a horizontal plane mirror (or vessel of water) upon the ground and step backward until the summit of the tower appears at the center of reflection; by equal angles of incidence and reflection (or parallel rays of the sun), the observer's eye-height and tower height form **equiangular right triangles**, :just:`[VI. 4] <VI.4>` giving $\text{Tower Height} : \text{Tower Distance} = \text{Eye Height} : \text{Mirror Distance}$.
2. **With the *Quadrans* Shadow Square**: Within the quarter-circle limb :g:`(DI) <quadrans_surveying:( D I )>` centered at sighting apex :g:`D <quadrans_surveying:D>`, inscribe the square :g:`DHAI <quadrans_surveying:< D H A I >>` divided along both its horizontal *umbra recta* side :g:`IA <quadrans_surveying:[ I P ]>` and vertical *umbra versa* side :g:`AH <quadrans_surveying:[ A H ]>` into **$12$ equal points** (*puncta*).

   * When the weighted plumb line hangs along the diagonal :g:`DA <quadrans_surveying:[ A B ]>` (meeting the arc at :g:`B <quadrans_surveying:B>` at $45^\circ$), the horizontal distance from the observer's foot to the base of the tower equals the tower's height above the observer's eye.
   * When sighting a steeper tower, the plumb line :g:`DP <quadrans_surveying:/ D P />` (extended as :g:`DC <quadrans_surveying:[ D C ]>` to :g:`C <quadrans_surveying:C>`) cuts *umbra recta* :g:`IA <quadrans_surveying:[ I P ]>` at :g:`P <quadrans_surveying:P>` (for example, at $IP = 8$ *puncta* out of $DI = 12$). By similar triangles :just:`[VI. 4] <VI.4>`, the ratio of horizontal distance to vertical elevation is $8 : 12 = 2 : 3$; hence at distance $40$ *perticae* (and eye-height $1$ *pertica*), the tower height is $\frac{12}{8} \times 40 + 1 = 61$ *perticae*. Conversely, for shallow angles where the plumb line cuts *umbra versa* :g:`AH <quadrans_surveying:[ A H ]>` at $v$ *puncta*, elevation to distance is $v : 12$.

----

.. _unit-5-dist8-en:

.. folio:: fol. 134r–148v
   :page: 207–226

Distinctio VIII — *Subtilitates Geometricae*: Pentagon, Decagon & *Al-Jabr*
---------------------------------------------------------------------------

*Latin Locus*: :ref:`Distinctio VIII — De Subtilitatibus Geometricis (pp. 207–226) <unit-5-dist8-la>` · *Commentary*: :ref:`Notes on Abū Kāmil's Quartic & Euclid XIII.10 <unit-5-s2-notes>`

.. enunciation::

   Here begins the Eighth Distinction, on certain geometrical subtleties (*de quibusdam subtilitatibus geometricis*): to find the chords and sides of the regular **decagon** and **pentagon** inscribed in a circle of rational diameter $d = 10$, both by geometrical proof and by the rule of algebra (*secundum modum algebrae et almuchabalae*).

.. picture:: /_static/figures/pentagon_decagon_circle.svg
   :alt: Pentagon and Decagon Inscribed in Circle of Diameter 10
   :caption: Circle ( I A ) of diameter CA = 10 (center I, radius ID = 5, midpoint H = 5/2): arc ( H D ) of radius / H D / = sqrt(31 1/4) cuts [ I K ] at K, giving decagon side / I K / = / D Q1 / = sqrt(31 1/4) - 2 1/2 and pentagon side / D K / = sqrt(62 1/2 - sqrt(781 1/4)) inscribing < D P1 P2 P3 P4 >.

1. **Euclidean Construction in Circle Diameter $10$** (:just:`[XIII. 9–10] <XIII.10>`):
   In circle :g:`(IA) <pentagon_decagon_circle:( I A )>` of diameter $CA = 10$ through :g:`C <pentagon_decagon_circle:C>`, center :g:`I <pentagon_decagon_circle:I>`, and :g:`A <pentagon_decagon_circle:A>`, erect perpendicular radius :g:`ID <pentagon_decagon_circle:/ I D />` $= 5$ to apex :g:`D <pentagon_decagon_circle:D>`, and bisect $IC$ at :g:`H <pentagon_decagon_circle:H>` ($IH = 2\frac{1}{2}$). Then hypotenuse :g:`HD <pentagon_decagon_circle:/ H D />` has square $25 + 6\frac{1}{4} = 31\frac{1}{4}$. Turning circle :g:`(HD) <pentagon_decagon_circle:( H D )>` onto the diameter at :g:`K <pentagon_decagon_circle:K>` along :g:`IK <pentagon_decagon_circle:[ I K ]>` divides radius $IA = 5$ (the inscribed **hexagon** side) in :term:`extreme and mean ratio <media-et-extrema-proportio>`, yielding the **decagon side** :g:`IK <pentagon_decagon_circle:/ I K />` :eq:`equal to chord <pentagon_decagon_circle:/ I K / = pentagon_decagon_circle:/ D Q1 / = pentagon_decagon_circle:/ Q1 P1 />` :g:`DQ1 <pentagon_decagon_circle:/ D Q1 />` (an :term:`apotome <recisum>`):

   $$s_{10} = IK = \sqrt{31\frac{1}{4}} - 2\frac{1}{2} = \frac{5(\sqrt{5} - 1)}{2}.$$

   By :person:`Euclid <euclid>`'s theorem that the square on the pentagon side equals the sum of the squares on the hexagon and decagon sides :just:`[XIII. 10] <XIII.10>`, hypotenuse :g:`DK <pentagon_decagon_circle:/ D K />` is the **exact side of the regular pentagon** :g:`DP1P2P3P4 <pentagon_decagon_circle:< D P1 P2 P3 P4 >>` (with vertices :g:`P1 <pentagon_decagon_circle:P1>`, :g:`P2 <pentagon_decagon_circle:P2>`, :g:`P3 <pentagon_decagon_circle:P3>`, :g:`P4 <pentagon_decagon_circle:P4>`):

   $$s_5^2 = ID^2 + IK^2 = 25 + \left(37\frac{1}{2} - \sqrt{781\frac{1}{4}}\right) = 62\frac{1}{2} - \sqrt{781\frac{1}{4}}, \qquad s_5 = \frac{5\sqrt{10 - 2\sqrt{5}}}{2}.$$

2. **Algebraic Derivation via *Res*, *Census* & *Census Census*** (:cite:`ptolemy:almagest`):
   Following :person:`al-Khwārizmī <al-khwarizmi>` and :person:`Abū Kāmil <abu-kamil>`, let the unknown pentagon side be one **thing** (:term:`res` $= x$), so its square is one :term:`census` ($x^2$) and its fourth power is *census census* ($x^4$). Combining :person:`Ptolemy <ptolemy>`'s cyclic-quadrilateral theorem :just:`[VI. D] <VI.d>` with diameter $d = 10$ produces the biquadratic equation:

   $$x^4 + 3{,}125 = 125\,x^2.$$

   Completing the square in *census* ($x^2 = 62\frac{1}{2} - \sqrt{3{,}906\frac{1}{4} - 3{,}125} = 62\frac{1}{2} - \sqrt{781\frac{1}{4}}$) recovers the identical Euclid X *minor* irrational!

----

.. _unit-5-flos-en:

.. folio:: Flos (1225)
   :page: 227–234

Bridge I — *Flos* (1225): The Imperial Cubic & Book X Irrationals
-----------------------------------------------------------------

*Latin Locus*: :ref:`Flos super Solutionibus Quarundam Questionum (pp. 227–234) <unit-5-flos-la>` · *Commentary*: :ref:`Notes on the Flos Cubic & Congruum <unit-5-s3-notes>`

Five years after *Practica Geometriae*, at the Pisan court of Emperor :person:`Frederick II <frederick-ii>`, Master :person:`John of Palermo <john-of-palermo>` proposed two celebrated challenges preserved in Leonardo's *Flos* (:cite:`fibonacci:flos`, dedicated to Cardinal :person:`Raniero Capocci <raniero-capocci>`):

1. **The Congruum of Five** (*Liber Quadratorum* & *Flos*): Find a rational square $x^2$ which, increased or diminished by $5$, remains a rational square ($x^2 \pm 5 = \square$). Scaling by $12^2 = 144$ (since $5 \times 144 = 720$ is a :term:`congruum` arising from $m = 5, n = 4$: $4mn(m^2 - n^2) = 720$), Leonardo exhibits $31^2 + 720 = 41^2$ and $41^2 + 720 = 49^2$, whence $x = 3\frac{5}{12} = \frac{41}{12}$:

   $$\left(\frac{41}{12}\right)^2 - 5 = \left(\frac{31}{12}\right)^2, \qquad \left(\frac{41}{12}\right)^2 + 5 = \left(\frac{49}{12}\right)^2.$$

2. **The Irreducible Cubic Equation**: Find a line $x$ such that a cube plus two squares and ten roots equals twenty:

   $$x^3 + 2x^2 + 10x = 20.$$

   Testing every species of rational fraction and every quadratic irrational classified in :person:`Euclid <euclid>`'s Book X (:term:`binomiale`, :term:`recisum`, medial, *minor*, *major*), Leonardo **proves rigorously that $x$ cannot be expressed by any square-root tower of Book X**, and then exhibits its astonishing six-place sexagesimal root:

   $$x \approx 1^{\circ}\ 22'\ 7''\ 42'''\ 33''''\ 4'''''\ 40'''''' = \frac{1{,}596{,}577{,}777}{1{,}166{,}400{,}000} \approx 1.36880810785322\dots$$

   whose error from the true real root $1.36880810782137\dots$ is less than $3.2 \times 10^{-11}$!

----

.. _unit-5-rabbits-en:

.. folio:: Liber Abaci XII
   :page: 283–284

Bridge II — *Liber Abaci* Cap. XII: The Rabbit Sequence & $\phi$
----------------------------------------------------------------

*Latin Locus*: :ref:`Quot Paria Coniculorum in Uno Anno (Vol. I, pp. 283–284) <unit-5-rabbits-la>` · *Commentary*: :ref:`Notes on Cassini's Identity & Golden Convergence <unit-5-s4-notes>`

.. enunciation::

   How many pairs of rabbits are bred in one year from a single pair (*Quot paria coniculorum in uno anno ex uno pario germinentur*).

A certain man placed one pair of rabbits in a place surrounded on all sides by a wall, to find how many pairs would be bred from it in one year, when by nature every mature pair produces another pair every month, and each newborn pair begins to bear in the second month after its birth. Starting with $1$ pair, in the first month there are $2$ pairs, in the second $3$, in the third $5$, and continuing month by month through the twelfth:

$$1,\; 2,\; 3,\; 5,\; 8,\; 13,\; 21,\; 34,\; 55,\; 89,\; 144,\; 233,\; 377.$$

.. qed::

   And thus you can do in order **for an infinite number of months** (*sic posses facere per ordinem de infinitis numeris mensibus*), always adding the first number to the second to form the third: $F_{n+1} = F_n + F_{n-1}$, whose successive ratios $\frac{F_{n+1}}{F_n}$ oscillate above and below and converge inexorably to the **extreme and mean ratio** $\phi = \frac{1 + \sqrt{5}}{2}$ of Units IV and V.
