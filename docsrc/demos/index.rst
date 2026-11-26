:order: 25
:nav_title: Demos

.. _demos:

Exact Symbolic Demonstrations
=============================

.. rubric:: *Runnable SymPy & geometor.model Verification Suites*

In strict accordance with GEOMETOR's separation of archival treatise text and executable code, all symbolic constructions, polynomial verifications, and CLI tables live in ``src/geometor/fibonacci/`` and ``demos/`` rather than inside the historical codex pages.

Run any demonstration directly from the repository root:

.. code-block:: bash

   uv run --no-sync python3 demos/mensuration_demo.py
   uv run --no-sync python3 demos/divisions_demo.py
   uv run --no-sync python3 demos/polyhedra_golden_demo.py

----

1. Mensuration, Heron's Incenter Proof & Circle Bounds
------------------------------------------------------

``demos/mensuration_demo.py`` exercises :mod:`geometor.fibonacci.mensuration` across *Distinctio I* and *Distinctio III*:

* Exact rational conversion across the Pisan :term:`pertica`, :term:`pes`, :term:`uncia`, :term:`denarius`, :term:`panorum`, and :term:`stariorum` (66 square *perticae*).
* Symbolic verification over :math:`\mathbb{Z}[x, y, z]` and geometric :class:`~geometor.model.Model` construction of Fibonacci's incenter proof of Heron's formula on :math:`(13, 14, 15)` (:math:`T = (6, 4)`, :math:`r = 4`, :math:`s = 21`, :math:`\Delta = 84`).
* Exact rational comparison of Fibonacci's 96-gon bounds :math:`\frac{6480}{2063} < \pi < \frac{7200}{2291}` and :math:`\pi_{\text{Fib}} = \frac{864}{275}` against Archimedes' :math:`\frac{223}{71}` and :math:`\frac{22}{7}`.

.. literalinclude:: ../../demos/mensuration_demo.py
   :language: python
   :linenos:

----

2. Division of Planar Fields (*De divisione camporum*)
------------------------------------------------------

``demos/divisions_demo.py`` exercises :mod:`geometor.fibonacci.divisions` on *Distinctio IV* (preserving Euclid's *On Divisions of Figures*):

* Straightedge-and-compass division of :math:`\triangle ABG` from an arbitrary point :math:`D` on side :math:`[BG]` in ratio :math:`p : q` via parallel transfer :math:`[EZ] \parallel [AD]` (:math:`GZ = \frac{35}{3} = 11\frac{2}{3}` when :math:`BD = 5`, :math:`p = q = 1`).
* Semicircle mean-proportional construction (:math:`AE^2 = \frac{p}{p+q} AB^2`) cutting :math:`\triangle ABG` parallel to base :math:`[BG]`, reproducing Boncompagni p. 119 (:math:`AE^2 = 50`, :math:`AZ^2 = 72`, :math:`EZ^2 = 98` on sides :math:`10, 14, 12`).
* Concurrency of medians at centroid :math:`D = X(2)` in :math:`2 : 1` ratio, partitioning :math:`\triangle ABG` into three equal consort shares, plus root-mean-square trapezoid bisection on :math:`(7, 17)` yielding chord :math:`13` (:math:`7^2, 13^2, 17^2` in arithmetic progression).

.. literalinclude:: ../../demos/divisions_demo.py
   :language: python
   :linenos:

----

3. Regular Polyhedra, Extreme & Mean Ratio, *Flos* & *Liber Abaci*
------------------------------------------------------------------

``demos/polyhedra_golden_demo.py`` exercises :mod:`geometor.fibonacci.polyhedra_golden` across *Distinctio VI–VIII*, *Flos* (1225), and *Liber Abaci* Ch. 12:

* Simultaneous planar construction of all five Platonic solid edges in a sphere of diameter 6 (:math:`e_4^2 = 24`, :math:`e_8^2 = 18`, :math:`e_6^2 = 12`, :math:`e_{12}^2 = 18 - 6\sqrt{5}`, :math:`e_{20}^2 = 18 - \frac{18}{5}\sqrt{5}`) and Hypsicles' Book XIV theorem :math:`V_{12}/V_{20} = e_6/e_{20} = \sqrt{\frac{5 + \sqrt{5}}{6}}`.
* Inscription of the regular pentagon and decagon in diameter 10 via Euclid XIII.9–10 and Ptolemy's *census census* quartic :math:`x^4 + 3125 = 125x^2`.
* Verification of John of Palermo's *congruum* triple :math:`(\frac{31}{12}, \frac{41}{12}, \frac{49}{12})`, the *Flos* sexagesimal cubic root :math:`1;22,7,42,33,4,40 = \frac{39931699}{29160000}`, and the twelve-month rabbit ratio convergents :math:`F_{n+1}/F_n \to \phi`.

.. literalinclude:: ../../demos/polyhedra_golden_demo.py
   :language: python
   :linenos:
