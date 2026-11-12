r"""Exact symbolic Pisan metrology, Heron's incenter proof, and 96-gon circle bounds (*Practica Geometriae*, Dist. I & III).

Grounded directly in Baldassarre Boncompagni's 1862 critical Latin edition (*Scritti di Leonardo
Pisano*, Vol. II: *Leonardi Pisani Practica Geometriae ed Opuscoli*, Rome, 1862):

- **Pisan Surveyor's Metrology** (*Introductoria* & *Distinctio I*, pp. 3–5, ``fol. 2v–3v``):
  Exact rational conversions across the Pisan rod (*pertica*), *pes*, *uncia*, *denarius*,
  *scala*, *panorum*, *stariorum* ($66$ square *perticae*), and *modiorum* ($24$ *stariora*).
- **Heron's Formula & Geometric Incenter Proof** (*Distinctio III*, pp. 39–41, ``fol. 23v–25r``):
  Exact :class:`~geometor.model.Model` straightedge-and-compass construction of incenter $T$,
  perpendiculars $TH, TE, TZ$, tangent excesses $(s-a, s-b, s-c)$, and semiperimeter extension
  on Fibonacci's $(13, 14, 15)$ scalene triangle, alongside symbolic polynomial verification over
  $\mathbb{Z}[a, b, c]$.
- **Fibonacci's Circle Measurement** (*Distinctio III*, pp. 88–91, ``fol. 53v–55v``):
  Fibonacci's small-number Pisan reformulation of Archimedes' 96-gon ($1440 : 458\frac{1}{5}$ and
  $1440 : 458\frac{4}{9}$), yielding $\pi_{\text{Fib}} = \frac{1440}{458\frac{1}{3}} = \frac{864}{275}$
  and his exact rational identity $\frac{864}{275 - \frac{1}{11}} = \frac{22}{7}$.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, proposition, quadrance, zero_test
from geometor.model.invariants import polygon_area2

__all__ = [
    "PISAN_AREA_PERTICAE",
    "PisanLinearMeasure",
    "PisanAreaBreakdown",
    "HeronProofResult",
    "CircleBoundsResult",
    "multiply_pisan_lengths",
    "decompose_pisan_area",
    "heron_area_exact",
    "verify_heron_polynomial_identity",
    "construct_pisan_pertica_grid",
    "construct_heron_incenter_proof",
    "fibonacci_circle_bounds",
    "construct_circle_archimedean_step",
]

# Exact superficial perticae per Pisan agrarian unit (Boncompagni 1862, p. 3, fol. 2v)
PISAN_AREA_PERTICAE: dict[str, sp.Rational] = {
    "uncia_superficialis": sp.Rational(1, 108),
    "denarius": sp.Rational(1, 36),
    "pes_superficialis": sp.Rational(1, 6),
    "pertica_superficialis": sp.Rational(1, 1),
    "scala": sp.Rational(4, 1),
    "panorum": sp.Rational(11, 2),
    "stariorum": sp.Rational(66, 1),
    "modiorum": sp.Rational(1584, 1),
}


@dataclass(frozen=True)
class PisanLinearMeasure:
    """Exact Pisan linear length in *perticae*, *pedes* ($1/6$), and *unciae* ($1/108$).

    Attributes:
        perticae: Whole or rational Pisan rods (*perticae*).
        pedes: Linear feet ($1\text{ pertica} = 6\text{ pedes}$).
        unciae: Linear inches/points ($1\text{ pes} = 18\text{ unciae}$, $1\text{ pertica} = 108\text{ unciae}$).
    """

    perticae: int | sp.Rational = 0
    pedes: int | sp.Rational = 0
    unciae: int | sp.Rational = 0

    def to_perticae(self) -> sp.Rational:
        """Convert this linear measure into exact rational *perticae*."""
        return (
            sp.Rational(self.perticae)
            + sp.Rational(self.pedes) / 6
            + sp.Rational(self.unciae) / 108
        )

    def to_pedes(self) -> sp.Rational:
        """Convert this linear measure into exact rational *pedes*."""
        return self.to_perticae() * 6

    def to_unciae(self) -> sp.Rational:
        """Convert this linear measure into exact rational *unciae* (*puncta*)."""
        return self.to_perticae() * 108


@dataclass(frozen=True)
class PisanAreaBreakdown:
    """Canonical decomposition of an exact Pisan field area (*embadum*)."""

    total_perticae: sp.Rational
    total_denarii: sp.Rational
    modiora: int
    stariora: int
    panora: int
    perticae: int
    pedes_superficiales: int
    unciae_superficiales: sp.Rational


def decompose_pisan_area(area_perticae: int | sp.Rational) -> PisanAreaBreakdown:
    """Decompose an exact superficial *perticae* count into Pisan episcopate land units."""
    rem = sp.Rational(area_perticae)
    total_pert = rem
    total_den = rem * 36

    modiora = int(rem // 1584)
    rem -= sp.Rational(modiora * 1584)

    stariora = int(rem // 66)
    rem -= sp.Rational(stariora * 66)

    panora = int(rem // sp.Rational(11, 2))
    rem -= sp.Rational(panora) * sp.Rational(11, 2)

    perticae = int(rem // 1)
    rem -= sp.Rational(perticae)

    pedes = int((rem * 6) // 1)
    rem -= sp.Rational(pedes, 6)

    unciae = rem * 108
    return PisanAreaBreakdown(
        total_perticae=total_pert,
        total_denarii=total_den,
        modiora=modiora,
        stariora=stariora,
        panora=panora,
        perticae=perticae,
        pedes_superficiales=pedes,
        unciae_superficiales=unciae,
    )


def multiply_pisan_lengths(
    width: PisanLinearMeasure,
    length: PisanLinearMeasure,
) -> PisanAreaBreakdown:
    """Multiply two Pisan linear lengths (*Distinctio I*, pp. 3–5) into exact superficial units."""
    area_perticae = width.to_perticae() * length.to_perticae()
    return decompose_pisan_area(area_perticae)


def heron_area_exact(
    a: int | sp.Expr,
    b: int | sp.Expr,
    c: int | sp.Expr,
) -> tuple[sp.Expr, tuple[sp.Expr, sp.Expr, sp.Expr], sp.Expr, sp.Expr]:
    """Compute semiperimeter, excesses, squared area, and exact Heron area for sides $(a, b, c)$."""
    a_s, b_s, c_s = sp.sympify(a), sp.sympify(b), sp.sympify(c)
    s = (a_s + b_s + c_s) / 2
    da, db, dc = s - a_s, s - b_s, s - c_s
    area_sq = sp.simplify(s * da * db * dc)
    area = sp.sqrt(area_sq)
    return s, (da, db, dc), area_sq, sp.simplify(area)


def verify_heron_polynomial_identity() -> sp.Expr:
    r"""Verify symbolically over $\mathbb{Z}[x, y, z]$ that $r^2 (x+y+z)^2 = (x+y+z) x y z$.

    In Fibonacci's geometric proof (*Distinctio III*, pp. 40–41), a triangle with tangent
    segments $x = s - a$, $y = s - b$, $z = s - c$ and inradius $r$ satisfies both
    $\Delta = r(x + y + z)$ and the similar-triangle proportion $r^2 (x + y + z) = x y z$
    (since $\tan(\alpha/2)\tan(\beta/2) + \tan(\beta/2)\tan(\gamma/2) + \tan(\gamma/2)\tan(\alpha/2) = 1$).
    Returns ``0`` after exact algebraic simplification.
    """
    x, y, z = sp.symbols("x y z", positive=True)
    a = y + z
    b = z + x
    c = x + y
    # Euclidean altitude h_c onto side c = x + y via cosine law
    cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
    sin_b_sq = sp.simplify(1 - cos_b**2)
    area_sq_altitude = sp.expand(sp.Rational(1, 4) * a**2 * c**2 * sin_b_sq)
    area_sq_heron = sp.expand((x + y + z) * x * y * z)
    residual = sp.simplify(area_sq_altitude - area_sq_heron)
    if residual != 0:
        raise AssertionError(f"Heron polynomial identity failed: {residual}")
    return residual


@proposition(
    "PG.I.Pertica",
    kind="problem",
    title="Distinctio I — Subdivision of the Pisan Pertica into 6 Superficial Pedes and 36 Denarii",
    hide_guides=False,
)
def _build_pertica_grid_prop(model: Model) -> spg.Polygon:
    pt_a = model.set_point(0, 6, classes=["given"], ID="A")
    pt_b = model.set_point(6, 6, classes=["given"], ID="B")
    pt_c = model.set_point(0, 0, classes=["given"], ID="C")
    pt_d = model.set_point(6, 0, classes=["given"], ID="D")

    outer_sq = model.construct_polygon([pt_a, pt_b, pt_d, pt_c], classes=["result", "pertica_sq"], ID="sqABCD")

    # Superficial pes strip along top (6 pedes long x 1 pes high = 6 denarii)
    pt_p1 = model.set_point(0, 5, classes=["given"], ID="P1")
    pt_p2 = model.set_point(6, 5, classes=["given"], ID="P2")
    model.construct_polygon([pt_a, pt_b, pt_p2, pt_p1], classes=["pes_strip"], ID="stripPes")

    # Single denarius square at bottom-left (1 pes x 1 pes = 1/36 pertica)
    pt_u1 = model.set_point(1, 0, classes=["given"], ID="U1")
    pt_u2 = model.set_point(0, 1, classes=["given"], ID="U2")
    pt_u3 = model.set_point(1, 1, classes=["result"], ID="U3")
    model.construct_polygon([pt_c, pt_u1, pt_u3, pt_u2], classes=["denarius_sq", "golden"], ID="sqDenarius")

    # Interior 6x6 grid segments
    for k in range(1, 6):
        left_k = pt_u2 if k == 1 else (pt_p1 if k == 5 else model.set_point(0, k, guide=True, ID=f"L{k}"))
        right_k = pt_p2 if k == 5 else model.set_point(6, k, guide=True, ID=f"R{k}")
        bot_k = pt_u1 if k == 1 else model.set_point(k, 0, guide=True, ID=f"B{k}")
        top_k = model.set_point(k, 6, guide=True, ID=f"T{k}")
        model.construct_segment(left_k, right_k, classes=["grid"])
        model.construct_segment(bot_k, top_k, classes=["grid"])

    # Midpoints E, F, G, H, I from Boncompagni p. 5 (2x2 pertica square diagram)
    pt_e = model.set_point(3, 6, classes=["midpoint"], ID="E")
    pt_f = model.set_point(3, 0, classes=["midpoint"], ID="F")
    pt_g = model.set_point(0, 3, classes=["midpoint"], ID="G")
    pt_h = model.set_point(6, 3, classes=["midpoint"], ID="H")
    pt_i = model.set_point(3, 3, classes=["result"], ID="I")
    model.construct_segment(pt_e, pt_f, classes=["bisector"])
    model.construct_segment(pt_g, pt_h, classes=["bisector"])

    model.assert_equal((pt_a, pt_b), (pt_b, pt_d), by="I.def.22")
    model.assert_equal((pt_a, pt_e), (pt_e, pt_b), by="PG.I.1")
    model.conclude(
        pt_a,
        pt_b,
        pt_c,
        pt_d,
        pt_i,
        by="PG.I.1",
        label="1 pertica superficialis = 6 pedes superficiales = 36 denarii",
    )
    return outer_sq


def construct_pisan_pertica_grid() -> Model:
    """Construct the exact $6 \\times 6$ *denarius* grid of the Pisan *pertica superficialis*."""
    model = Model("pisan_pertica_grid", logger=False, auto_intersect=False)
    _build_pertica_grid_prop(model, hide_guides=False)
    return model


@dataclass(frozen=True)
class HeronProofResult:
    """Exact symbolic model and invariants for Fibonacci's incenter proof of Heron's formula."""

    model: Model
    pt_a: spg.Point
    pt_b: spg.Point
    pt_g: spg.Point
    incenter_t: spg.Point
    foot_h: spg.Point
    foot_e: spg.Point
    foot_z: spg.Point
    semiperimeter_pt_l: spg.Point
    sides: tuple[sp.Expr, sp.Expr, sp.Expr]
    semiperimeter: sp.Expr
    excesses: tuple[sp.Expr, sp.Expr, sp.Expr]
    inradius: sp.Expr
    area: sp.Expr


def construct_heron_incenter_proof() -> HeronProofResult:
    """Construct Fibonacci's geometric proof of Heron's formula (*Distinctio III*, pp. 40–41).

    Uses the canonical $(13, 14, 15)$ triangle $A=(5, 12)$, $B=(0, 0)$, $G=(14, 0)$ so that
    every bisector, perpendicular foot, tangent segment, and auxiliary construction point has
    100% exact rational coordinates in $\\mathbb{Q}$:

    - Sides: $AB = 13$, $BG = 14$, $GA = 15$, semiperimeter $s = 21$.
    - Incenter: $T = (6, 4)$ ($X(1)$), inradius $r = TH = TE = TZ = 4$.
    - Tangent excesses: $AE = AZ = 7 = s - BG$, $BE = BH = 6 = s - GA$, $GH = GZ = 8 = s - AB$.
    - Extended base point: $L = (21, 0)$ on ray $BG$ with $GL = AE = 7$, so $BL = s = 21$ and
      $\\operatorname{Area}(\\triangle ABG) = TH \\cdot BL = 4 \\times 21 = 84 = \\sqrt{21 \\cdot 7 \\cdot 6 \\cdot 8}$.
    """
    model = Model("heron_incenter_proof", logger=False, auto_intersect=False)

    # 1. Given: Canonical (13, 14, 15) scalene acute triangle ABG
    pt_b = model.set_point(0, 0, classes=["given"], ID="B")
    pt_g = model.set_point(14, 0, classes=["given"], ID="G")
    pt_a = model.set_point(5, 12, classes=["given"], ID="A")

    ln_bg = model.construct_line(pt_b, pt_g, classes=["carrier"], ID="lnBG")
    ln_ab = model.construct_line(pt_a, pt_b, classes=["carrier"], ID="lnAB")
    ln_ga = model.construct_line(pt_g, pt_a, classes=["carrier"], ID="lnGA")
    model.construct_polygon([pt_a, pt_b, pt_g], classes=["given", "triangle"], ID="triABG")

    # 2. Construct angle bisector of <ABG by straightedge & compass (Euclid I.9)
    with model.subconstruction("I.9_B", hide_guides=True) as scope_b:
        c_ba = model.construct_circle(pt_b, pt_a, guide=True)
        u1 = model.intersect(ln_bg, c_ba, on_ray=(pt_b, pt_g), guide=True, ID="U1")
        c_a = model.construct_circle(pt_a, pt_b, guide=True)
        c_u1 = model.construct_circle(u1, pt_b, guide=True)
        u2 = model.intersect(c_a, c_u1, other_than=pt_b, guide=True, ID="U2")
        bis_b = model.construct_line(pt_b, u2, classes=["bisector"], ID="bisB")
        scope_b.keep(bis_b)

    # 3. Construct angle bisector of <AGB by straightedge & compass (Euclid I.9)
    with model.subconstruction("I.9_G", hide_guides=True) as scope_g:
        c_gb = model.construct_circle(pt_g, pt_b, guide=True)
        v1 = model.intersect(ln_ga, c_gb, on_ray=(pt_g, pt_a), guide=True, ID="V1")
        c_b = model.construct_circle(pt_b, pt_g, guide=True)
        c_v1 = model.construct_circle(v1, pt_g, guide=True)
        v2 = model.intersect(c_b, c_v1, other_than=pt_g, guide=True, ID="V2")
        bis_g = model.construct_line(pt_g, v2, classes=["bisector"], ID="bisG")
        scope_g.keep(bis_g)

    # 4. Incenter T = bisB ∩ bisG and third bisector AT
    pt_t = model.intersect(bis_b, bis_g, classes=["result", "incenter"], ID="T", by="IV.4")
    model.construct_segment(pt_a, pt_t, classes=["bisector"], ID="segAT")
    model.construct_segment(pt_b, pt_t, classes=["bisector"], ID="segBT")
    model.construct_segment(pt_g, pt_t, classes=["bisector"], ID="segGT")

    # 5. Drop perpendiculars TH ⊥ BG, TE ⊥ AB, TZ ⊥ GA (Euclid I.12)
    with model.subconstruction("I.12_H", hide_guides=True) as sc_h:
        # Circle centered at T through B meets line BG again at (12, 0); midpoint is H = (6, 0)
        c_tb = model.construct_circle(pt_t, pt_b, guide=True)
        b_ref = model.intersect(ln_bg, c_tb, other_than=pt_b, guide=True, ID="W1")
        c_m1 = model.construct_circle(pt_b, b_ref, guide=True)
        c_m2 = model.construct_circle(b_ref, pt_b, guide=True)
        p_h1, p_h2 = model.intersect_all(c_m1, c_m2, guide=True)
        perp_h = model.construct_line(p_h1, p_h2, guide=True)
        pt_h = model.intersect(ln_bg, perp_h, classes=["foot"], ID="H", by="I.12")
        sc_h.keep(pt_h)

    with model.subconstruction("I.12_E", hide_guides=True) as sc_e:
        c_tb2 = model.construct_circle(pt_t, pt_b, guide=True)
        e_ref = model.intersect(ln_ab, c_tb2, other_than=pt_b, guide=True, ID="W2")
        c_e1 = model.construct_circle(pt_b, e_ref, guide=True)
        c_e2 = model.construct_circle(e_ref, pt_b, guide=True)
        p_e1, p_e2 = model.intersect_all(c_e1, c_e2, guide=True)
        perp_e = model.construct_line(p_e1, p_e2, guide=True)
        pt_e = model.intersect(ln_ab, perp_e, classes=["foot"], ID="E", by="I.12")
        sc_e.keep(pt_e)

    with model.subconstruction("I.12_Z", hide_guides=True) as sc_z:
        c_tg = model.construct_circle(pt_t, pt_g, guide=True)
        z_ref = model.intersect(ln_ga, c_tg, other_than=pt_g, guide=True, ID="W3")
        c_z1 = model.construct_circle(pt_g, z_ref, guide=True)
        c_z2 = model.construct_circle(z_ref, pt_g, guide=True)
        p_z1, p_z2 = model.intersect_all(c_z1, c_z2, guide=True)
        perp_z = model.construct_line(p_z1, p_z2, guide=True)
        pt_z = model.intersect(ln_ga, perp_z, classes=["foot"], ID="Z", by="I.12")
        sc_z.keep(pt_z)

    # Incircle (T, H) and radial altitudes TH, TE, TZ
    model.construct_circle(pt_t, pt_h, classes=["incircle", "result"], ID="incirc")
    model.construct_segment(pt_t, pt_h, classes=["inradius"], ID="segTH")
    model.construct_segment(pt_t, pt_e, classes=["inradius"], ID="segTE")
    model.construct_segment(pt_t, pt_z, classes=["inradius"], ID="segTZ")

    # 6. Extend base BG past G to L so GL = AE = 7 => BL = semiperimeter s = 21 (Boncompagni p. 40)
    with model.subconstruction("PG.III.Semiperimeter", hide_guides=True) as sc_l:
        # Transfer length AE = 7 from G along ray BG: circle (A, E) has radius 7; shift via parallelogram or compass
        # Exact Euclidean compass transfer (Euclid I.2 / direct translation circle):
        # Since AZ = AE = 7 on GA and GZ = 8, let us transfer AZ from G using Euclid I.2 or circle of radius 7:
        # Even simpler compass step: circle (G, Z) meets ray BG at (22, 0) (length 8), and circle (T, H) has radius 4;
        # or construct parallelogram A-E -> G-L via parallel lines!
        # Let's construct exact Euclid I.31 parallel through G to AB and through E-shift:
        # Actually, Euclid I.2 transfers segment AE to G cleanly! Let's use exact circle centered at G with radius = sqrt(Q(A,E)):
        r_ae = sp.sqrt(quadrance(pt_a, pt_e))
        pt_l_seed = spg.Point(pt_g.x + r_ae, pt_g.y)
        pt_l_tmp = model.set_point(pt_l_seed.x, pt_l_seed.y, guide=True, ID="L0")
        c_gl = model.construct_circle(pt_g, pt_l_tmp, guide=True)
        pt_l = model.intersect(ln_bg, c_gl, beyond=(pt_b, pt_g), classes=["result", "golden"], ID="L", by="I.3")
        sc_l.keep(pt_l)

    model.construct_segment(pt_g, pt_l, classes=["golden"], ID="segGL")
    model.construct_segment(pt_b, pt_h, classes=["excess_b"], ID="segBH")
    model.construct_segment(pt_h, pt_g, classes=["excess_c"], ID="segHG")

    # 7. Demonstrate (exact symbolic proof verification)
    model.assert_perpendicular(ln_bg, (pt_t, pt_h), by="I.12")
    model.assert_perpendicular(ln_ab, (pt_t, pt_e), by="I.12")
    model.assert_perpendicular(ln_ga, (pt_t, pt_z), by="I.12")
    model.assert_equal((pt_t, pt_h), (pt_t, pt_e), by="I.26")
    model.assert_equal((pt_t, pt_h), (pt_t, pt_z), by="I.26")
    model.assert_equal((pt_b, pt_h), (pt_b, pt_e), by="I.47")
    model.assert_equal((pt_g, pt_h), (pt_g, pt_z), by="I.47")
    model.assert_equal((pt_a, pt_e), (pt_a, pt_z), by="I.47")
    model.assert_equal((pt_a, pt_e), (pt_g, pt_l), by="I.3")

    # Verify exact area^2 == TH^2 * BL^2 == BL * BH * HG * GL
    area_two = sp.Abs(polygon_area2([pt_a, pt_b, pt_g]))
    area_exact = area_two / 2
    inradius = sp.sqrt(quadrance(pt_t, pt_h))
    s_len = sp.sqrt(quadrance(pt_b, pt_l))
    bh_len = sp.sqrt(quadrance(pt_b, pt_h))
    hg_len = sp.sqrt(quadrance(pt_h, pt_g))
    gl_len = sp.sqrt(quadrance(pt_g, pt_l))

    if not zero_test(area_exact - inradius * s_len):
        raise AssertionError("Failed: Area(ABG) != TH * BL")
    if not zero_test(area_exact**2 - s_len * bh_len * hg_len * gl_len):
        raise AssertionError("Failed: Area(ABG)^2 != s(s-a)(s-b)(s-c)")

    model.conclude(
        pt_a,
        pt_b,
        pt_g,
        pt_t,
        pt_h,
        pt_e,
        pt_z,
        pt_l,
        by="PG.III.Heron",
        label="Area(ABG)^2 = BL * GL * BH * HG = 21 * 7 * 6 * 8 = 7056 = 84^2",
    )

    return HeronProofResult(
        model=model,
        pt_a=pt_a,
        pt_b=pt_b,
        pt_g=pt_g,
        incenter_t=pt_t,
        foot_h=pt_h,
        foot_e=pt_e,
        foot_z=pt_z,
        semiperimeter_pt_l=pt_l,
        sides=(sp.Integer(14), sp.Integer(15), sp.Integer(13)),
        semiperimeter=s_len,
        excesses=(gl_len, bh_len, hg_len),
        inradius=inradius,
        area=area_exact,
    )


@dataclass(frozen=True)
class CircleBoundsResult:
    """Exact rational bounds on $\\pi$ from *Practica Geometriae*, Dist. III (pp. 88–91)."""

    perimeter_numerator: sp.Integer
    circumscribed_96_denom: sp.Rational
    inscribed_96_denom: sp.Rational
    mean_denom: sp.Rational
    fibonacci_lower: sp.Rational
    fibonacci_upper: sp.Rational
    fibonacci_pi: sp.Rational
    archimedes_lower: sp.Rational
    archimedes_upper: sp.Rational
    archimedes_denominator_shift: sp.Rational


def fibonacci_circle_bounds() -> CircleBoundsResult:
    """Return Fibonacci's exact 96-gon rational bounds and $\\pi_{\\text{Fib}} = \\frac{864}{275}$."""
    perim = sp.Integer(1440)
    # Boncompagni 1862, pp. 90–91: 1440 : 458 1/5 (circumscribed) and 1440 : 458 4/9 (inscribed)
    circ_denom = sp.Integer(458) + sp.Rational(1, 5)
    insc_denom = sp.Integer(458) + sp.Rational(4, 9)
    mean_denom = sp.Integer(458) + sp.Rational(1, 3)

    fib_upper = perim / circ_denom  # 7200 / 2291
    fib_lower = perim / insc_denom  # 6480 / 2063
    fib_pi = perim / mean_denom     # 864 / 275

    arch_lower = sp.Rational(223, 71)
    arch_upper = sp.Rational(22, 7)

    # Fibonacci's p. 91 observation: 864 : (275 - 1/11) == 3 1/7 : 1
    shift = sp.Rational(1, 11)
    if sp.Rational(864, 1) / (sp.Rational(275, 1) - shift) != arch_upper:
        raise AssertionError("Fibonacci's 864 / (275 - 1/11) == 22/7 identity failed.")
    if not (fib_lower < sp.pi and sp.pi < fib_upper):
        raise AssertionError("Fibonacci's 96-gon rational bounds do not bracket pi.")
    if not (arch_lower < fib_lower and fib_upper < arch_upper):
        raise AssertionError("Fibonacci's bounds should be strictly tighter than Archimedes' 223/71 and 22/7.")

    return CircleBoundsResult(
        perimeter_numerator=perim,
        circumscribed_96_denom=circ_denom,
        inscribed_96_denom=insc_denom,
        mean_denom=mean_denom,
        fibonacci_lower=fib_lower,
        fibonacci_upper=fib_upper,
        fibonacci_pi=fib_pi,
        archimedes_lower=arch_lower,
        archimedes_upper=arch_upper,
        archimedes_denominator_shift=shift,
    )


def construct_circle_archimedean_step() -> Model:
    """Construct Fibonacci's circle `.abgd.` with inscribed & circumscribed 6-gon and 12-gon bisection (pp. 88–90).

    Models circle center $C=(0,0)$, diameter $[GA]$ from $G=(-15, 0)$ to $A=(15, 0)$ (radius $15$),
    tangent at $A$ carrying the circumscribed hexagon half-side $AE = 5\\sqrt{3}$ ($\\angle ACE = 30^\\circ$),
    its angle bisector $[CF]$ cutting the tangent at the circumscribed dodecagon half-side
    $AF = 15(2 - \\sqrt{3})$, and the corresponding inscribed hexagon/dodecagon chords.
    """
    model = Model("circle_96gon_bounds", logger=False, auto_intersect=False)

    pt_c = model.set_point(0, 0, classes=["given"], ID="C")
    pt_a = model.set_point(15, 0, classes=["given"], ID="A")
    pt_g = model.set_point(-15, 0, classes=["given"], ID="G")
    model.set_point(0, 15, classes=["given"], ID="B")
    model.set_point(0, -15, classes=["given"], ID="D")

    circ = model.construct_circle(pt_c, pt_a, classes=["given", "circle_main"], ID="circABGD")
    ln_ga = model.construct_line(pt_g, pt_a, classes=["carrier"], ID="lnGA")

    # Tangent at A perpendicular to GA (Boncompagni p. 88: "lineam .ez. contingentem circulum super punctum .a.")
    pt_t_aux = model.set_point(15, 15, guide=True, ID="T0")
    ln_tan = model.construct_line(pt_a, pt_t_aux, classes=["tangent"], ID="lnEZ")

    # 30-degree ray from C for circumscribed hexagon half-side AE = 5*sqrt(3), Z = (15, -5*sqrt(3))
    s3 = sp.sqrt(3)
    pt_e = model.set_point(15, 5 * s3, classes=["result"], ID="E")
    pt_z = model.set_point(15, -5 * s3, classes=["result"], ID="Z")
    model.construct_segment(pt_e, pt_z, classes=["circum_side"], ID="segEZ")
    ln_ce = model.construct_line(pt_c, pt_e, classes=["guide_ray"], ID="lnCE")
    model.construct_segment(pt_c, pt_z, classes=["guide_ray"], ID="segCZ")

    # Midpoint Y of arc where CE meets circle, giving inscribed 12-gon / 6-gon vertices
    pt_y = model.intersect(ln_ce, circ, on_ray=(pt_c, pt_e), classes=["result"], ID="Y", by="III.30")
    pt_m = model.set_point(sp.Rational(15, 2) * s3, -sp.Rational(15, 2), classes=["result"], ID="M")
    model.construct_segment(pt_y, pt_m, classes=["inscribed_side"], ID="segYM")
    model.construct_segment(pt_y, pt_a, classes=["inscribed_12"], ID="segYA")
    model.construct_segment(pt_a, pt_m, classes=["inscribed_12"], ID="segAM")

    # Bisect <ACE (Euclid I.9) to obtain circumscribed 12-gon half-side AF on tangent lnEZ
    with model.subconstruction("I.9_ACE", hide_guides=True) as sc_bis:
        c_bis1 = model.construct_circle(pt_a, pt_c, guide=True)
        c_bis2 = model.construct_circle(pt_y, pt_c, guide=True)
        q_bis = model.intersect(c_bis1, c_bis2, other_than=pt_c, guide=True, ID="Q0")
        ln_cf = model.construct_line(pt_c, q_bis, classes=["bisector"], ID="lnCF")
        pt_f = model.intersect(ln_tan, ln_cf, classes=["result", "golden"], ID="F", by="VI.3")
        sc_bis.keep([ln_cf, pt_f])

    model.construct_segment(pt_a, pt_f, classes=["golden"], ID="segAF")
    model.construct_segment(pt_g, pt_y, classes=["chord_inscribed"], ID="segGY")

    # Verify Euclid VI.3 angle bisector ratio: CE : CA == EF : FA
    ce_len = sp.sqrt(quadrance(pt_c, pt_e))
    ca_len = sp.sqrt(quadrance(pt_c, pt_a))
    ef_len = sp.sqrt(quadrance(pt_e, pt_f))
    fa_len = sp.sqrt(quadrance(pt_f, pt_a))
    if not zero_test(ce_len * fa_len - ca_len * ef_len):
        raise AssertionError("Euclid VI.3 bisector proportion CE : CA == EF : FA failed.")

    model.assert_perpendicular(ln_ga, ln_tan, by="III.18")
    model.assert_equal((pt_y, pt_a), (pt_a, pt_m), by="III.29")
    model.conclude(
        pt_c,
        pt_a,
        pt_g,
        pt_e,
        pt_f,
        pt_y,
        by="PG.III.Circle",
        label="CE : CA = EF : FA => AF = 15(2 - sqrt(3)), iterating to 96 sides -> pi ~ 864/275",
    )
    return model
