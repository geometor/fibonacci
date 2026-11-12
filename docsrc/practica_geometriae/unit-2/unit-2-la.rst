:title: UNITAS II — DISTINCTIO III: IN MENSURATIONE OMNIUM CAMPORUM
:layout: book

.. _unit-2-la:

UNITAS II — DISTINCTIO III: IN MENSURATIONE OMNIUM CAMPORUM
===========================================================

.. rubric:: *De Mensuratione Trigonorum, Demonstratione Regulae Heronis, Quadrilateris et Mensuratione Circulorum*

**Fons Criticus**: :cite:`boncompagni:1862` (*Scritti di Leonardo Pisano, Vol. II, pp. 30–110 · Cod. Urb. Lat. 292, fol. 18v–67v*) · :ref:`English Translation <unit-2-en>` · :ref:`Summary <unit-2-summary>` · :ref:`GEOMETOR Notes <unit-2-notes>`

----

.. _unit-2-cathetus-la:

.. folio:: fol. 18v–24r
   :page: 30–39

De Mensuratione Trigonorum per Cathetum et Casum
------------------------------------------------

*Versio Anglica*: :ref:`Triangles by Cathetus and Casus (pp. 30–39) <unit-2-cathetus-en>` · *Commentarius*: :ref:`Notae ad Trigonum (13, 14, 15) <unit-2-s1-notes>`

.. enunciation::

   Incipit distinctio tertia in mensuratione omnium camporum; et primo de campis trigonis.

Omnis trigonus aut est ortogonius, aut oxigonius, aut ambligonius; et cuiuslibet trigoni :term:`embadum` equale est ei quod fit ex dimidio :term:`catheti <cathetus>` in basim super quam cadit, vel ex dimidio basis in totum cathetum. :just:`[I. 41] <I.41>`

Sit trigonus oxigonius diversilaterus `.abg.`, cuius latus `.ab.` sit perticarum $.XIII.$, latus `.ag.` $.XV.$, et basis `.bg.` $.XIIII.$. Ut inveniatur :term:`casus` et cathetus `.ad.` :just:`[II. 13] <II.13>`:

.. assertion:: [II. 13, I. 47] <II.13>

   Auferatur quadratum `.ab.` ($169$) a quadratis `.bg.` ($196$) et `.ag.` ($225$) pariter acceptis ($421$); remanent $.CCLII.$ ($252$), que dividantur per duplum basis `.bg.` ($28$): exibit maior casus `.dg.` perticarum $.VIIII.$ ($9$), et minor casus `.bd.` erit $.V.$ ($5$). Inde quadratum `.bd.` ($25$) demptum ex quadrato `.ab.` ($169$) relinquit $.CXLIIII.$ ($144$), cuius radix $.XII.$ est cathetus `.ad.`; multiplicato itaque dimidio basis ($7$) in $.XII.$, provenit embadum perticarum $.LXXXIIII.$ ($84$).

----

.. _unit-2-heron-la:

.. folio:: fol. 24v–25v
   :page: 40–41

Regula Generalis et Demonstratio Campi Trigonij (Heron)
-------------------------------------------------------

*Versio Anglica*: :ref:`Heron's Semiperimeter Rule & Incenter Proof (pp. 40–41) <unit-2-heron-en>` · *Commentarius*: :ref:`Notae ad Demonstrationem Heronis <unit-2-s2-notes>`

.. enunciation::

   Trigoni latera in unum coniunge, et dimidium sume accipe eorum; a qua per ordinem singulum latus eiusdem trigoni aufer, et residuum serva; post hec multiplica primum residuum in secundum, et summam in tertium, et quod inde provenerit multiplica in dimidium sume trium laterum; et summe provenientis radix erit :term:`embadum` ipsius trigoni.

In trigono $.XIII., .XIIII., .XV.$ summa laterum est $.XLII.$, cuius dimidium est $.XXI.$; residua sunt $.VIII., .VII., .VI.$; ex $.XXI.$ in $.VIII.$ in $.VII.$ in $.VI.$ proveniunt $7{,}056$, cuius radix $.LXXXIIII.$ ($84$) est embadum. Quod nunc geometrice (:cite:`heron:metrica`, :cite:`banu-musa:verba`) demonstretur.

.. picture:: /_static/figures/heron_incenter_proof.svg
   :alt: Demonstratio Geometrica Regulae Heronis in Trigono ABG
   :caption: Trigonus < A B G > cum puncto concursus bisectorum T, cathetis equalibus / T H /, / T E /, / T Z /, circulo inscripto ( T H ) et linea [ B L ] protracta ad dimidium perimetri.

Sit datus trigonus :g:`ABG <heron_incenter_proof:< A B G >>`, dividanturque duo eius anguli ad :g:`B <heron_incenter_proof:B>` et :g:`G <heron_incenter_proof:G>` per equalia lineis :g:`BT <heron_incenter_proof:[ B T ]>` et :g:`GT <heron_incenter_proof:[ G T ]>` concurrentibus in puncto :g:`T <heron_incenter_proof:T>`. :just:`[I. 9] <I.9>`

1. **De Equalitate Perpendicularium**: A puncto :g:`T <heron_incenter_proof:T>` ducantur perpendiculares :g:`TH <heron_incenter_proof:/ T H />`, :g:`TE <heron_incenter_proof:/ T E />`, et :g:`TZ <heron_incenter_proof:/ T Z />` super tria latera :g:`BL <heron_incenter_proof:[ B L ]>`, :g:`BE <heron_incenter_proof:[ B E ]>`, et :g:`GZ <heron_incenter_proof:[ G Z ]>`. :just:`[I. 12] <I.12>` Quia trigoni rectanguli circa :g:`BT <heron_incenter_proof:/ B T />` et :g:`GT <heron_incenter_proof:/ G T />` habent angulos equales et latus commune, :just:`[I. 26] <I.26>` erunt tres perpendiculares :g:`TH <heron_incenter_proof:/ T H />`, :g:`TE <heron_incenter_proof:/ T E />`, :g:`TZ <heron_incenter_proof:/ T Z />` :eq:`sibi invicem equales <heron_incenter_proof:/ T H / = heron_incenter_proof:/ T E / = heron_incenter_proof:/ T Z />`, circulusque :g:`(TH) <heron_incenter_proof:( T H )>` continget tria latera; :just:`[IV. 4] <IV.4>` coniunctaque :g:`AT <heron_incenter_proof:/ A T />` dividet similiter angulum :g:`A <heron_incenter_proof:A>` per equalia.
2. **Protractio Basis ad Dimidium Laterum**: Protrahatur basis :g:`BL <heron_incenter_proof:[ B L ]>` in rectum usque ad :g:`L <heron_incenter_proof:L>`, ponaturque :g:`GL <heron_incenter_proof:/ G L />` equalis portioni $AE$ (sive $AZ$). Erit igitur tota linea $BL$ (composita ex :g:`BH <heron_incenter_proof:/ B H />`, :g:`HG <heron_incenter_proof:/ H G />`, et :g:`GL <heron_incenter_proof:/ G L />`) **dimidium trium laterum** trigoni :g:`ABG <heron_incenter_proof:< A B G >>`, et tria residua erunt $GL$, $BH$, et $HG$.
3. **Demonstratio Proportionalitatis**: Quoniam embadum trigoni :g:`ABG <heron_incenter_proof:< A B G >>` componitur ex tribus trigonis circa :g:`T <heron_incenter_proof:T>`, fit ipsum ex multiplicatione :g:`TH <heron_incenter_proof:/ T H />` in $BL$, quadratumque embadi est quadratum :g:`TH <heron_incenter_proof:/ T H />` in quadratum $BL$. Per similitudinem autem trigonorum rectangulorum ostenditur quod id quod fit ex quadrato :g:`TH <heron_incenter_proof:/ T H />` in $BL$ equale est ei quod fit ex :g:`GL <heron_incenter_proof:/ G L />` in :g:`BH <heron_incenter_proof:/ B H />` et in :g:`HG <heron_incenter_proof:/ H G />`; quare:

   $$\text{Embadum}^2 = TH^2 \cdot BL^2 = BL \cdot GL \cdot BH \cdot HG.$$

.. qed::

   Quod oportebat ostendere.

----

.. _unit-2-quad-la:

.. folio:: fol. 34r–53v
   :page: 56–87

De Campis Quadrilateris et Multangulis
--------------------------------------

*Versio Anglica*: :ref:`Quadrilaterals & Multi-Angular Polygons (pp. 56–87) <unit-2-quad-en>` · *Commentarius*: :ref:`Notae ad Quadrilatera <unit-2-s3-notes>`

Tractantur consequenter campi quadrilateri—rombi per dyametros orthogonaliter se secantes ($\frac{1}{2} e_1 e_2$), campi caput abscisi (trapezia) per cathetum in dimidium aggregati capitis et basis ($\frac{a+b}{2}\cdot h$), ac quadrilatera irregularia et multangula, que omnia per protractionem dyametrorum in trigonos resolvuntur.

----

.. _unit-2-circle-la:

.. folio:: fol. 54r–56v
   :page: 88–91

De Mensuratione Circulorum Secundum Archimenidem cum Parvis Numeris
-------------------------------------------------------------------

*Versio Anglica*: :ref:`Archimedes' Circle Measurement (pp. 88–91) <unit-2-circle-en>` · *Commentarius*: :ref:`Notae ad Polygonum XCVI Laterum <unit-2-s4-notes>`

.. enunciation::

   **OSTENDENDVM** est etiam quomodo inventum fuit, lineam circunferentem omnis circuli esse triplam et septimam sui dyametri ab :person:`ARCHIMENIDE <archimedes>` phylosopho (:cite:`archimedes:circle`); cum possibile sit **cum parvis numeris** ea que ipse cum magnis ostendit plenissime demonstrare.

.. picture:: /_static/figures/circle_96gon_bounds.svg
   :alt: Mensuratio Circuli per Polygona XCVI Laterum Circumscripta et Inscripta
   :caption: Circulus ( C A ) super dyametrum [ C G ] cum contingente / E Z / in puncto A, radio [ C Y ], bisectore [ C F ] et corda inscripta / Y A /.

1. **Polygonum Circumscriptum $.XCVI.$ Laterum**: Describatur circulus :g:`(CA) <circle_96gon_bounds:( C A )>` circa centrum :g:`C <circle_96gon_bounds:C>` cum dyametris per :g:`G <circle_96gon_bounds:G>`, :g:`A <circle_96gon_bounds:A>` et :g:`B <circle_96gon_bounds:B>`, :g:`D <circle_96gon_bounds:D>`, contingenteque :g:`EZ <circle_96gon_bounds:/ E Z />` in puncto :g:`A <circle_96gon_bounds:A>`. :just:`[III. 16] <III.16>` Sit angulus sub :g:`CY <circle_96gon_bounds:[ C Y ]>` et $CA$ tertia pars unius recti, dividaturque quater per equalia per lineas ut :g:`CF <circle_96gon_bounds:[ C F ]>` secantes contingentem in :g:`F <circle_96gon_bounds:F>` (:g:`AF <circle_96gon_bounds:/ A F />`, :g:`CZ <circle_96gon_bounds:/ C Z />`)—ab exagono ad figuram $.XII.$, $.XXIIII.$, $.XLVIII.$, et $.XCVI.$ laterum. :just:`[VI. 3] <VI.3>` Posito dyametro $.MCCCCXL.$ ($1440$, semidyametro $CA = 720$), ostenditur ambitum figure circumscripte $.XCVI.$ laterum minorem habere proportionem ad dyametrum quam $1440$ ad $458\frac{1}{5}$ ($\frac{7200}{2291}$).
2. **Polygonum Inscriptum $.XCVI.$ Laterum**: In semicirculo autem inscribatur corda exagoni :g:`YA <circle_96gon_bounds:/ Y A />` cum catheto :g:`GY <circle_96gon_bounds:/ G Y />` et casibus ad :g:`M <circle_96gon_bounds:M>` (:g:`YM <circle_96gon_bounds:/ Y M />`, :g:`AM <circle_96gon_bounds:/ A M />`). :just:`[III. 31] <III.31>` Quatuor subduplicationibus arcuum demonstratur ambitum figure inscripte $.XCVI.$ laterum maiorem habere proportionem ad dyametrum quam $1440$ ad $458\frac{4}{9}$ ($\frac{6480}{2063}$).
3. **Proportio Media Leonardi ($864 : 275$) et $22 : 7$**: Accipiendo numerum medium $458\frac{1}{3}$ inter $458\frac{1}{5}$ et $458\frac{4}{9}$, habetur proportio circunferentie ad dyametrum ut $1440$ ad $458\frac{1}{3}$, hoc est **ut $864$ ad $275$** ($3\frac{39}{275}$); et dempta undecima parte unius ($\frac{1}{11}$) a $275$, remanet $864$ ad $274\frac{10}{11}$, que est ipsissima proportio **tripla sesquiseptima** ($3\frac{1}{7} = \frac{22}{7}$).
