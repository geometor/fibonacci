:title: UNIT I NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
:layout: book

.. _unit-1-notes:

UNIT I NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
==============================================

.. rubric:: *Philological, Metrological, and Constructive Analysis of Prologus & Distinctiones I–II*

:ref:`English Edition <unit-1-en>` · :ref:`Latin (1220 / Boncompagni 1862) <unit-1-la>` · :ref:`Summary <unit-1-summary>`

----

.. _unit-1-s1-notes:

1. Master Dominicus & the Synthesis of Two Traditions
-----------------------------------------------------

The addressee :person:`Master Dominicus <dominicus>`, whom Leonardo also presented to Emperor :person:`Frederick II <frederick-ii>` at Pisa c. $1225$ (as recounted in the *Liber Quadratorum*, :cite:`fibonacci:quadratorum`), stood within the imperial court circle alongside :person:`Michael Scot <michael-scot>`, :person:`John of Palermo <john-of-palermo>`, and :person:`Theodorus of Antioch <theodorus>`.

Historically, medieval Latin geometry before $1220$ was split into two disconnected genres:

1. The contemplative *quadrivium* and twelfth-century translations of :person:`Euclid <euclid>` (:cite:`euclid:elements`), which proved theorems without numerical coordinates or unit conversions; and
2. The *agrimensores* and practical *geometriae* (descended from Roman gromatic treatises), which applied rules of thumb without Euclidean proof.

Following :person:`Abraham bar Hiyya (Savasorda) <savasorda>`'s *Liber Embadorum* ($1145$, :cite:`savasorda:embadorum`) and :person:`Gerard of Cremona <gerard-of-cremona>`'s Toledan translations from Toledo, Leonardo fuses both traditions into a single deductive-computational architecture. Notice his deliberate retention of the Greco-Arabic transliteration :term:`embadum` ($\varepsilon\mu\beta\alpha\delta\acute{o}\nu$) for planar area and the Greek alphabetic point order `.a., .b., .g., .d., .e., .z., .h., .t.` ($\alpha, \beta, \gamma, \delta, \varepsilon, \zeta, \eta, \theta$) in geometric diagrams.

----

.. _unit-1-s2-notes:

2. Strip-Measure Arithmetic in the Pisan *Pertica*
--------------------------------------------------

Why did Pisan surveyors define the **superficial pes** as a $1 \times 6$ strip ($\frac{1}{6}$ *pertica*) rather than a $1 \times 1$ unit square? Because in duodecimal/hexagesimal cross-multiplication (*perticae*, *pedes*, *unciae*), strip units make the product bilinear and shift-invariant:

$$\left(P_1 + \frac{f_1}{6} + \frac{u_1}{108}\right)\left(P_2 + \frac{f_2}{6} + \frac{u_2}{108}\right) = P_1 P_2 + \frac{P_1 f_2 + P_2 f_1}{6} + \frac{f_1 f_2}{36} + \cdots$$

Here:

* $P_1 f_2$ (*perticae* $\times$ *pedes*) directly counts **superficial pedes** ($\frac{1}{6}$ *pertica*);
* $f_1 f_2$ (*pedes* $\times$ *pedes*) directly counts **superficial denarii** ($\frac{1}{36}$ *pertica*), where $6$ *denarii* carry cleanly into $1$ superficial *pes*!

In ``geometor.fibonacci.mensuration``, ``PisanLinearMeasure``, ``multiply_pisan_lengths()``, and ``construct_pisan_pertica_grid()`` model this exact $\mathbb{Q}$ arithmetic and construct the $6 \times 6$ lattice over ``geometor.model.Model`` with zero floating-point operations:

* ``PISAN_AREA_PERTICAE["stariorum"] == sp.Integer(66)``
* ``PisanLinearMeasure(7)`` frontage $\times$ ``PisanLinearMeasure(9, 2, sp.Rational(72, 7))`` depth $= 66$ superficial *perticae* ($1$ *stariorum*).

----

.. _unit-1-s3-notes:

3. Euclid Book II as the Engine of *Al-Jabr*
--------------------------------------------

Leonardo's inclusion of :cite:`euclid:elements` II.4–10 in *Distinctio I* is not merely ornamental. Throughout *Practica Geometriae* (especially in *Distinctio III* quadrilaterals, *Distinctio IV* consortium divisions, and *Distinctio VIII* *subtilitates*), quadratic equations in :term:`res` ($x$) and :term:`census` ($x^2$) are reduced directly to Book II gnomons:

* $x^2 + bx = c \iff$ Euclid II.6 (line $b$ bisected with $x$ adjoined in a straight line: $(x + \tfrac{b}{2})^2 = c + (\tfrac{b}{2})^2$);
* $bx - x^2 = c \iff$ Euclid II.5 (line $b$ bisected and cut unequally at $x$: $(\tfrac{b}{2})^2 - (\tfrac{b}{2} - x)^2 = c$).

----

.. _unit-1-s4-notes:

4. Newton–Heron Quadratic Convergence in *Distinctio II*
--------------------------------------------------------

Leonardo's two-step square-root rule $a_1 = a + \frac{r}{2a}$, $a_2 = a_1 - \frac{a_1^2 - N}{2a_1}$ is algebraically identical to two iterations of Newton's method on $f(t) = t^2 - N$ starting from $t_0 = a \in \mathbb{Z}_{>0}$. The residual error after the second step satisfies:

$$0 < a_2 - \sqrt{N} < \frac{(N - a^2)^4}{128\, a^7},$$

achieving four- to six-place sexagesimal or metrological accuracy in two elementary rational divisions.
