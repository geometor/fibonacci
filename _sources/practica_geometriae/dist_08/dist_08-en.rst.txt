:title: DISTINCTIO VIII — SUBTILITATES GEOMETRICAE & FLOS (1225)
:layout: book
:order: 8
:tracks: English: dist_08-en | Latin: dist_08-la | Summary: dist_08-summary | Notes: dist_08-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0214
:excerpt: Subtilitates Geometricae, pentagon and decagon in circle d=10, Abu Kamil's quartic, and the Flos imperial cubic and congruum.

.. _dist-08-en:
.. _unit-5-en:

DISTINCTIO VIII — SUBTILITATES GEOMETRICAE & FLOS (1225)
========================================================

.. rubric:: *Geometrical Subtleties of the Pentagon and Decagon, Al-Jabr Quartic, and the Flos Imperial Cubic*

**Source Text**: :cite:`fibonacci:pg-8`, :cite:`fibonacci:flos` (*Boncompagni Vol. II, pp. 207–234 · fol. 134r–148v & Flos*) · :ref:`Latin (1220 / Boncompagni 1862) <dist-08-la>` · :ref:`Summary <dist-08-summary>` · :ref:`GEOMETOR Notes <dist-08-notes>`

----

.. _dist-08-subtilitates-en:
.. _unit-5-dist8-en:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0214
   :page: 207–226

Distinctio VIII — *Subtilitates Geometricae*: Pentagon, Decagon & *Al-Jabr*
---------------------------------------------------------------------------

*Latin Locus*: :ref:`Distinctio VIII — De Subtilitatibus Geometricis (pp. 207–226) <dist-08-subtilitates-la>` · *Commentary*: :ref:`Notes on Abū Kāmil's Quartic & Euclid XIII.10 <dist-08-s2-notes>`

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

.. _dist-08-flos-en:
.. _unit-5-flos-en:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0234
   :page: 227–234

*Flos* (1225) — The Imperial Cubic & Book X Irrationals
-------------------------------------------------------

*Latin Locus*: :ref:`Flos super Solutionibus Quarundam Questionum (pp. 227–234) <dist-08-flos-la>` · *Commentary*: :ref:`Notes on the Flos Cubic & Congruum <dist-08-s3-notes>`

Five years after *Practica Geometriae*, at the Pisan court of Emperor :person:`Frederick II <frederick-ii>`, Master :person:`John of Palermo <john-of-palermo>` proposed two celebrated challenges preserved in Leonardo's *Flos* (:cite:`fibonacci:flos`, dedicated to Cardinal :person:`Raniero Capocci <raniero-capocci>`):

1. **The Congruum of Five** (*Liber Quadratorum* & *Flos*): Find a rational square $x^2$ which, increased or diminished by $5$, remains a rational square ($x^2 \pm 5 = \square$). Scaling by $12^2 = 144$ (since $5 \times 144 = 720$ is a :term:`congruum` arising from $m = 5, n = 4$: $4mn(m^2 - n^2) = 720$), Leonardo exhibits $31^2 + 720 = 41^2$ and $41^2 + 720 = 49^2$, whence $x = 3\frac{5}{12} = \frac{41}{12}$:

   $$\left(\frac{41}{12}\right)^2 - 5 = \left(\frac{31}{12}\right)^2, \qquad \left(\frac{41}{12}\right)^2 + 5 = \left(\frac{49}{12}\right)^2.$$

2. **The Irreducible Cubic Equation**: Find a line $x$ such that a cube plus two squares and ten roots equals twenty:

   $$x^3 + 2x^2 + 10x = 20.$$

   Testing every species of rational fraction and every quadratic irrational classified in :person:`Euclid <euclid>`'s Book X (:term:`binomiale`, :term:`recisum`, medial, *minor*, *major*), Leonardo **proves rigorously that $x$ cannot be expressed by any square-root tower of Book X**, and then exhibits its astonishing six-place sexagesimal root:

   $$x \approx 1^{\circ}\ 22'\ 7''\ 42'''\ 33''''\ 4'''''\ 40'''''' = \frac{1{,}596{,}577{,}777}{1{,}166{,}400{,}000} \approx 1.36880810785322\dots$$

   whose error from the true real root $1.36880810782137\dots$ is less than $3.2 \times 10^{-11}$!
