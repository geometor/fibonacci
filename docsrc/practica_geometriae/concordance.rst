:title: Concordantia — Cross-Corpus Geometric Concordance
:layout: book

.. _concordance:

Concordantia Geometrica (Cross-Corpus Concordance)
==================================================

.. rubric:: *Linking Leonardo Pisano's Loci to Euclid, Heron, Archimedes, Pacioli, and the GEOMETOR Canon*

This concordance maps the principal propositions and algebraic constructions of :person:`Leonardo Pisano <fibonacci>`'s *Practica Geometriae* (1220), *Flos* (1225), and *Liber Abaci* (1202/1228) across ten sister repositories in the **GEOMETOR** Digital Scriptorium and symbolic engine.

.. list-table:: Master Concordance of Fibonacci Loci
   :header-rows: 1
   :widths: 16 26 30 28

   * - Codex Unit
     - Boncompagni (1857–1862) Locus
     - Mathematical & Constructive Core
     - GEOMETOR Sister Canon Links
   * - :ref:`Unit I <unit-1-en>`
     - *Prologus*, *Introductoria* & *Dist. I* (Vol. II, pp. 1–18, ``fol. 1r–11v``)
     - Euclidean definitions; Pisan :term:`pertica` ($6$ *pedes*, $36$ *denarii*, $66$-*pertica* *stariorum*); Book II identities & III.35 chords
     - ``euclid`` (I.def.1–23, II.1–10, III.35) · ``elements`` (G.1–G.58) · ``pacioli`` (*Summa* Dist. IX) · ``wildberger`` (lattice quadrance)
   * - :ref:`Unit I <unit-1-en>`
     - *Distinctio II* (Vol. II, pp. 18–30, ``fol. 11v–18v``)
     - Positional, sexagesimal, and Pisan *uncia* square-root extraction via Euclid II.4 gnomon completion
     - ``euclid`` (II.4) · ``heron`` (*Metrica* I.8 root iteration) · ``archimedes`` (rational bounds for $\sqrt{3}$)
   * - :ref:`Unit II <unit-2-en>`
     - *Distinctio III, Pars I* (Vol. II, pp. 39–41, ``fol. 23v–25r``)
     - Scalene *cathetus* & *casus* on $(13, 14, 15)$; complete Euclidean incenter proof of Heron's formula $\Delta = \sqrt{s(s-a)(s-b)(s-c)}$
     - ``heron`` (*Metrica* I.8) · ``euclid`` (I.9, I.12, II.12–13, IV.4) · ``etc`` ($X(1)$ Incenter) · ``wildberger`` (Archimedes' quadrea)
   * - :ref:`Unit II <unit-2-en>`
     - *Distinctio III, Pars IV* (Vol. II, pp. 88–91, ``fol. 53v–55v``)
     - Small-number 96-gon bisection ($1440 : 458\frac{1}{5}$ and $1440 : 458\frac{4}{9}$), yielding $\pi_{\text{Fib}} = \frac{864}{275}$ and $\frac{864}{275 - 1/11} = \frac{22}{7}$
     - ``archimedes`` (*Dimensio Circuli* Props. 1 & 3) · ``euclid`` (I.9, III.18, VI.3, XII.2)
   * - :ref:`Unit III <unit-3-en>`
     - *Distinctio IV, Pars I* (Vol. II, pp. 110–121, ``fol. 67v–74v``)
     - Preservation of Euclid's *On Divisions of Figures*: cuts from vertex, side point $D$, interior/exterior point, parallel to base (VI.13), & centroid $X(2)$
     - ``euclid`` (*On Divisions*, I.31, I.37–38, VI.2, VI.13, VI.19, VI.28–29) · ``etc`` ($X(2)$ Centroid) · ``pappus`` (*Synagoge* VII)
   * - :ref:`Unit III <unit-3-en>`
     - *Distinctio IV, Pars II–IV* (Vol. II, pp. 121–148, ``fol. 74v–92v``)
     - Trapezoid parallel cut $c = \sqrt{(q a^2 + p b^2)/(p+q)}$ ($(7^2, 13^2, 17^2)$ progression), quadrilaterals, polygons & circular arcs
     - ``euclid`` (*On Divisions* Props. 19–29) · ``heron`` (*Metrica* III) · ``wildberger`` (*congruum* quadrance triples)
   * - :ref:`Unit IV <unit-4-en>`
     - *Distinctio V–VI* (Vol. II, pp. 148–202, ``fol. 92v–130v``)
     - Cube roots $(a+b)^3$; sphere/cone volumes; all five regular polyhedra in sphere $d = 6$ via $\phi$ ($e_{12} = \sqrt{15} - \sqrt{3}$) & Hypsicles Book XIV
     - ``euclid`` (II.11, VI.30, XII.7–18, XIII.8–18, XIV) · ``archimedes`` (*Sphere & Cylinder*) · ``pacioli`` (*De Divina Proportione*) · ``divine`` ($\phi$ sections)
   * - :ref:`Unit V <unit-5-en>`
     - *Distinctio VII* (Vol. II, pp. 202–206, ``fol. 131r–133v``)
     - Optical sighting of heights, valley depths & plains via rods and the 12-part :term:`quadrans` shadow square
     - ``euclid`` (*Optics* Props. 18–21, VI.4) · ``pappus`` (projective sighting rays)
   * - :ref:`Unit V <unit-5-en>`
     - *Distinctio VIII* (pp. 207–224), *Flos* (pp. 227–247), & *Liber Abaci* Cap. XII (Vol. I, pp. 283–284)
     - Pentagon & decagon in $d = 10$ via *census census* ($x^4 + 3125 = 125x^2$) & XIII.9–10; *Flos* cubic $1;22,7,42,33,4,40$; rabbit ratios $F_{n+1}/F_n \to \phi$
     - ``euclid`` (IV.10–11, X.36–73, XIII.9–10) · ``divine`` (convergents to $\phi$) · ``phyllotaxis`` (parastichy numbers $1..377$) · ``pacioli``
