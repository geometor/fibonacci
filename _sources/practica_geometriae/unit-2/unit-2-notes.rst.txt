:title: UNIT II NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
:layout: book

.. _unit-2-notes:

UNIT II NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
===============================================

.. rubric:: *Heron's Formula, Rational Trigonometry, and Fibonacci's Small-Number Archimedean Bounds*

:ref:`English Edition <unit-2-en>` · :ref:`Latin (1220 / Boncompagni 1862) <unit-2-la>` · :ref:`Summary <unit-2-summary>`

----

.. _unit-2-s1-notes:

1. The Canonical $(13, 14, 15)$ Heronian Triangle
-------------------------------------------------

Built by juxtaposing the Pythagorean right triangles $(5, 12, 13)$ and $(9, 12, 15)$ back-to-back along their common :term:`cathetus` $12$, the $(13, 14, 15)$ scalene triangle is the universal benchmark of ancient and medieval mensuration—appearing in :person:`Heron <heron>`'s *Metrica* I.8 (:cite:`heron:metrica`), :person:`Savasorda <savasorda>`'s *Liber Embadorum* (:cite:`savasorda:embadorum`), and throughout *Practica Geometriae* (*Dist. III* and *Dist. IV*).

In ``geometor.fibonacci.mensuration.construct_heron_incenter_proof()``, with $B = (0, 0)$, $G = (14, 0)$, and $A = (5, 12)$:

* The angle bisectors meet at the exact rational **incenter** $X(1) = T = (6, 4)$ (cross-referenced to ``geometor/etc`` `X(1)`);
* All three perpendicular feet are exact over $\mathbb{Q}$: $H = (6, 0)$, $E = \left(\frac{42}{13}, \frac{100}{13}\right)$, $Z = \left(\frac{46}{5}, \frac{32}{5}\right)$, with common **inradius quadrance** $Q(T, H) = Q(T, E) = Q(T, Z) = 16$ ($r = 4$);
* Extending $[BG]$ to $L = (21, 0)$ realizes $BL = 21 = s$, with $BH = 6 = s - 15$, $HG = 8 = s - 13$, and $GL = 7 = s - 14$.

----

.. _unit-2-s2-notes:

2. Heron's Polynomial Identity & Archimedes' Theorem
----------------------------------------------------

Leonardo did not read Heron's Greek *Metrica* directly (which remained in Constantinople until its rediscovery in $1896$); instead, he drew the incenter proof through the ninth-century Baghdadi treatise of the :person:`Banū Mūsā <banu-musa>`, translated at Toledo by :person:`Gerard of Cremona <gerard-of-cremona>` as *Verba filiorum Moysi filii Sekir* (:cite:`banu-musa:verba`).

In Rational Trigonometry (`geometor/wildberger`), ``verify_heron_polynomial_identity()`` proves over $\mathbb{Z}[x, y, z]$ that Heron's factored semiperimeter product is identically **Archimedes' quadrea formula** in terms of side quadrances $Q_1 = a^2, Q_2 = b^2, Q_3 = c^2$:

$$16\Delta^2 = 16 s(s-a)(s-b)(s-c) = (a+b+c)(-a+b+c)(a-b+c)(a+b-c) = 4 Q_1 Q_2 - (Q_1 + Q_2 - Q_3)^2.$$

----

.. _unit-2-s3-notes:

3. Refuting the Agrimensor Quadrilateral Fallacy
------------------------------------------------

Roman gromatic manuals routinely approximated any four-sided field $(a, b, c, d)$ by $\frac{a+c}{2}\cdot\frac{b+d}{2}$. By Brahmagupta's and Bretschneider's identities, for a quadrilateral with semiperimeter $s$ and opposite angles $\alpha, \gamma$:

$$\Delta^2 = (s-a)(s-b)(s-c)(s-d) - abcd \cos^2\!\left(\frac{\alpha + \gamma}{2}\right) \le \left(\frac{a+c}{2}\right)^2 \left(\frac{b+d}{2}\right)^2,$$

with equality if and only if $a = c$, $b = d$, and $\alpha = \gamma = 90^\circ$. Leonardo insists that at least one diagonal or angle must be measured so the quadrilateral is decomposed into rigid Euclidean triangles.

----

.. _unit-2-s4-notes:

4. Why Fibonacci's $\frac{864}{275}$ Improves Upon $\frac{22}{7}$
-----------------------------------------------------------------

In :cite:`archimedes:circle`, :person:`Archimedes <archimedes>` started his $30^\circ$ rational bounds from $265 < 153\sqrt{3} < 1351/5$, producing four-digit numerators and denominators ($14{,}688$ and $4{,}673\frac{1}{2}$). Leonardo instead fixes the circle diameter uniformly at $d = 1440$ ($r = 720 = 6!$), a highly composite sexagesimal-duodecimal scale in which all four bisections remain transparent.

Comparing absolute errors against $\pi = 3.14159265358979\dots$ (verified in ``fibonacci_circle_bounds()``):

* Archimedean upper bound $\frac{22}{7} \approx 3.14285714$: error $+1.264 \times 10^{-3}$;
* Fibonacci's circumscribed upper bound $\frac{7200}{2291} \approx 3.14273243$: error $+1.140 \times 10^{-3}$;
* Fibonacci's inscribed lower bound $\frac{6480}{2063} \approx 3.14105671$: error $-5.359 \times 10^{-4}$;
* **Fibonacci's mean ratio $\frac{864}{275} \approx 3.14181818$**: error **$+2.255 \times 10^{-4}$**—more than **five times closer** to $\pi$ than $\frac{22}{7}$!
