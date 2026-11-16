:title: DISTINCTIO III — IN MENSURATIONE OMNIUM CAMPORUM
:layout: book
:order: 3
:tracks: English: dist_03-en | Latin: dist_03-la | Summary: dist_03-summary | Notes: dist_03-notes
:folio: boncompagni_1862_vol2_practica_geometriae:0037
:excerpt: Distinctio tertia: in mensuratione omnium camporum, demonstratio regulae Heronis per inscriptum circulum, et mensuratio circulorum.

.. _dist-03-la:
.. _unit-2-la:

DISTINCTIO III — IN MENSURATIONE OMNIUM CAMPORUM
================================================

.. rubric:: *Distinctio Tertia: In Mensuratione Omnium Camporum Superficialium*

**Fons Criticus**: :cite:`boncompagni:1862` (*Scritti di Leonardo Pisano, Vol. II, pp. 30–110 · Cod. Urb. Lat. 292, fol. 18v–67v*) · :ref:`English Translation <dist-03-en>` · :ref:`Summary <dist-03-summary>` · :ref:`GEOMETOR Notes <dist-03-notes>`

----

.. _dist-03-cathetus-la:
.. _unit-2-cathetus-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0037
   :page: 30–39

De Mensuratione Trigonorum per Cathetum et Casum
------------------------------------------------

*Versio Anglica*: :ref:`Triangles by Cathetus & Casus (pp. 30–39) <dist-03-cathetus-en>` · *Commentarius*: :ref:`Notae ad Trigonometriam Rationalem <dist-03-s1-notes>`

.. enunciation::

   Incipit distinctio tertia in mensuratione omnium camporum.

**HANC** itaque distinctionem in quinque partes diuidere decreui. In prima quarum mensurabimus triangulos. In secunda quadrilateros. In tertia multilateros, qui ex rectis lineis constant. In quarta circulos, et eorum portiones, et obliquas figuras insuper, et commixtas ex rectis et curuis lineis. In quinta mensurabimus ipsos campos, qui in ascensione montium iacent.

Incipit pars prima tertie distinctionis de mensuratione triangulorum. Campi qui triangulj uel trilateri sunt, alij orthogonij, scilicet rectianguli; alij oxigonij, scilicet acutianguli; alij quoque ampligonij appellantur: et hec nomina recipiunt ab angulis. Colligitur quippe :term:`embadum`, scilicet area omnium triangulorum, ex multiplicatione dimidij unius laterum, super quod cadit :term:`cathetus`, in ipsum cathetum; uel ex multiplicatione totius basis in dimidium catheti. :just:`[I. 41] <I.41>`

In triangulo oxigonio `.a.b.g.` cuius latera sint $.13.$, $.14.$, $.15.$, cadat cathetus `.a.d.` a uertice `.a.` super basim `.b.g.`:

.. assertion:: [II. 13] <II.13>

   Per tertiamdecimam secundi :person:`Euclidis <euclid>`: auferatur quadratum de `.a.b.` ($169$) de aggregato quadratorum `.b.g.` ($196$) et `.a.g.` ($225$), remanent $.252.$; que diuisa per duplum basis $.28.$, reddunt casum maiorem $.g.d. = 9.$; et subtracto $.9.$ de $.14.$, remanet casus minor $.b.d. = 5.$. Per penultimam primi :just:`[I. 47] <I.47>`, quadratum catheti $.a.d.^2 = 169 - 25 = 144$, quare cathetus est $.12.$, et embadum est $\frac{1}{2} \times 14 \times 12 = 84$.

----

.. _dist-03-heron-la:
.. _unit-2-heron-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0047
   :page: 40–41

Regula et Demonstratio Geometrica Campi Trigonij per Tria Latera
----------------------------------------------------------------

*Versio Anglica*: :ref:`Heron's Rule & Incenter Proof (pp. 40–41) <dist-03-heron-en>` · *Commentarius*: :ref:`Notae ad Heronis Demonstrationem <dist-03-s2-notes>`

.. enunciation::

   Regula ad inueniendum embadum cuiuslibet trianguli absque inuentione catheti: Iunge tria latera ipsius trianguli in unum, et medietatem summe eorum accipe; de qua proice singula latera per se, et que remanserint seorsum tene; deinde multiplica unum residuum in aliud, et quod prouenerit multiplica in tertium residuum; et quod ex hac multiplicatione exierit, multiplica in suprascriptam medietatem: et summe huius multiplicationis accipe radicem; et ipsa erit embadum illius trianguli.

.. picture:: /_static/figures/heron_incenter_proof.svg
   :alt: Demonstratio Geometrica Regule Heronis
   :caption: Triangulus < A B G > cum bisectricibus concurrentibus in centro circuli inscripti T, cathetis perpendicularibus / T H /, / T E /, / T Z / ad latera, et basi extensa usque ad L ita ut BL sit medietas perimetri.

1. **Circulus Inscriptus et Perpendiculares Equales**: In triangulo :g:`ABG <heron_incenter_proof:< A B G >>` secentur anguli `.b.` et `.g.` per equalia per rectas :g:`BT <heron_incenter_proof:[ B T ]>` et :g:`GT <heron_incenter_proof:[ G T ]>` concurrentes in :g:`T <heron_incenter_proof:T>`. Ducantur catheti :g:`TH <heron_incenter_proof:/ T H />`, :g:`TE <heron_incenter_proof:/ T E />`, :g:`TZ <heron_incenter_proof:/ T Z />` :just:`[I. 12] <I.12>`. Quoniam triangula circa :g:`T <heron_incenter_proof:T>` sunt similia et equalia, :just:`[I. 26] <I.26>` tres perpendiculares :g:`TH <heron_incenter_proof:/ T H />`, :g:`TE <heron_incenter_proof:/ T E />`, :g:`TZ <heron_incenter_proof:/ T Z />` :eq:`sunt invicem equales <heron_incenter_proof:/ T H / = heron_incenter_proof:/ T E / = heron_incenter_proof:/ T Z />`, et circulus :g:`(TH) <heron_incenter_proof:( T H )>` contingit tria latera :just:`[IV. 4] <IV.4>`.
2. **Protractio Basis in Medietatem Perimetri**: Protrahatur :g:`BL <heron_incenter_proof:[ B L ]>` in directum ipsius :g:`BG <heron_incenter_proof:< A B G >>` usque ad :g:`L <heron_incenter_proof:L>` ita ut :g:`GL <heron_incenter_proof:/ G L />` sit equalis ipsi $AE = AZ$. Tunc tota recta $BL$ est medietas summe trium laterum ($s = 21$), et tria residua sunt $GL = s - a$, $BH = s - b$, $HG = s - c$.
3. **Embadum ex Triangulatione et Similitudine**: Embadum trianguli :g:`ABG <heron_incenter_proof:< A B G >>` est $TH \cdot BL$, et eius quadratum $TH^2 \cdot BL^2$. Per circulum auxiliarem circumscriptum et proportiones laterum ortogoniorum ostenditur:

   $$BL : BH = HG : \text{segmentum}, \qquad \text{unde} \quad TH^2 \cdot BL = GL \cdot BH \cdot HG.$$

   Et multiplicatis ambabus partibus per $BL$, perficitur demonstratio:

   $$\Delta^2 = TH^2 \cdot BL^2 = BL \cdot GL \cdot BH \cdot HG = s(s - a)(s - b)(s - c).$$

.. qed::

   Quod erat demonstrandum.

----

.. _dist-03-quad-la:
.. _unit-2-quad-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0063
   :page: 56–87

Incipit Pars Secunda Tertie Distinctionis de Campis Quadrilateris
-----------------------------------------------------------------

*Versio Anglica*: :ref:`Quadrilaterals & Polygons (pp. 56–87) <dist-03-quad-en>` · *Commentarius*: :ref:`Notae ad Quadrilateros <dist-03-s3-notes>`

Pars secunda de mensuratione quadrilaterorum et multangulorum:

* **Rhombi**: Mensurantur per medietatem multiplicationis unius dyametri in alteram orthogonalem.
* **Trapezoidia** (*Caput abscisum*): Per lineam equidistantem reducitur ad paralillogrammum et triangulum scalenum, unde elicitur cathetus et embadum $\frac{a + b}{2} \cdot h$.
* **Multangula**: Omnis figura multilatera per dyametros in triangulos resoluitur, caute refellendo errorem laicorum qui latera opposita indiscrete multiplicant.

----

.. _dist-03-circle-la:
.. _unit-2-circle-la:

.. folio:: boncompagni_1862_vol2_practica_geometriae:0095
   :page: 88–91

Incipit Pars Quarta Tertie Distinctionis de Mensuratione Circulorum
-------------------------------------------------------------------

*Versio Anglica*: :ref:`Archimedes' Circle Measurement (pp. 88–91) <dist-03-circle-en>` · *Commentarius*: :ref:`Notae ad Mensurationem Circuli <dist-03-s4-notes>`

.. enunciation::

   Ostendendum est quomodo ab :person:`Archimenide <archimedes>` philosopho inuentum sit, quod omnis circuli periferia sit tripla et septima pars dyametri sui, cum paruis numeris plenissime demonstrare.

.. picture:: /_static/figures/circle_96gon_bounds.svg
   :alt: Demonstratio Circuli per Figuram 96 Laterum
   :caption: Circulus ( C A ) super dyametrum [ C G ] cum contingente / E Z / ad A, bisectrice [ C F ] et chorda / Y A / trianguli semicircularis GYA.

1. **Figura Circumscripta 96 Laterum**: Per quatuor bisiectiones anguli semitertij recti a latere exagoni circumscripti :g:`EZ <circle_96gon_bounds:/ E Z />` ad latus $.96.$ laterum, ostenditur proportio periferie circumscripte ad dyametrum minor quam $1440 : 458\frac{1}{5} = \frac{7200}{2291} < 3\frac{1}{7}$.
2. **Figura Inscripta 96 Laterum**: Per quatuor bisectiones chordarum in semicirculo a latere exagoni :g:`YA <circle_96gon_bounds:/ Y A />` ad latus $.96.$ laterum, ostenditur proportio periferie inscripte ad dyametrum maior quam $1440 : 458\frac{4}{9} = \frac{6480}{2063} > 3\frac{10}{71}$.
3. **Proportio Leonardi ($864 : 275$)**: Accipiens medietatem $458\frac{1}{3}$, statuit Leonardo proportionem $\frac{1440}{458\frac{1}{3}} = \frac{864}{275} = 3\frac{39}{275}$, que dempta $\frac{1}{11}$ de denominatore redit in $22 : 7$.
