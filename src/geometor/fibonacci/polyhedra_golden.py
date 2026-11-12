r"""Exact regular polyhedra in a sphere ($d=6$), extreme & mean ratio ($\phi$), *Distinctio VIII*, *Flos*, and *Liber Abaci*.

Grounded directly in Baldassarre Boncompagni's critical Latin editions (*Scritti di Leonardo Pisano*,
Vol. I, 1857 & Vol. II, 1862):

- **Distinctio VI — The Five Regular Polyhedra in a Sphere of Diameter $6$** (Vol. II, pp. 190–202,
  ``fol. 122v–130v``): Exact symbolic metrics and straightedge-and-compass planar constructions for
  the tetrahedron ($e_4^2 = 24$), octahedron ($e_8^2 = 18$), cube ($e_6^2 = 12$), dodecahedron
  ($e_{12} = \sqrt{15} - \sqrt{3}$, $e_{12}^2 = 18 - \sqrt{180}$), and icosahedron
  ($e_{20}^2 = 18 - \sqrt{64\frac{4}{5}}$), together with Hypsicles' Book XIV volume proportion
  $V_{12} : V_{20} = e_6 : e_{20} = \sqrt{\frac{5 + \sqrt{5}}{6}}$.
- **Distinctio VII — Optical Surveying with the *Quadrans*** (Vol. II, pp. 202–206, ``fol. 131r–133v``):
  Exact geometric model of Fibonacci's 12-part *umbra recta / umbra versa* quadrant ``dhai``.
- **Distinctio VIII — *Subtilitates Geometricae*** (Vol. II, pp. 207–224, ``fol. 134r–148r``):
  Inscribing the regular pentagon and decagon in a circle of diameter $10$ both algebraically via
  Ptolemy's theorem ($x^4 + 3125 = 125 x^2$) and geometrically via Euclid XIII.9–10.
- ***Flos* (1225) & *Liber Abaci* (1202/1228) Bridges**:
  John of Palermo's *congruum* challenge ($x = \frac{41}{12}$, $x^2 \pm 5 = \square$), the cubic
  $x^3 + 2x^2 + 10x = 20$ solved to six sexagesimal places ($1;22,7,42,33,4,40$), and the twelve-month
  rabbit recurrence $F_{n+1} = F_n + F_{n-1}$ whose ratios $F_{n+1}/F_n$ converge monotonically in
  alternating bounds to $\phi = \frac{1 + \sqrt{5}}{2}$.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test

from geometor.fibonacci.divisions import _divide_segment_in_ratio, construct_midpoint

__all__ = [
    "PHI",
    "PSI",
    "PolyhedronMetrics",
    "SpherePolyhedraSectionResult",
    "GoldenChordResult",
    "PentagonDecagonResult",
    "RabbitConvergentRow",
    "FlosCubicResult",
    "polyhedra_in_sphere",
    "verify_hypsicles_xiv_ratio",
    "construct_sphere_polyhedra_section",
    "construct_dodecahedron_golden_chord",
    "construct_pentagon_decagon_in_circle",
    "solve_pentagon_ptolemy_quartic",
    "construct_quadrans_surveying",
    "fibonacci_rabbit_convergents",
    "verify_cassini_identity",
    "flos_sexagesimal_cubic",
    "flos_congruum_squares",
]

PHI: sp.Expr = (sp.Integer(1) + sp.sqrt(5)) / 2
PSI: sp.Expr = (sp.Integer(1) - sp.sqrt(5)) / 2


@dataclass(frozen=True)
class PolyhedronMetrics:
    """Exact symbolic invariants of a regular polyhedron inscribed in a sphere of diameter $d$."""

    name: str
    latin_name: str
    faces: int
    vertices: int
    edges: int
    sphere_diameter: sp.Expr
    edge: sp.Expr
    edge_sq: sp.Expr
    face_circumradius_sq: sp.Expr
    insphere_radius_sq: sp.Expr
    surface_area: sp.Expr
    volume: sp.Expr


def polyhedra_in_sphere(diameter: int | sp.Expr = 6) -> dict[str, PolyhedronMetrics]:
    """Return exact symbolic metrics for all five Platonic solids in a sphere of ``diameter`` (default $6$).

    Matches Fibonacci's exact expressions in *Practica Geometriae*, *Distinctio VI* (Boncompagni 1862,
    pp. 190–202) for $d = 6$:

    - Tetrahedron (*pyramis*): $e_4^2 = 24$, $V_4 = 8\\sqrt{3}$.
    - Cube (*cubus*): $e_6^2 = 12$, $V_6 = 24\\sqrt{3} = 3 V_4$.
    - Octahedron (*octaedron*): $e_8^2 = 18$, $V_8 = 36$.
    - Dodecahedron (*duodecaedron*): $e_{12} = \\sqrt{15} - \\sqrt{3}$, $e_{12}^2 = 18 - 6\\sqrt{5}$,
      $r_{f,12}^2 = 6 - \\frac{6}{5}\\sqrt{5}$, $r_{\\text{in},12}^2 = 3 + \\frac{6}{5}\\sqrt{5}$.
    - Icosahedron (*ycosaedron*): $e_{20}^2 = 18 - \\frac{18}{5}\\sqrt{5}$,
      $r_{f,20}^2 = 6 - \\frac{6}{5}\\sqrt{5}$, $r_{\\text{in},20}^2 = 3 + \\frac{6}{5}\\sqrt{5}$.
    """
    d = sp.sympify(diameter)
    r_sph_sq = d**2 / 4
    s2 = sp.sqrt(2)
    s3 = sp.sqrt(3)
    s5 = sp.sqrt(5)

    # 1. Tetrahedron (4 triangular faces)
    e4_sq = sp.simplify(sp.Rational(2, 3) * d**2)
    e4 = sp.simplify(sp.sqrt(e4_sq))
    rf4_sq = sp.simplify(e4_sq / 3)
    rin4_sq = sp.simplify(r_sph_sq - rf4_sq)
    surf4 = sp.simplify(s3 * e4_sq)
    vol4 = sp.simplify(s2 * e4**3 / 12)

    # 2. Cube / Hexahedron (6 square faces)
    e6_sq = sp.simplify(sp.Rational(1, 3) * d**2)
    e6 = sp.simplify(sp.sqrt(e6_sq))
    rf6_sq = sp.simplify(e6_sq / 2)
    rin6_sq = sp.simplify(r_sph_sq - rf6_sq)
    surf6 = sp.simplify(6 * e6_sq)
    vol6 = sp.simplify(e6**3)

    # 3. Octahedron (8 triangular faces)
    e8_sq = sp.simplify(sp.Rational(1, 2) * d**2)
    e8 = sp.simplify(sp.sqrt(e8_sq))
    rf8_sq = sp.simplify(e8_sq / 3)
    rin8_sq = sp.simplify(r_sph_sq - rf8_sq)
    surf8 = sp.simplify(2 * s3 * e8_sq)
    vol8 = sp.simplify(s2 * e8**3 / 3)

    # 4. Dodecahedron (12 pentagonal faces): e12 = e6 / phi = d * (sqrt(15) - sqrt(3)) / 6
    e12 = sp.simplify(d * (sp.sqrt(15) - s3) / 6)
    e12_sq = sp.expand(e12**2)
    rf12_sq = sp.expand((sp.Integer(5) - s5) * d**2 / 30)
    rin12_sq = sp.expand(r_sph_sq - rf12_sq)
    surf12 = sp.simplify(3 * sp.sqrt(25 + 10 * s5) * e12_sq)
    vol12 = sp.simplify(surf12 * sp.sqrt(rin12_sq) / 3)

    # 5. Icosahedron (20 triangular faces): shares face circumcircle with dodecahedron (Hypsicles XIV.2)
    rf20_sq = rf12_sq
    e20_sq = sp.expand(3 * rf20_sq)
    e20 = sp.simplify(sp.sqrt(e20_sq))
    rin20_sq = rin12_sq
    surf20 = sp.simplify(5 * s3 * e20_sq)
    vol20 = sp.simplify(surf20 * sp.sqrt(rin20_sq) / 3)

    return {
        "tetrahedron": PolyhedronMetrics(
            name="Tetrahedron",
            latin_name="Pyramis (quatuor basium triangularium)",
            faces=4,
            vertices=4,
            edges=6,
            sphere_diameter=d,
            edge=e4,
            edge_sq=e4_sq,
            face_circumradius_sq=rf4_sq,
            insphere_radius_sq=rin4_sq,
            surface_area=surf4,
            volume=vol4,
        ),
        "cube": PolyhedronMetrics(
            name="Cube",
            latin_name="Cubus (sex basium quadratarum)",
            faces=6,
            vertices=8,
            edges=12,
            sphere_diameter=d,
            edge=e6,
            edge_sq=e6_sq,
            face_circumradius_sq=rf6_sq,
            insphere_radius_sq=rin6_sq,
            surface_area=surf6,
            volume=vol6,
        ),
        "octahedron": PolyhedronMetrics(
            name="Octahedron",
            latin_name="Octaedron (solidum octo basium)",
            faces=8,
            vertices=6,
            edges=12,
            sphere_diameter=d,
            edge=e8,
            edge_sq=e8_sq,
            face_circumradius_sq=rf8_sq,
            insphere_radius_sq=rin8_sq,
            surface_area=surf8,
            volume=vol8,
        ),
        "dodecahedron": PolyhedronMetrics(
            name="Dodecahedron",
            latin_name="Duodecaedron (duodecim basium pentagonarum)",
            faces=12,
            vertices=20,
            edges=30,
            sphere_diameter=d,
            edge=e12,
            edge_sq=e12_sq,
            face_circumradius_sq=rf12_sq,
            insphere_radius_sq=rin12_sq,
            surface_area=surf12,
            volume=vol12,
        ),
        "icosahedron": PolyhedronMetrics(
            name="Icosahedron",
            latin_name="Ycosaedron (viginti basium triangularium)",
            faces=20,
            vertices=12,
            edges=30,
            sphere_diameter=d,
            edge=e20,
            edge_sq=e20_sq,
            face_circumradius_sq=rf20_sq,
            insphere_radius_sq=rin20_sq,
            surface_area=surf20,
            volume=vol20,
        ),
    }


def verify_hypsicles_xiv_ratio(diameter: int | sp.Expr = 6) -> sp.Expr:
    """Verify Hypsicles' Book XIV theorem (*Distinctio VI*, pp. 200–202): $V_{12}/V_{20} = S_{12}/S_{20} = e_6/e_{20}$.

    Returns the shared exact closed-form ratio $\\sqrt{\\frac{5 + \\sqrt{5}}{6}}$.
    """
    solids = polyhedra_in_sphere(diameter)
    c6 = solids["cube"]
    d12 = solids["dodecahedron"]
    i20 = solids["icosahedron"]

    if not zero_test(d12.face_circumradius_sq - i20.face_circumradius_sq):
        raise AssertionError("Hypsicles XIV.2 failed: dodecahedron & icosahedron face circumradii differ.")
    if not zero_test(d12.insphere_radius_sq - i20.insphere_radius_sq):
        raise AssertionError("Insphere radii of dodecahedron & icosahedron differ.")

    vol_ratio = sp.simplify(d12.volume / i20.volume)
    surf_ratio = sp.simplify(d12.surface_area / i20.surface_area)
    edge_ratio = sp.simplify(c6.edge / i20.edge)
    closed_form = sp.sqrt((5 + sp.sqrt(5)) / 6)

    if not zero_test(vol_ratio - surf_ratio):
        raise AssertionError("V12/V20 != S12/S20")
    if not zero_test(vol_ratio**2 - edge_ratio**2):
        raise AssertionError("(V12/V20)^2 != (e6/e20)^2")
    if not zero_test(edge_ratio**2 - closed_form**2):
        raise AssertionError("(e6/e20)^2 != (5 + sqrt(5))/6")
    return closed_form


@dataclass(frozen=True)
class SpherePolyhedraSectionResult:
    """Exact Euclid XIII.18 / *Distinctio VI* construction of all 5 polyhedron edges in diameter $AI = 6$."""

    model: Model
    pt_a: spg.Point
    pt_i: spg.Point
    pt_o: spg.Point
    pt_k: spg.Point
    pt_b: spg.Point
    pt_c: spg.Point
    pt_m: spg.Point
    pt_n: spg.Point
    quadrances: dict[str, sp.Expr]


def construct_sphere_polyhedra_section() -> SpherePolyhedraSectionResult:
    """Construct all five regular polyhedron edges inside sphere diameter $AI = 6$ (Euclid XIII.18; Dist. VI).

    On great circle ``(O, A)`` with $A = (-3, 0)$, $I = (3, 0)$, $O = (0, 0)$:

    - Trisection point $K = (-1, 0)$ ($AK = 2 = \\frac{1}{3} AI$) and perpendicular $KB$ to circle give
      **Cube edge** $AB$ ($Q = 12$) and **Tetrahedron edge** $BI$ ($Q = 24$).
    - Center perpendicular $OC$ to $C = (0, 3)$ gives **Octahedron edge** $AC$ ($Q = 18$).
    - Golden section $N$ of cube edge $[AB]$ gives **Dodecahedron edge** $AN$ ($Q = 18 - 6\\sqrt{5}$).
    - Tangent $[IP] \\perp [AI]$ of length $AI = 6$ joined to center $O$ cuts the circle at $M$, giving
      **Icosahedron edge** $MI$ ($Q = 18 - \\frac{18}{5}\\sqrt{5}$).
    """
    model = Model("euclid_xiii_sphere_polyhedra", logger=False, auto_intersect=False)

    pt_a = model.set_point(-3, 0, classes=["given"], ID="A")
    pt_i = model.set_point(3, 0, classes=["given"], ID="I")
    ln_ai = model.construct_line(pt_a, pt_i, classes=["carrier"], ID="lnAI")

    # 1. Center O = midpoint(A, I) and great circle of diameter AI = 6
    pt_o = construct_midpoint(model, pt_a, pt_i, pt_id="O", classes=["midpoint"])
    circ = model.construct_circle(pt_o, pt_a, classes=["given", "circle_main"], ID="circAI")

    # 2. Perpendicular at O -> C = (0, 3) => Octahedron edge [AC] (Q = 18)
    with model.subconstruction("I.11_O", hide_guides=True) as sc_o:
        c_o1 = model.construct_circle(pt_a, pt_i, guide=True)
        c_o2 = model.construct_circle(pt_i, pt_a, guide=True)
        v1, v2 = model.intersect_all(c_o1, c_o2, guide=True)
        perp_o = model.construct_line(v1, v2, guide=True)
        pt_c = model.intersect(
            circ,
            perp_o,
            side_of=(pt_a, pt_i, 1),
            classes=["result"],
            ID="C",
            by="XIII.14",
        )
        sc_o.keep(pt_c)

    model.construct_segment(pt_o, pt_c, classes=["guide_ray"], ID="segOC")
    model.construct_segment(pt_a, pt_c, classes=["octahedron_edge"], ID="segAC")

    # 3. Trisect AI at K = (-1, 0) (AK = 2) and erect perpendicular -> B = (-1, 2*sqrt(2))
    pt_k = _divide_segment_in_ratio(model, pt_a, pt_i, 1, 3, pt_id="K", classes=["midpoint"])
    with model.subconstruction("I.11_K", hide_guides=True) as sc_k:
        # Mirror A across K to R1 = (1, 0) for symmetric perpendicular bisector at K
        c_ka = model.construct_circle(pt_k, pt_a, guide=True)
        r1 = model.intersect(ln_ai, c_ka, other_than=pt_a, guide=True)
        c_k1 = model.construct_circle(pt_a, r1, guide=True)
        c_k2 = model.construct_circle(r1, pt_a, guide=True)
        w1, w2 = model.intersect_all(c_k1, c_k2, guide=True)
        perp_k = model.construct_line(w1, w2, guide=True)
        pt_b = model.intersect(
            circ,
            perp_k,
            side_of=(pt_a, pt_i, 1),
            classes=["result"],
            ID="B",
            by="XIII.15",
        )
        sc_k.keep(pt_b)

    model.construct_segment(pt_k, pt_b, classes=["guide_ray"], ID="segKB")
    ln_ab = model.construct_line(pt_a, pt_b, guide=True, ID="lnAB")
    model.construct_segment(pt_a, pt_b, classes=["cube_edge"], ID="segAB")
    model.construct_segment(pt_b, pt_i, classes=["tetrahedron_edge"], ID="segBI")

    # 4. Golden cut N of cube edge [AB] (Euclid II.11 / XIII.17) -> Dodecahedron edge [AN]
    with model.subconstruction("II.11_AB", hide_guides=True) as sc_gold:
        mid_ab = construct_midpoint(model, pt_a, pt_b, guide=True)
        c_bm = model.construct_circle(pt_b, mid_ab, guide=True)
        b_ext = model.intersect(ln_ab, c_bm, other_than=mid_ab, guide=True)
        c_g1 = model.construct_circle(mid_ab, b_ext, guide=True)
        c_g2 = model.construct_circle(b_ext, mid_ab, guide=True)
        g1, g2 = model.intersect_all(c_g1, c_g2, guide=True)
        perp_b = model.construct_line(g1, g2, guide=True)
        pt_q = model.intersect(c_bm, perp_b, side_of=(pt_a, pt_b, 1), guide=True)
        ln_aq = model.construct_line(pt_a, pt_q, guide=True)
        c_qb = model.construct_circle(pt_q, pt_b, guide=True)
        pt_r = model.intersect(ln_aq, c_qb, between=(pt_a, pt_q), guide=True)
        c_ar = model.construct_circle(pt_a, pt_r, guide=True)
        pt_n = model.intersect(
            ln_ab,
            c_ar,
            between=(pt_a, pt_b),
            classes=["result", "golden"],
            ID="N",
            by="XIII.17",
        )
        sc_gold.keep(pt_n)

    model.construct_segment(pt_a, pt_n, classes=["golden", "dodecahedron_edge"], ID="segAN")
    model.set_section([pt_a, pt_n, pt_b], classes=["golden"])

    # 5. Tangent [IP] perpendicular to [AI] at I of length AI = 6 -> ray OP cuts circle at M (Euclid XIII.18)
    with model.subconstruction("XIII.18_Icosa", hide_guides=True) as sc_icosa:
        c_ia = model.construct_circle(pt_i, pt_a, guide=True)
        i_ext = model.intersect(ln_ai, c_ia, other_than=pt_a, guide=True)
        c_p1 = model.construct_circle(pt_a, i_ext, guide=True)
        c_p2 = model.construct_circle(i_ext, pt_a, guide=True)
        z1, z2 = model.intersect_all(c_p1, c_p2, guide=True)
        perp_i = model.construct_line(z1, z2, guide=True)
        # Drop negative side so M lies cleanly in lower semicircle without crowding upper chords B, C!
        pt_p = model.intersect(c_ia, perp_i, side_of=(pt_a, pt_i, -1), guide=True, ID="P")
        ln_op = model.construct_line(pt_o, pt_p, guide=True, ID="lnOP")
        pt_m = model.intersect(
            circ,
            ln_op,
            between=(pt_o, pt_p),
            classes=["result", "icosahedron_pt"],
            ID="M",
            by="XIII.16",
        )
        sc_icosa.keep(pt_m)

    model.construct_segment(pt_o, pt_m, classes=["guide_ray"], ID="segOM")
    model.construct_segment(pt_m, pt_i, classes=["icosahedron_edge"], ID="segMI")

    # 6. Verify all 5 exact quadrances against polyhedra_in_sphere(6)
    q_map = {
        "tetrahedron": sp.simplify(quadrance(pt_b, pt_i)),
        "octahedron": sp.simplify(quadrance(pt_a, pt_c)),
        "cube": sp.simplify(quadrance(pt_a, pt_b)),
        "dodecahedron": sp.simplify(quadrance(pt_a, pt_n)),
        "icosahedron": sp.simplify(quadrance(pt_m, pt_i)),
    }
    expected = polyhedra_in_sphere(6)
    for key, q_val in q_map.items():
        if not zero_test(q_val - expected[key].edge_sq):
            raise AssertionError(f"{key} quadrance mismatch: got {q_val}, expected {expected[key].edge_sq}")

    model.assert_perpendicular(ln_ai, (pt_o, pt_c), by="I.11")
    model.assert_perpendicular(ln_ai, (pt_k, pt_b), by="I.11")
    model.conclude(
        pt_a,
        pt_i,
        pt_b,
        pt_c,
        pt_n,
        pt_m,
        by="XIII.18",
        label="BI^2=24, AC^2=18, AB^2=12, MI^2=18-18*sqrt(5)/5, AN^2=18-6*sqrt(5)",
    )

    return SpherePolyhedraSectionResult(
        model=model,
        pt_a=pt_a,
        pt_i=pt_i,
        pt_o=pt_o,
        pt_k=pt_k,
        pt_b=pt_b,
        pt_c=pt_c,
        pt_m=pt_m,
        pt_n=pt_n,
        quadrances=q_map,
    )


@dataclass(frozen=True)
class GoldenChordResult:
    """Exact model & invariants for Fibonacci's extreme-and-mean-ratio division (*Distinctio VI*, pp. 196–197)."""

    model: Model
    pt_b: spg.Point
    pt_e: spg.Point
    pt_m: spg.Point
    pt_c: spg.Point
    pt_d: spg.Point
    pt_g: spg.Point
    pt_a: spg.Point
    chord_length: sp.Expr
    golden_major: sp.Expr
    golden_minor: sp.Expr


def construct_dodecahedron_golden_chord() -> GoldenChordResult:
    """Construct *Modus diuidendi lineam media et extrema proportione* on chord $BE = 2\\sqrt{3}$ (pp. 196–197).

    Follows Boncompagni pp. 196–197 step-for-step:

    1. Pentagon diagonal / cube edge $BE = \\sqrt{12} = 2\\sqrt{3}$ from $B=(0,0)$ to $E=(2\\sqrt{3}, 0)$.
    2. Midpoint $M = (\\sqrt{3}, 0)$ and perpendicular $[EC] \\perp [BE]$ with $EC = EM = \\sqrt{3}$.
    3. Hypotenuse $[BC]$ has $BC^2 = BE^2 + EC^2 = 12 + 3 = 15$ ($BC = \\sqrt{15}$).
    4. Circle $(C, E)$ cuts $[BC]$ at $D$, leaving $BD = \\sqrt{15} - \\sqrt{3}$; circle $(B, D)$ transfers
       $BD$ onto $[BE]$ at golden cut $G = (\\sqrt{15} - \\sqrt{3}, 0)$ and meets circle $(E, G)$ at apex $A$
       of the dodecahedron's pentagonal cap $\\triangle ABE$ ($AB = AE = BG = \\sqrt{15} - \\sqrt{3}$).
    """
    model = Model("dodecahedron_golden_chord", logger=False, auto_intersect=False)

    s3 = sp.sqrt(3)
    pt_b = model.set_point(0, 0, classes=["given"], ID="B")
    pt_e = model.set_point(2 * s3, 0, classes=["given"], ID="E")
    ln_be = model.construct_line(pt_b, pt_e, classes=["carrier"], ID="lnBE")

    pt_m = construct_midpoint(model, pt_b, pt_e, pt_id="M", classes=["midpoint"])

    # Erect perpendicular at E of length EM = sqrt(3) -> C = (2*sqrt(3), sqrt(3))
    c_em = model.construct_circle(pt_e, pt_m, classes=["semicircle_guide"], ID="circCE")
    with model.subconstruction("I.11_E", hide_guides=True) as sc_perp:
        e_ext = model.intersect(ln_be, c_em, other_than=pt_m, guide=True)
        c_1 = model.construct_circle(pt_m, e_ext, guide=True)
        c_2 = model.construct_circle(e_ext, pt_m, guide=True)
        p1, p2 = model.intersect_all(c_1, c_2, guide=True)
        perp_e = model.construct_line(p1, p2, guide=True)
        pt_c = model.intersect(
            c_em,
            perp_e,
            side_of=(pt_b, pt_e, 1),
            classes=["result"],
            ID="C",
            by="I.11",
        )
        sc_perp.keep(pt_c)

    model.construct_segment(pt_e, pt_c, classes=["bisector"], ID="segEC")
    ln_bc = model.construct_line(pt_b, pt_c, classes=["guide_ray"], ID="lnBC")

    # Circle (C, E) has radius EC = sqrt(3); cut [BC] at D
    c_ce = model.construct_circle(pt_c, pt_e, classes=["semicircle_guide"], ID="circCD")
    pt_d = model.intersect(
        ln_bc,
        c_ce,
        between=(pt_b, pt_c),
        classes=["result"],
        ID="D",
        by="II.11",
    )

    # Circle (B, D) transfers BD = sqrt(15) - sqrt(3) onto [BE] at G
    c_bd = model.construct_circle(pt_b, pt_d, classes=["transfer_arc"], ID="circBD")
    pt_g = model.intersect(
        ln_be,
        c_bd,
        between=(pt_b, pt_e),
        classes=["result", "golden"],
        ID="G",
        by="VI.30",
    )

    # Construct pentagonal face apex A above [BE] where AB = AE = BG = e_12
    with model.subconstruction("XIII.8_Apex", hide_guides=True) as sc_apex:
        # Mirror G across midpoint M to get radius EG = BG around E: circle (E, A_seed) via compass transfer
        # Since BG = sqrt(15) - sqrt(3), shift along ln_be from E toward B by BG:
        # Specifically, circle (M, G) reflects G across M to G' on [BE] with E-G' = B-G!
        c_mg = model.construct_circle(pt_m, pt_g, guide=True)
        g_mirror = model.intersect(ln_be, c_mg, other_than=pt_g, guide=True)
        c_eg = model.construct_circle(pt_e, g_mirror, guide=True)
        pt_a = model.intersect(
            c_bd,
            c_eg,
            side_of=(pt_b, pt_e, 1),
            classes=["result", "golden"],
            ID="A",
            by="I.22",
        )
        sc_apex.keep(pt_a)

    model.construct_polygon([pt_a, pt_b, pt_e], classes=["share_p"], ID="triABE")
    model.construct_segment(pt_a, pt_b, classes=["golden"], ID="segAB")
    model.construct_segment(pt_a, pt_e, classes=["golden"], ID="segAE")
    model.construct_segment(pt_b, pt_g, classes=["golden"], ID="segBG")
    model.set_section([pt_b, pt_g, pt_e], classes=["golden"])

    be_len = sp.simplify(sp.sqrt(quadrance(pt_b, pt_e)))
    bg_len = sp.simplify(sp.sqrt(quadrance(pt_b, pt_g)))
    ge_len = sp.simplify(sp.sqrt(quadrance(pt_g, pt_e)))

    if not zero_test(be_len * ge_len - bg_len**2):
        raise AssertionError("Extreme and mean ratio BE * GE == BG^2 failed.")
    if not zero_test(bg_len - (sp.sqrt(15) - s3)):
        raise AssertionError(f"Expected BG = sqrt(15) - sqrt(3), got {bg_len}")

    model.assert_perpendicular(ln_be, (pt_e, pt_c), by="I.11")
    model.assert_equal((pt_b, pt_d), (pt_b, pt_g), by="I.3")
    model.assert_equal((pt_a, pt_b), (pt_b, pt_g), by="I.3")
    model.assert_equal((pt_a, pt_e), (pt_b, pt_g), by="I.3")
    model.conclude(
        pt_b,
        pt_g,
        pt_e,
        pt_c,
        pt_d,
        pt_a,
        by="PG.VI.Golden",
        label="BE : BG = BG : GE = phi, with BG = sqrt(15) - sqrt(3)",
    )

    return GoldenChordResult(
        model=model,
        pt_b=pt_b,
        pt_e=pt_e,
        pt_m=pt_m,
        pt_c=pt_c,
        pt_d=pt_d,
        pt_g=pt_g,
        pt_a=pt_a,
        chord_length=be_len,
        golden_major=bg_len,
        golden_minor=ge_len,
    )


@dataclass(frozen=True)
class PentagonDecagonResult:
    """Exact model & invariants for Fibonacci's pentagon & decagon in diameter $10$ (*Distinctio VIII*)."""

    model: Model
    center_i: spg.Point
    apex_d: spg.Point
    midpoint_h: spg.Point
    golden_pt_k: spg.Point
    pentagon_vertices: tuple[spg.Point, ...]
    decagon_vertex: spg.Point
    radius: sp.Expr
    decagon_side: sp.Expr
    decagon_side_sq: sp.Expr
    pentagon_side: sp.Expr
    pentagon_side_sq: sp.Expr


def construct_pentagon_decagon_in_circle() -> PentagonDecagonResult:
    """Inscribe the regular pentagon & decagon in a circle of diameter $10$ (*Distinctio VIII*, pp. 207–208).

    Follows Fibonacci's Euclidean demonstration on p. 208 (Euclid XIII.9–10):

    - Circle center $I = (0, 0)$, horizontal diameter $C=(-5,0)$ to $A=(5,0)$, apex $D=(0,5)$ ($R = 5$).
    - Midpoint $H = (\\frac{5}{2}, 0)$ of $[IA]$, segment $[HD]$ of length $\\sqrt{31\\frac{1}{4}} = \\frac{5\\sqrt{5}}{2}$.
    - Circle $(H, D)$ cuts $[CA]$ at $K = (\\frac{5 - 5\\sqrt{5}}{2}, 0)$:

      * $IK = \\frac{5\\sqrt{5} - 5}{2} = \\sqrt{31\\frac{1}{4}} - 2\\frac{1}{2} = s_{10}$ (regular decagon side).
      * $DK = \\sqrt{ID^2 + IK^2} = \\sqrt{62\\frac{1}{2} - \\sqrt{781\\frac{1}{4}}} = s_5$ (regular pentagon side).
    """
    model = Model("pentagon_decagon_circle", logger=False, auto_intersect=False)

    pt_i = model.set_point(0, 0, classes=["given"], ID="I")
    pt_a = model.set_point(5, 0, classes=["given"], ID="A")
    pt_c = model.set_point(-5, 0, classes=["given"], ID="C")
    pt_d = model.set_point(0, 5, classes=["given"], ID="D")

    circ = model.construct_circle(pt_i, pt_a, classes=["given", "circle_main"], ID="circDAC")
    ln_ca = model.construct_line(pt_c, pt_a, classes=["carrier"], ID="lnCA")
    model.construct_segment(pt_i, pt_d, classes=["bisector"], ID="segID")

    # Midpoint H of radius [IA] and arc (H, D) -> golden point K on [IC]
    pt_h = construct_midpoint(model, pt_i, pt_a, pt_id="H", classes=["midpoint"])
    model.construct_segment(pt_h, pt_d, classes=["guide_ray"], ID="segHD")
    c_hd = model.construct_circle(pt_h, pt_d, classes=["transfer_arc"], ID="circHD")
    pt_k = model.intersect(
        ln_ca,
        c_hd,
        between=(pt_c, pt_i),
        classes=["result", "golden"],
        ID="K",
        by="XIII.9",
    )

    # Decagon side [IK] and Pentagon hypotenuse [DK] (Euclid XIII.10: DK^2 = ID^2 + IK^2)
    model.construct_segment(pt_i, pt_k, classes=["golden"], ID="segIK")
    model.construct_segment(pt_d, pt_k, classes=["golden"], ID="segDK")

    # Step pentagon chord s_5 = DK around circle (I, A) starting at D = (0, 5)
    c_dk = model.construct_circle(pt_d, pt_k, guide=True)
    p1 = model.intersect(circ, c_dk, side_of=(pt_i, pt_d, -1), classes=["result"], ID="P1", by="IV.11")
    p4 = model.intersect(circ, c_dk, side_of=(pt_i, pt_d, 1), classes=["result"], ID="P4", by="IV.11")

    with model.subconstruction("IV.11_Lower", hide_guides=True) as sc_low:
        # Circle centered at P1 through D has radius s_5 and meets circ again at P2
        c_p1 = model.construct_circle(p1, pt_d, guide=True)
        p2 = model.intersect(circ, c_p1, other_than=pt_d, classes=["result"], ID="P2", by="IV.11")
        c_p4 = model.construct_circle(p4, pt_d, guide=True)
        p3 = model.intersect(circ, c_p4, other_than=pt_d, classes=["result"], ID="P3", by="IV.11")
        # Also mark decagon vertex Q1 between D and P1 as midpoint of arc DP1 via angle bisector
        c_d0 = model.construct_circle(pt_d, p1, guide=True)
        m_arc = model.intersect(c_d0, c_p1, side_of=(pt_d, p1, 1), guide=True)
        ln_iq = model.construct_line(pt_i, m_arc, guide=True)
        q1 = model.intersect(circ, ln_iq, on_ray=(pt_i, m_arc), classes=["result", "golden"], ID="Q1", by="III.30")
        sc_low.keep([p2, p3, q1])

    model.construct_polygon([pt_d, p1, p2, p3, p4], classes=["share_p"], ID="pentagon")
    model.construct_segment(pt_d, q1, classes=["golden"], ID="segDQ1")
    model.construct_segment(q1, p1, classes=["golden"], ID="segQ1P1")

    s10_sq = sp.simplify(quadrance(pt_i, pt_k))
    s10 = sp.simplify(sp.sqrt(s10_sq))
    s5_sq = sp.simplify(quadrance(pt_d, pt_k))
    s5 = sp.simplify(sp.sqrt(s5_sq))
    r_sq = sp.simplify(quadrance(pt_i, pt_d))

    # Euclid XIII.10: pentagon_side^2 == hexagon_side^2 + decagon_side^2
    if not zero_test(s5_sq - (r_sq + s10_sq)):
        raise AssertionError("Euclid XIII.10 identity s_5^2 = R^2 + s_10^2 failed.")
    if not zero_test(quadrance(pt_d, q1) - s10_sq):
        raise AssertionError("Inscribed decagon chord DQ1 != IK.")
    if not zero_test(quadrance(p2, p3) - s5_sq):
        raise AssertionError("Regular pentagon closure chord P2P3 != s_5.")

    model.assert_perpendicular(ln_ca, (pt_i, pt_d), by="I.11")
    model.assert_equal((pt_i, pt_k), (pt_d, q1), by="XIII.9")
    model.assert_equal((pt_d, pt_k), (pt_d, p1), by="XIII.10")
    model.conclude(
        pt_i,
        pt_d,
        pt_h,
        pt_k,
        p1,
        p2,
        p3,
        p4,
        q1,
        by="PG.VIII.Pentagon",
        label="s_10 = sqrt(125/4) - 5/2, s_5^2 = 25 + s_10^2 = 125/2 - 25*sqrt(5)/2",
    )

    return PentagonDecagonResult(
        model=model,
        center_i=pt_i,
        apex_d=pt_d,
        midpoint_h=pt_h,
        golden_pt_k=pt_k,
        pentagon_vertices=(pt_d, p1, p2, p3, p4),
        decagon_vertex=q1,
        radius=sp.Integer(5),
        decagon_side=s10,
        decagon_side_sq=s10_sq,
        pentagon_side=s5,
        pentagon_side_sq=s5_sq,
    )


def solve_pentagon_ptolemy_quartic(diameter: int | sp.Expr = 10) -> tuple[sp.Expr, sp.Expr]:
    """Solve Fibonacci's *Distinctio VIII* algebraic biquadratic (`census census`) for pentagon side & diagonal.

    In *Distinctio VIII* (Boncompagni pp. 207–208), setting diameter $d = 10$ and unknown chord
    $x$ (*res*, $x^2 =$ *census*, $x^4 =$ *census census*), Ptolemy's theorem on the cyclic pentagon
    yields $x^4 + \\frac{5}{16} d^4 = \\frac{5}{4} d^2 x^2$ (for $d = 10$: $x^4 + 3125 = 125 x^2$).
    Returns ``(pentagon_side, pentagon_diagonal)`` as exact nested radicals.
    """
    d = sp.sympify(diameter)
    u = sp.Symbol("u", positive=True)  # u = census = x^2
    poly_eq = sp.Eq(u**2 + sp.Rational(5, 16) * d**4, sp.Rational(5, 4) * d**2 * u)
    roots = sorted(sp.solve(poly_eq, u), key=lambda expr: float(expr.evalf()))
    side = sp.simplify(sp.sqrt(roots[0]))
    diag = sp.simplify(sp.sqrt(roots[1]))
    if not zero_test(diag / side - PHI):
        raise AssertionError("Pentagon diagonal / side != phi.")
    return side, diag


def construct_quadrans_surveying() -> Model:
    """Construct Fibonacci's optical *Quadrans* (`dhai`, 12-part shadow square) from *Distinctio VII* (p. 204).

    Models the surveyor's quadrant square $DHAI$ of side $12$ (*puncta*), graduated quarter-circle arc
    centered at sighting pinnule $D = (0, 12)$ through $H = (12, 12)$ and $I = (0, 0)$, *umbra recta*
    division on $[IA]$, *umbra versa* division on $[AH]$, and plumb line $[DP]$ cutting $[IA]$ at $8$
    *puncta* (giving tower height : horizontal distance $= 12 : 8 = 3 : 2$).
    """
    model = Model("quadrans_surveying", logger=False, auto_intersect=False)

    pt_i = model.set_point(0, 0, classes=["given"], ID="I")
    pt_a = model.set_point(12, 0, classes=["given"], ID="A")
    pt_h = model.set_point(12, 12, classes=["given"], ID="H")
    pt_d = model.set_point(0, 12, classes=["given"], ID="D")

    model.construct_polygon([pt_d, pt_h, pt_a, pt_i], classes=["given", "pertica_sq"], ID="sqDHAI")
    model.construct_line(pt_i, pt_a, classes=["carrier"], ID="lnIA")
    model.construct_line(pt_a, pt_h, classes=["carrier"], ID="lnAH")

    # Quarter-circle arc circle centered at D = (0, 12) through H = (12, 12) and I = (0, 0)
    circ_q = model.construct_circle(pt_d, pt_h, classes=["semicircle_guide"], ID="circQuad")

    # Diagonal [DA] (45-degree boundary between umbra recta and umbra versa)
    ln_da = model.construct_line(pt_d, pt_a, classes=["bisector"], ID="lnDA")
    pt_b = model.intersect(circ_q, ln_da, between=(pt_d, pt_a), classes=["midpoint"], ID="B", by="I.47")

    # Plumb-bob line cutting umbra recta [IA] at P = (8, 0) (2/3 of 12 puncta) and arc at C
    pt_p = _divide_segment_in_ratio(model, pt_i, pt_a, 2, 3, pt_id="P", classes=["result", "golden"])
    ln_dp = model.construct_line(pt_d, pt_p, classes=["guide_ray"], ID="lnDP")
    pt_c = model.intersect(circ_q, ln_dp, between=(pt_d, pt_p), classes=["result"], ID="C", by="PG.VII.Quad")
    model.construct_segment(pt_d, pt_p, classes=["golden"], ID="segDP")

    # Tick marks every 3 puncta along umbra recta [IA] and umbra versa [AH]
    for tick in (3, 6, 9):
        u_bot = model.set_point(tick, 0, guide=True, ID=f"U{tick}")
        u_top = model.set_point(tick, 12, guide=True, ID=f"UT{tick}")
        v_left = model.set_point(0, tick, guide=True, ID=f"VL{tick}")
        v_right = model.set_point(12, tick, guide=True, ID=f"VR{tick}")
        model.construct_segment(u_bot, u_top, classes=["grid"])
        model.construct_segment(v_left, v_right, classes=["grid"])

    model.assert_equal((pt_d, pt_h), (pt_d, pt_i), by="I.def.22")
    model.assert_collinear(pt_i, pt_p, pt_a, by="VI.9")
    model.conclude(
        pt_d,
        pt_h,
        pt_a,
        pt_i,
        pt_b,
        pt_c,
        pt_p,
        by="PG.VII.Quadrans",
        label="DI : IP = 12 : 8 = Tower Height : Horizontal Shadow",
    )
    return model


@dataclass(frozen=True)
class RabbitConvergentRow:
    """Single month entry from Fibonacci's *Liber Abaci* Ch. 12 rabbit recurrence ($1202/1228$)."""

    month: int
    fibonacci_index: int
    pairs: sp.Integer
    prev_pairs: sp.Integer
    ratio_to_prev: sp.Rational
    cassini_determinant: sp.Integer
    phi_error_abs: sp.Expr


def fibonacci_number_exact(n: int) -> sp.Integer:
    """Return exact $F_n$ with $F_0 = 0, F_1 = 1, F_2 = 1$."""
    if n < 0:
        raise ValueError("Fibonacci index n must be non-negative.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return sp.Integer(a)


def fibonacci_rabbit_convergents(months: int = 12) -> list[RabbitConvergentRow]:
    """Build Fibonacci's *Liber Abaci* Ch. 12 rabbit table (Boncompagni Vol. I, pp. 283–284).

    Starting with $1$ fertile pair (`paria 1` = $F_2 = 1$) at month $0$, month $m \\in \\{1, \\dots, 12\\}$
    has $F_{m+2}$ pairs: ``2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377``.
    """
    if months < 1:
        raise ValueError("months must be >= 1")

    rows: list[RabbitConvergentRow] = []
    for m in range(1, months + 1):
        idx = m + 2
        fn = fibonacci_number_exact(idx)
        fn_prev = fibonacci_number_exact(idx - 1)
        fn_next = fibonacci_number_exact(idx + 1)
        ratio = sp.Rational(fn, fn_prev)
        # Cassini determinant around F_{idx-1}: F_{idx} * F_{idx-2} - F_{idx-1}^2
        fn_prev2 = fibonacci_number_exact(idx - 2)
        cassini = sp.Integer(fn * fn_prev2 - fn_prev**2)
        err = sp.Abs(ratio - PHI)
        rows.append(
            RabbitConvergentRow(
                month=m,
                fibonacci_index=idx,
                pairs=fn,
                prev_pairs=fn_prev,
                ratio_to_prev=ratio,
                cassini_determinant=cassini,
                phi_error_abs=err,
            )
        )
        _ = fn_next
    return rows


def verify_cassini_identity(max_n: int = 15) -> bool:
    """Verify exact Binet closed form and Cassini identity $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$."""
    s5 = sp.sqrt(5)
    for n in range(1, max_n + 1):
        fn = fibonacci_number_exact(n)
        fn_minus = fibonacci_number_exact(n - 1)
        fn_plus = fibonacci_number_exact(n + 1)
        if fn_minus * fn_plus - fn**2 != (-1) ** n:
            raise AssertionError(f"Cassini identity failed at n={n}")
        binet = sp.simplify((PHI**n - PSI**n) / s5)
        if binet != fn:
            raise AssertionError(f"Binet formula mismatch at n={n}: {binet} != {fn}")
    return True


@dataclass(frozen=True)
class FlosCubicResult:
    """Exact rational & algebraic analysis of Fibonacci's *Flos* (1225) cubic $x^3 + 2x^2 + 10x = 20$."""

    sexagesimal_digits: tuple[int, ...]
    rational_root: sp.Rational
    polynomial_value_at_rational: sp.Rational
    residual_from_20: sp.Rational
    exact_cardano_root: sp.Expr
    abs_root_error: sp.Expr


def flos_sexagesimal_cubic() -> FlosCubicResult:
    """Evaluate Fibonacci's 1225 *Flos* sexagesimal root $1; 22, 7, 42, 33, 4, 40$ (Boncompagni Vol. II, p. 234).

    In *Flos*, Leonardo Pisano proves against Euclid Book X that no rational or quadratic-irrational
    line satisfies $x^3 + 2x^2 + 10x = 20$, and gives its root to six sexagesimal places:
    $1 + \\frac{22}{60} + \\frac{7}{60^2} + \\frac{42}{60^3} + \\frac{33}{60^4} + \\frac{4}{60^5} + \\frac{40}{60^6} = \\frac{1596577777}{1166400000}$.
    """
    digits = (1, 22, 7, 42, 33, 4, 40)
    x_fib = sum(
        (sp.Rational(d, 60**k) for k, d in enumerate(digits)),
        start=sp.Rational(0, 1),
    )
    poly_val = x_fib**3 + 2 * x_fib**2 + 10 * x_fib
    residual = poly_val - 20

    # Exact depressed-cubic Cardano radical root for x^3 + 2x^2 + 10x - 20 = 0:
    # Substitute x = y - 2/3 => y^3 + (26/3)y - (704/27) = 0
    # -q/2 = 352/27, p/3 = 26/9 => discriminant D = (352/27)^2 + (26/9)^3 = 141480/729 = (2*sqrt(3930)/9)^2
    disc_sqrt = sp.Rational(2, 9) * sp.sqrt(3930)
    u_rad = (sp.Rational(352, 27) + disc_sqrt) ** sp.Rational(1, 3)
    w_rad = (disc_sqrt - sp.Rational(352, 27)) ** sp.Rational(1, 3)
    x_exact = u_rad - w_rad - sp.Rational(2, 3)

    if abs(float((x_exact**3 + 2 * x_exact**2 + 10 * x_exact - 20).evalf(50))) > 1e-40:
        raise AssertionError("Cardano radical root failed 50-digit check.")

    return FlosCubicResult(
        sexagesimal_digits=digits,
        rational_root=x_fib,
        polynomial_value_at_rational=poly_val,
        residual_from_20=residual,
        exact_cardano_root=x_exact,
        abs_root_error=sp.Abs(x_fib - x_exact),
    )


def flos_congruum_squares() -> tuple[sp.Rational, sp.Rational, sp.Rational]:
    """Return John of Palermo's *Flos* / *Liber Quadratorum* rational square triple for $x^2 \\pm 5 = \\square$.

    On Boncompagni Vol. II p. 227, Fibonacci solves $x^2 - 5 = a^2$ and $x^2 + 5 = b^2$ via the
    *congruum* $720 = 5 \\times 12^2$ (from $(31^2, 41^2, 49^2)$ in arithmetic progression with step $720$),
    yielding $(a, x, b) = (\\frac{31}{12}, \\frac{41}{12}, \\frac{49}{12})$.
    """
    a = sp.Rational(31, 12)
    x = sp.Rational(41, 12)
    b = sp.Rational(49, 12)
    if x**2 - 5 != a**2 or x**2 + 5 != b**2:
        raise AssertionError("Congruum triple failed x^2 +/- 5 == square.")
    return (a, x, b)
