:title: UNITAS III — DISTINCTIO IV: DE DIVISIONE CAMPORUM INTER CONSORTES
:layout: book

.. _unit-3-la:

UNITAS III — DISTINCTIO IV: DE DIVISIONE CAMPORUM INTER CONSORTES
=================================================================

.. rubric:: *Liber Divisionum Euclidis Latinitate Donatus et Ampliatus: Trigoni, Quadrilatera, Trapezia et Circuli*

**Fons Criticus**: :cite:`boncompagni:1862` (*Scritti di Leonardo Pisano, Vol. II, pp. 110–148 · Cod. Urb. Lat. 292, fol. 67v–92v*) · :ref:`English Translation <unit-3-en>` · :ref:`Summary <unit-3-summary>` · :ref:`GEOMETOR Notes <unit-3-notes>`

----

.. _unit-3-sidepoint-la:

.. folio:: fol. 67v–69r
   :page: 110–112

De Divisione Trigonorum ab Angulo vel a Puncto Dato in Latere
-------------------------------------------------------------

*Versio Anglica*: :ref:`Dividing Triangles from a Vertex or Side Point (pp. 110–112) <unit-3-sidepoint-en>` · *Commentarius*: :ref:`Notae ad Librum Divisionum Euclidis <unit-3-s1-notes>`

.. enunciation::

   Explicit distinctio tertia; incipit quarta de divisione camporum inter :term:`consortes`.

1. **Divisio ab Angulo**: Si trigonus `.abg.` dividendus sit in duas vel plures partes equales ab uno eius angulo `.a.`, dividatur basis opposita `.bg.` in totidem partes equales et protrahantur linee ab `.a.` ad puncta divisionis; trigoni enim sub eadem altitudine constituti eandem habent inter se proportionem quam bases. :just:`[VI. 1] <VI.1>`
2. **Lemma de Trigonis Unum Angulum Equalem Habentibus**: Premittitur quod duorum trigonorum habentium unum angulum equalem (utpote angulum `.g.`), proportio alterius ad alterum componitur ex proportione laterum continentium ipsum angulum equalem. :just:`[VI. 23] <VI.23>`
3. **Divisio in Duo Equalia a Puncto Dato in Latere**: Sit dividendus trigonus :g:`ABG <division_side_point:< A B G >>` in duas partes equales per lineam exeuntem a dato puncto :g:`D <division_side_point:D>` posito in latere :g:`BE <division_side_point:[ B E ]>`.

.. picture:: /_static/figures/division_side_point.svg
   :alt: Divisio Trigoni ABG in Duo Equalia a Puncto D in Latere
   :caption: Trigonus < A B G > (13, 14, 15) divisus a puncto D (BD = 5, DG = 9) per punctum medium E et equidistantem [ E Z ] ad [ A D ], efficiens lineam divisionis / D Z / (GZ = 11 2/3).

* **Constructio et Demonstratio**: Secetur basis per equalia in :g:`E <division_side_point:E>` et protrahatur :g:`AE <division_side_point:/ A E />` ac :g:`AD <division_side_point:[ A D ]>`; a puncto autem :g:`E <division_side_point:E>` ducatur linea :g:`EZ <division_side_point:[ E Z ]>` equidistans ipsi :g:`AD <division_side_point:[ A D ]>` :just:`[I. 31] <I.31>` secans latus :g:`GZ <division_side_point:[ G Z ]>` in :g:`Z <division_side_point:Z>`, et copuletur :g:`DZ <division_side_point:/ D Z />`. Quoniam trigoni $ADE$ et $ADZ$ sunt super eandem basim :g:`AD <division_side_point:[ A D ]>` et in eisdem equidistantibus, sunt invicem equales; :just:`[I. 37] <I.37>` addito igitur communi $EDG$, erit trigonus :g:`DZG <division_side_point:< D Z G >>` equalis trigono $AEG$, hoc est dimidio totius :g:`ABG <division_side_point:< A B G >>`, reliquumque quadrilaterum :g:`ABDZ <division_side_point:< A B D Z >>` erit reliquum dimidium.
* **Exemplum in Numeris**: Sit $AB = 13$, $BG = 14$, $GA = 15$, $BD = 5$, et $DG = 9$. Quia $GD$ ($9$) ad $GE$ ($7$) est sicut $GA$ ($15$) ad $GZ$, :just:`[VI. 2] <VI.2>` multiplicetur $7$ in $15$ ($105$) et dividatur per $9$: provenit $GZ = 11\frac{2}{3}$, utraque autem pars continet perticas $.XLII.$ ($42$).

----

.. _unit-3-centroid-la:

.. folio:: fol. 69r–74r
   :page: 112–120

Preparatoria de Concursu Mediarum et Divisio Inter Tres Consortes
-----------------------------------------------------------------

*Versio Anglica*: :ref:`Concurrency of Medians & Centroid Division (pp. 112–120) <unit-3-centroid-en>` · *Commentarius*: :ref:`Notae ad Centrum Gravitatis D <unit-3-s2-notes>`

.. picture:: /_static/figures/division_medians_centroid.svg
   :alt: Concursus Trium Linearum Mediarum in Puncto D et Divisio Inter Tres Consortes
   :caption: Trigonus < A B G > divisus per lineas / A D /, / B D /, / G D / concurrentes in puncto D in tres trigonos equales < D A B >, < D B G > et < D G A >.

.. lemma::

   *Preparatoria*: In omni trigono :g:`ABG <division_medians_centroid:< A B G >>` tres linee protracte ab angulis ad puncta media :g:`E <division_medians_centroid:E>`, :g:`Z <division_medians_centroid:Z>`, :g:`T <division_medians_centroid:T>` oppositorum laterum concurrunt simul in uno puncto :g:`D <division_medians_centroid:D>`, ita ut portio versus quemlibet angulum sit **dupla** portionis relique ($AD = 2\,DE$, $BD = 2\,DZ$, $GD = 2\,DT$).

Copulata enim $EZ$, est $AB$ dupla ipsius $EZ$; :just:`[VI. 2] <VI.2>` quare per similitudinem trigonorum est :g:`AD <division_medians_centroid:/ A D />` dupla ipsius $DE$ et :g:`BD <division_medians_centroid:/ B D />` dupla ipsius $DZ$, similiterque tertia linea :g:`GT <division_medians_centroid:[ B T ]>` transit per idem punctum :g:`D <division_medians_centroid:D>`.

Unde si tres consortes voluerint dividere campum trigonum :g:`ABG <division_medians_centroid:< A B G >>` habentem puteum vel terminum in :g:`D <division_medians_centroid:D>`, protractis :g:`AD <division_medians_centroid:/ A D />`, :g:`BD <division_medians_centroid:/ B D />`, :g:`GD <division_medians_centroid:/ G D />`, efficiuntur tres trigoni equales :g:`DAB <division_medians_centroid:< D A B >>`, :g:`DBG <division_medians_centroid:< D B G >>`, et :g:`DGA <division_medians_centroid:< D G A >>`, quorum unusquisque est tertia pars totius trigoni (in trigono $13, 14, 15$ pertice $.XXVIII.$). Ostenditur insuper divisio trigoni per quodlibet punctum datum intra vel extra trigonum (*pp. 113–117*). :just:`[VI. 28–29] <VI.28>`

----

.. _unit-3-parallel-la:

.. folio:: fol. 73r–73v
   :page: 118–119

Divisio Trigoni per Lineam Equidistantem Basi
---------------------------------------------

*Versio Anglica*: :ref:`Dividing a Triangle Parallel to Its Base (p. 119) <unit-3-parallel-en>` · *Commentarius*: :ref:`Notae ad Semicirculum Mediae Proportionalis <unit-3-s3-notes>`

.. enunciation::

   Datum trigonum :g:`ABG <division_parallel_base:< A B G >>` dividere in duo equalia per lineam :g:`EZ <division_parallel_base:/ E Z />` equidistantem basi :g:`BG <division_parallel_base:[ B G ]>`.

.. picture:: /_static/figures/division_parallel_base.svg
   :alt: Divisio Trigoni ABG per Lineam EZ Equidistantem Basi BG
   :caption: Trigonus < A B G > (10, 14, 12) divisus per lineam / E Z / equidistantem basi [ B G ] mediante semicirculo ( O1 B ) et catheto mediae proportionalis / A K /.

Protrahatur latus :g:`BE <division_parallel_base:[ B E ]>` extra :g:`A <division_parallel_base:A>` usque in :g:`D <division_parallel_base:D>`, sitque :g:`AD <division_parallel_base:/ A D />` dimidium ipsius $BA$. Super dyametrum $BD$ describatur semicirculus :g:`(O1B) <division_parallel_base:( O1 B )>`, erigaturque a puncto :g:`A <division_parallel_base:A>` perpendicularis :g:`AK <division_parallel_base:/ A K />` usque ad circumferentiam in :g:`K <division_parallel_base:K>`, :just:`[VI. 13] <VI.13>` et secundum spatium :g:`AK <division_parallel_base:/ A K />` describatur circulus :g:`(AK) <division_parallel_base:( A K )>` secans $AB$ in :g:`E <division_parallel_base:E>`, unde ducatur :g:`EZ <division_parallel_base:/ E Z />` equidistans basi :g:`BG <division_parallel_base:[ B G ]>`.

Quoniam $BA$ ad $EA$ ($= AK$) est sicut $EA$ ad $AD$, erit $BA^2$ ad $EA^2$ sicut $BA$ ad $AD$, hoc est dupla; sed trigonus :g:`ABG <division_parallel_base:< A B G >>` ad trigonum :g:`AEZ <division_parallel_base:< A E Z >>` habet proportionem duplicatam lateris $BA$ ad $EA$; :just:`[VI. 19] <VI.19>` igitur trigonus :g:`AEZ <division_parallel_base:< A E Z >>` equalis est residuo quadrilatero :g:`EBGZ <division_parallel_base:< E B G Z >>`. In trigono ubi $AB = 10$, $BG = 14$, $AG = 12$, erit $AD = 5$, et:

$$AE^2 = 50, \qquad AZ^2 = 72, \qquad EZ^2 = 98.$$

----

.. _unit-3-trapezoid-la:

.. folio:: fol. 78r–92v
   :page: 126–148

De Divisione Quadrilaterorum, Trapeziorum et Circulorum
-------------------------------------------------------

*Versio Anglica*: :ref:`Divisions of Quadrilaterals, Trapezoids & Circles (pp. 126–148) <unit-3-trapezoid-en>` · *Commentarius*: :ref:`Notae ad Divisionem Trapezij <unit-3-s3-notes>`

In campo caput absciso (trapezio) habente caput $a$ et basim $b$ equidistantem, linea media $c$ dividens campum in duo equalia equidistanter basibus invenitur accipiendo **radicem medietatis aggregati quadratorum** capitis et basis:

$$c = \sqrt{\frac{a^2 + b^2}{2}} \qquad \text{(ut in } a = 7,\ b = 17 \implies c = \sqrt{169} = 13\text{)};$$

universaliter vero secundum proportionem $p : q$ est $c^2 = \frac{q a^2 + p b^2}{p + q}$. Subiunguntur divisiones quadrilaterorum diversilaterorum, pentagonorum, circulorum, semicirculorum et portionum circuli (:cite:`euclid:divisions`).

.. qed::

   Explicit distinctio quarta de divisione camporum.
