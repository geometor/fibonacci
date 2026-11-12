.. _modules:

Python API Reference
====================

.. rubric:: *Exact Symbolic Modules in* ``geometor.fibonacci``

``geometor.fibonacci`` implements every construction and algebraic verification in 100% exact symbolic ``SymPy`` arithmetic and ``geometor.model.Model(..., auto_intersect=False)`` targeted Euclidean DAGs—with zero ``float`` or ``sp.Float`` coordinates.

Module Overview
---------------

* :mod:`geometor.fibonacci.mensuration` — Pisan agrarian metrology (*Introductoria* & *Distinctio I*), Heron's incenter proof (*Distinctio III*, pp. 40–41), and 96-gon circle bounds ($\pi \approx \frac{864}{275}$, pp. 88–91).
* :mod:`geometor.fibonacci.divisions` — Euclidean planar field divisions (*Distinctio IV*, pp. 110–148): cuts from a point on a side, parallel to the base via semicircle mean proportional, three-consort centroid partition, and root-mean-square trapezoid division.
* :mod:`geometor.fibonacci.polyhedra_golden` — The five regular polyhedra in a sphere of diameter $6$ (*Distinctio VI*, pp. 190–202), optical *quadrans* surveying (*Distinctio VII*), pentagon & decagon in diameter $10$ (*Distinctio VIII*), *Flos* cubic & *congruum* challenges (1225), and *Liber Abaci* Ch. 12 rabbit convergents to $\phi$.
* :mod:`geometor.fibonacci.render` — Publication-grade interactive ``.euclid-graphic`` SVG exporter with dark/light CSS variables, 3-vertex ``<path>`` geometry, and canonical ``data-ref`` / ``data-aliases`` wiring.
* :mod:`geometor.fibonacci.sphinx_ext` — Runtime Sphinx hook registering ``Latin (1220 / Boncompagni 1862)`` in ``photon_platform.publish.book`` and binding local ``objects.inv`` inventories.

.. include:: api/geometor/fibonacci/index.rst
