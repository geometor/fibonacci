:title: DISTINCTIO VIII — DE SUBTILITATIBUS GEOMETRICIS & FLOS (1225)
:layout: book
:order: 8
:tracks: English: dist_08-en | Latin: dist_08-la | Summary: dist_08-summary | Notes: dist_08-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0214
:excerpt: Incipit distinctio octaua de quibusdam subtilitatibus geometricis, et Flos super solutionibus quarumdam questionum.

.. _dist-08-la:
.. _unit-5-la:

DISTINCTIO VIII — DE SUBTILITATIBUS GEOMETRICIS & FLOS (1225)
=============================================================

.. rubric:: *Incipit Distinctio Octaua de Quibusdam Subtilitatibus Geometricis, et Flos (1225)*

**Fons Criticus**: :cite:`boncompagni:1862` (*Scritti di Leonardo Pisano, Vol. II, pp. 207–234 · Cod. Urb. Lat. 292, fol. 134r–148v & Flos*) · :ref:`English Translation <dist-08-en>` · :ref:`Summary <dist-08-summary>` · :ref:`GEOMETOR Notes <dist-08-notes>`

----

.. _dist-08-subtilitates-la:
.. _unit-5-dist8-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0214
   :page: 207–226

Incipit Distinctio Octaua de Quibusdam Subtilitatibus Geometricis
-----------------------------------------------------------------

*Versio Anglica*: :ref:`Distinctio VIII — Pentagon, Decagon & Al-Jabr (pp. 207–226) <dist-08-subtilitates-en>` · *Commentarius*: :ref:`Notae ad Censum Census <dist-08-s2-notes>`

.. enunciation::

   Incipit distinctio octaua de quibusdam subtilitatibus geometricis.

**CIRCULI**, cuius dyameter sit $.10.$, uolo latus penthagonicum inuenire. Adiaceat circulus `.abgde.`, et in ipso sit penthagonum equilaterum et equiangulum `.abgde.`; et protrahatur in ipso corda anguli penthagonici `.ag.`, nec non et dyameter `.bf.` secans cordam `.ag.` in duo equa ad punctum `.c.`.

.. picture:: /_static/figures/pentagon_decagon_circle.svg
   :alt: Descriptio Pentagoni et Decagoni in Circulo Dyametri X
   :caption: Circulus ( I A ) dyametri CA = 10 cum centro I, catheto / I D / = 5, medietate H = 5/2, chorda / H D / = rad. 31 1/4, latere decagoni / I K / = rad. 31 1/4 minus 2 1/2, et latere pentagoni / D K / = rad. (62 1/2 minus rad. 781 1/4).

1. **Modus Geometricus ex Tertio Decimo Euclidis** (:just:`[XIII. 9–10] <XIII.10>`):
   Ducto catheto :g:`ID <pentagon_decagon_circle:/ I D />` $= 5$ et sumpta medietate :g:`H <pentagon_decagon_circle:H>` ($IH = 2\frac{1}{2}$), fit :g:`HD <pentagon_decagon_circle:/ H D />` $= \sqrt{31\frac{1}{4}}$. Transferendo :g:`HD <pentagon_decagon_circle:/ H D />` in :g:`K <pentagon_decagon_circle:K>` per circulum :g:`(HD) <pentagon_decagon_circle:( H D )>`, latus **decagoni** est :g:`IK <pentagon_decagon_circle:/ I K />` :eq:`equale chorde <pentagon_decagon_circle:/ I K / = pentagon_decagon_circle:/ D Q1 / = pentagon_decagon_circle:/ Q1 P1 />` :g:`DQ1 <pentagon_decagon_circle:/ D Q1 />`:

   $$s_{10} = \sqrt{31\frac{1}{4}} - 2\frac{1}{2}.$$

   Et quoniam quadratum lateris pentagoni equatur quadratis laterum hexagoni et decagoni :just:`[XIII. 10] <XIII.10>`, hypotenusa :g:`DK <pentagon_decagon_circle:/ D K />` est **latus pentagoni** :g:`DP1P2P3P4 <pentagon_decagon_circle:< D P1 P2 P3 P4 >>`:

   $$s_5^2 = 25 + \left(37\frac{1}{2} - \sqrt{781\frac{1}{4}}\right) = 62\frac{1}{2} - \sqrt{781\frac{1}{4}}.$$

2. **Modus Algebrae et Almuchabalae** (*p. 208*): Pone latus pentagoni unam :term:`rem <res>` ($x$), quadratum eius unum :term:`censum <census>` ($x^2$), et quadratum census *censum census* ($x^4$). Ex theorematibus :person:`Ptolemei <ptolemy>` in quadrilatero circulari oritur equatio:

   $$x^4 + 3125 = 125\,x^2.$$

   Cuius census est $x^2 = 62\frac{1}{2} - \sqrt{781\frac{1}{4}}$, linea irrationalis minor decimi libri :person:`Euclidis <euclid>`.

----

.. _dist-08-flos-la:
.. _unit-5-flos-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0234
   :page: 227–234

Flos Leonardi Bigolli Pisani (1225)
-----------------------------------

*Versio Anglica*: :ref:`Flos: The Imperial Cubic & Congruum (pp. 227–234) <dist-08-flos-en>` · *Commentarius*: :ref:`Notae ad Florem <dist-08-s3-notes>`

.. enunciation::

   Incipit Flos Leonardi bigolli pisani super solutionibus quarumdam questionum ad numerum et ad geometriam uel ad utrumque pertinentium.

**CVM CORAM MAIESTATE VESTRA**, gloriosissime princeps Frederice, magister Iohannes panormitanus, phylosophus uester, pisis mecum multa de numeris contulisset, interque duas questiones, que non minus ad geometriam quam ad numerum pertinent, proposuit:

1. **De Congruo Quinarij**: Inuenire quadratum numerum cui addito uel diminuto quinario numero egrediatur quadratus numerus ($x^2 \pm 5 = \square$). Quod solutum est per $x = \frac{41}{12}$:

   $$\left(\frac{41}{12}\right)^2 - 5 = \left(\frac{31}{12}\right)^2 = 6\frac{101}{144}, \qquad \left(\frac{41}{12}\right)^2 + 5 = \left(\frac{49}{12}\right)^2 = 16\frac{97}{144}.$$

2. **De Equacione Cubica Irreducibili**: Inuenire lineam $x$ cuius cubus et duo quadrati et decem radices sint uiginti ($x^3 + 2x^2 + 10x = 20$). Demonstrato geometrice per omnes species decimi libri :person:`Euclidis <euclid>` quod hec radix non potest esse rationalis nec aliqua linearum irrationalium euclidis, ostenditur solutio per fractiones sexagesimales:

   $$x = 1^{\circ}\ 22'\ 7''\ 42'''\ 33''''\ 4'''''\ 40'''''' = \frac{1{,}596{,}577{,}777}{1{,}166{,}400{,}000}.$$

.. qed::

   Explicit tractatus floris.
