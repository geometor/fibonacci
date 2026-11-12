:title: UNIT V NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
:layout: book

.. _unit-5-notes:

UNIT V NOTES — SCHOLARLY & SYMBOLIC COMMENTARY
==============================================

.. rubric:: *Abū Kāmil's Pentagon Algebra, the Irreducibility of the Flos Cubic, and Golden Convergence*

:ref:`English Edition <unit-5-en>` · :ref:`Latin (1220 / Boncompagni 1862) <unit-5-la>` · :ref:`Summary <unit-5-summary>`

----

.. _unit-5-s1-notes:

1. The *Quadrans* Shadow Square as Pre-Trigonometric Cotangent/Tangent
----------------------------------------------------------------------

On the medieval :term:`quadrans` ($12 \times 12$ *puncta*), *umbra recta* ($u_r$) and *umbra versa* ($u_v$) encode exact rational cotangent and tangent scales scaled by $12$:

$$u_r = 12 \cot\theta, \qquad u_v = 12 \tan\theta, \qquad u_r \cdot u_v = 144.$$

By switching between *umbra recta* for $\theta \ge 45^\circ$ and *umbra versa* for $\theta \le 45^\circ$, the surveyor always reads an integer scale bounded in $[0, 12]$, avoiding unbounded tangents near the zenith! ``construct_quadrans_surveying()`` models this exact $12 \times 12$ lattice and plumb-line intersection in ``geometor.model``.

----

.. _unit-5-s2-notes:

2. Abū Kāmil's *Kitāb fī al-mukhammas wa-al-muʿashshar* in *Distinctio VIII*
----------------------------------------------------------------------------

Roshdi Rashed and Barnabas Hughes have traced *Distinctio VIII*'s pentagon and decagon equations directly to :person:`Abū Kāmil Shujāʿ ibn Aslam <abu-kamil>`'s tenth-century treatise *On the Pentagon and Decagon* (:cite:`fibonacci:pg-8`). What makes this chapter historic is the **bidirectional isomorphism between Euclid Book XIII and Arabic *al-jabr***:

* In :person:`Euclid <euclid>` XIII.10, $s_5^2 = r^2 + s_{10}^2$ is proved purely by congruent triangles and arcs without numbers;
* In *Distinctio VIII*, setting $d = 10$ turns Euclid's **apotome** ($s_{10}$) and **minor** ($s_5$) lines into concrete nested radical expressions over $\mathbb{Q}(\sqrt{5})$ solved via *census census* ($x^4 + 3125 = 125x^2$), verified symbolically in ``solve_pentagon_ptolemy_quartic(10)``.

----

.. _unit-5-s3-notes:

3. Galois Theory Avant la Lettre in *Flos* (1225)
-------------------------------------------------

John of Palermo borrowed the cubic $x^3 + 2x^2 + 10x = 20$ from ʿUmar al-Khayyāmī's *Treatise on Algebra* (where it is constructed by intersecting a circle and a rectangular hyperbola). Instead of stopping at conic intersection, Leonardo asks a genuinely **number-theoretic question**: can the root $x$ belong to any of the thirteen quadratic irrational classes of Euclid Book X?

In modern field theory, $P(x) = x^3 + 2x^2 + 10x - 20$ is irreducible over $\mathbb{Q}$ (by the Rational Root Theorem on divisors of $20$), so $[\mathbb{Q}(x) : \mathbb{Q}] = 3$. Every Euclidean Book X irrational generates an iterated quadratic tower of degree $2^k$; since $3 \nmid 2^k$, **$x$ cannot lie in any Euclidean ruler-and-compass field**! Leonardo's elimination of Book X binomials, apotomes, and medials in $1225$ is the earliest known European proof that a cubic algebraic irrational transcends Euclid Book X.

In ``flos_sexagesimal_cubic()``, evaluating $P\!\left(\frac{1{,}596{,}577{,}777}{1{,}166{,}400{,}000}\right)$ yields a residual of $+5.40 \times 10^{-10}$, corresponding to a root error of $+3.18 \times 10^{-11}$ (only the sixth sexagesimal place $40''''''$ differs by $1$ unit from the closest possible rounding $39''''''$!).

----

.. _unit-5-s4-notes:

4. From *Liber Abaci* Rabbits to the Divine Proportion
------------------------------------------------------

Although *Liber Abaci* (Vol. I, pp. 283–284) presents the rabbit sequence as an exercise in additive recurrence, ``fibonacci_rabbit_convergents(12)`` and ``verify_cassini_identity()`` reveal why the GEOMETOR ecosystem (`geometor/divine`, `geometor/phyllotaxis`, `geometor/pacioli`) treats *Liber Abaci* XII and *Practica Geometriae* VI/VIII as two halves of a single mathematical jewel:

$$\frac{F_{n+1}}{F_n} - \phi = \frac{(-1)^n}{F_n (F_n \phi + F_{n-1})}, \qquad \frac{377}{233} \approx 1.61802575 \quad (\text{error } 8.2 \times 10^{-6}\text{ from } \phi).$$

Every golden chord constructed by compass and straightedge in ``dodecahedron_golden_chord.svg`` and ``pentagon_decagon_circle.svg`` is the geometric limit of the rational integer ratios generated in *Liber Abaci*!
