r"""Exact Euclidean constructions for *Practica Geometriae*, Distinctio IV (*De divisione camporum*).

Preserves and formalizes in :mod:`geometor.model` Leonardo Pisano's celebrated 1220 Latin
transmission and expansion of **Euclid's lost treatise *On Divisions of Figures*** (Boncompagni
1862, Vol. II, pp. 110–148):

1. **Dividing a Triangle from a Point on a Side** (pp. 111–112, ``fol. 68v–69r``):
   Straightedge-and-compass division of $\triangle ABG$ in exact ratio $p : q$ by a line $[DZ]$
   drawn from any given point $D$ on side $[BG]$, using Euclid I.31 parallel transfer $[EZ] \parallel [AD]$
   and Euclid I.37 equal-area shearing ($\triangle ADE = \triangle ADZ$).
2. **Dividing a Triangle Parallel to the Base** (p. 119, ``fol. 73r–73v``):
   Straightedge-and-compass division of $\triangle ABG$ in exact ratio $p : q$ by $[EZ] \parallel [BG]$
   via Euclid VI.13 semicircle mean proportional $AE = \sqrt{\frac{p}{p+q}}\, AB$.
3. **Concurrency of Medians & Three-Consort Centroid Division** (pp. 112–113, 120, ``fol. 69r–74r``):
   Fibonacci's *Preparatoria* proving the $2 : 1$ concurrency of medians at centroid $D$ ($X(2)$)
   and partitioning $\triangle ABG$ into three equal consort triangles $\triangle DAB, \triangle DBG, \triangle DGA$.
4. **Dividing a Trapezoid Parallel to its Bases** (*Distinctio IV, Pars II*):
   Root-mean-square chord $c = \sqrt{\frac{q a^2 + p b^2}{p + q}}$, linking planar field division
   to three squares in arithmetic progression ($7^2, 13^2, 17^2$) in *Liber Quadratorum* (1225).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test
from geometor.model.invariants import polygon_area2
from sympy.simplify.sqrtdenest import sqrtdenest

__all__ = [
    "SidePointDivisionResult",
    "ParallelDivisionResult",
    "CentroidDivisionResult",
    "TrapezoidDivisionResult",
    "construct_parallel_line",
    "construct_midpoint",
    "construct_triangle_side_point_division",
    "construct_triangle_parallel_division",
    "construct_triangle_medians_centroid",
    "trapezoid_parallel_division",
]


def construct_midpoint(
    model: Model,
    pt_p: spg.Point,
    pt_q: spg.Point,
    *,
    pt_id: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Construct the exact midpoint of $[PQ]$ via Euclid I.10 symmetric circles."""
    with model.subconstruction(f"I.10_{pt_id or 'mid'}", hide_guides=True) as scope:
        ln_pq = model.construct_line(pt_p, pt_q, guide=True)
        c1 = model.construct_circle(pt_p, pt_q, guide=True)
        c2 = model.construct_circle(pt_q, pt_p, guide=True)
        m1, m2 = model.intersect_all(c1, c2, guide=True)
        perp = model.construct_line(m1, m2, guide=True)
        mid = model.intersect(
            ln_pq,
            perp,
            classes=list(classes) if classes else None,
            guide=guide,
            ID=pt_id,
            by="I.10",
        )
        if not guide:
            scope.keep(mid)
        return mid


def construct_parallel_line(
    model: Model,
    ref_p1: spg.Point,
    ref_p2: spg.Point,
    through_pt: spg.Point,
    *,
    line_id: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line:
    """Construct the line through ``through_pt`` parallel to $[\\text{ref\\_p1}\\,\\text{ref\\_p2}]$ (Euclid I.31).

    Uses central reflection across the midpoint $M$ of $[\\text{ref\\_p2}, \\text{through\\_pt}]$ so
    quadrilateral $(\\text{ref\\_p1}, \\text{ref\\_p2}, \\text{S}, \\text{through\\_pt})$ is an exact
    parallelogram over any symbolic subfield of $\\mathbb{R}$.
    """
    with model.subconstruction(f"I.31_{line_id or 'par'}", hide_guides=True) as scope:
        mid_m = construct_midpoint(model, ref_p2, through_pt, guide=True)
        ln_pm = model.construct_line(ref_p1, mid_m, guide=True)
        c_mp = model.construct_circle(mid_m, ref_p1, guide=True)
        pt_s = model.intersect(ln_pm, c_mp, other_than=ref_p1, guide=True)
        par_ln = model.construct_line(
            through_pt,
            pt_s,
            classes=list(classes) if classes else None,
            guide=guide,
            ID=line_id,
        )
        if not guide:
            scope.keep(par_ln)
        return par_ln


def _divide_segment_in_ratio(
    model: Model,
    pt_start: spg.Point,
    pt_end: spg.Point,
    num: int,
    den: int,
    *,
    pt_id: str,
    classes: list[str] | None = None,
) -> spg.Point:
    """Divide $[\\text{pt\\_start}, \\text{pt\\_end}]$ at $E$ with $|\\text{pt\\_start}\\,E| : |\\text{pt\\_start}\\,\\text{pt\\_end}| = \\text{num} : \\text{den}$ (Euclid VI.9)."""
    if num <= 0 or den <= num:
        raise ValueError(f"Expected 0 < num < den, got {num}/{den}.")
    if 2 * num == den:
        return construct_midpoint(model, pt_start, pt_end, pt_id=pt_id, classes=classes)

    with model.subconstruction(f"VI.9_{pt_id}", hide_guides=True) as scope:
        ln_base = model.construct_line(pt_start, pt_end, guide=True)
        # Auxiliary non-collinear ray via equilateral pole (Euclid I.1)
        c1 = model.construct_circle(pt_start, pt_end, guide=True)
        c2 = model.construct_circle(pt_end, pt_start, guide=True)
        u_step = model.intersect(c1, c2, index=0, guide=True)
        ln_ray = model.construct_line(pt_start, u_step, guide=True)

        # Step off `den` equal compass steps along ln_ray starting from pt_start
        marks: list[spg.Point] = [pt_start, u_step]
        for _step_idx in range(2, den + 1):
            prev_center = marks[-1]
            prev_prev = marks[-2]
            c_step = model.construct_circle(prev_center, prev_prev, guide=True)
            nxt = model.intersect(ln_ray, c_step, other_than=prev_prev, guide=True)
            marks.append(nxt)

        mark_num = marks[num]
        mark_den = marks[den]
        par = construct_parallel_line(model, mark_den, pt_end, mark_num, guide=True)
        pt_div = model.intersect(
            ln_base,
            par,
            classes=list(classes) if classes else None,
            ID=pt_id,
            by="VI.9",
        )
        scope.keep(pt_div)
        return pt_div


@dataclass(frozen=True)
class SidePointDivisionResult:
    """Exact model & invariants for dividing $\\triangle ABG$ from a point $D$ on side $BG$."""

    model: Model
    pt_a: spg.Point
    pt_b: spg.Point
    pt_g: spg.Point
    pt_d: spg.Point
    pt_e: spg.Point
    pt_z: spg.Point
    ratio_p: int
    ratio_q: int
    gz_length: sp.Expr
    area_dzg: sp.Expr
    area_abdz: sp.Expr
    area_total: sp.Expr


def construct_triangle_side_point_division(
    *,
    p: int = 1,
    q: int = 1,
    d_offset_from_b: int | sp.Rational = 5,
) -> SidePointDivisionResult:
    """Divide $\\triangle ABG$ $(13, 14, 15)$ in ratio $p : q$ from point $D$ on $[BG]$ (Boncompagni p. 112).

    Assumes $D$ lies between $B$ and the fractional base division point $E$ (so $BD < BE$, i.e.,
    $Z$ falls on side $[AG]$ just as in Fibonacci's figure on p. 112 where $BD = 5$, $BE = 7$,
    $DG = 9$, and $GZ = 11\\frac{2}{3}$).
    """
    if p <= 0 or q <= 0:
        raise ValueError("Ratio components p and q must be positive integers.")

    model = Model("division_side_point", logger=False, auto_intersect=False)

    # 1. Given: Canonical (13, 14, 15) triangle ABG and point D on side BG
    pt_b = model.set_point(0, 0, classes=["given"], ID="B")
    pt_g = model.set_point(14, 0, classes=["given"], ID="G")
    pt_a = model.set_point(5, 12, classes=["given"], ID="A")
    pt_d = model.set_point(sp.Rational(d_offset_from_b), 0, classes=["given", "consort_pt"], ID="D")

    model.construct_line(pt_b, pt_g, classes=["carrier"], ID="lnBG")
    model.construct_line(pt_a, pt_b, classes=["carrier"], ID="lnAB")
    ln_ga = model.construct_line(pt_g, pt_a, classes=["carrier"], ID="lnGA")
    model.construct_polygon([pt_a, pt_b, pt_g], classes=["given", "triangle"], ID="triABG")

    # 2. Construct E on BG so GE : BG = p : (p + q) (hence BE : BG = q : (p + q))
    pt_e = _divide_segment_in_ratio(
        model,
        pt_g,
        pt_b,
        p,
        p + q,
        pt_id="E",
        classes=["midpoint"],
    )
    if sp.simplify(pt_d.x - pt_e.x) >= 0:
        raise ValueError("Point D must lie closer to B than E so cut [DZ] meets side [AG].")

    # 3. Join [AD] and [AE], construct [EZ] || [AD] meeting [GA] at Z, and join [DZ]
    ln_ad = model.construct_line(pt_a, pt_d, classes=["guide_ray"], ID="lnAD")
    model.construct_segment(pt_a, pt_e, classes=["guide_ray"], ID="segAE")
    ln_ez = construct_parallel_line(
        model,
        pt_a,
        pt_d,
        pt_e,
        line_id="lnEZ",
        classes=["parallel_guide"],
    )
    pt_z = model.intersect(ln_ga, ln_ez, classes=["result", "division_pt"], ID="Z", by="VI.2")

    model.construct_segment(pt_d, pt_z, classes=["result", "cut_line", "golden"], ID="segDZ")
    model.construct_polygon([pt_d, pt_z, pt_g], classes=["share_p"], ID="polyDZG")
    model.construct_polygon([pt_a, pt_b, pt_d, pt_z], classes=["share_q"], ID="polyABDZ")

    # 4. Demonstrate (Euclid I.31, I.37, and exact signed area ratio p : q)
    model.assert_collinear(pt_b, pt_d, pt_g, by="given")
    model.assert_collinear(pt_b, pt_e, pt_g, by="VI.9")
    model.assert_parallel(ln_ad, ln_ez, by="I.31")
    model.assert_area_equal([pt_a, pt_d, pt_e], [pt_a, pt_d, pt_z], by="I.37")

    area_total = sp.Abs(polygon_area2([pt_a, pt_b, pt_g])) / 2
    area_dzg = sp.Abs(polygon_area2([pt_d, pt_z, pt_g])) / 2
    area_abdz = sp.Abs(polygon_area2([pt_a, pt_b, pt_d, pt_z])) / 2
    gz_len = sp.sqrt(quadrance(pt_g, pt_z))

    if not zero_test(area_dzg * (p + q) - area_total * p):
        raise AssertionError("Area(DZG) / Area(ABG) != p / (p + q)")
    if not zero_test(area_dzg + area_abdz - area_total):
        raise AssertionError("Areas of shares DZG and ABDZ do not sum to Area(ABG)")

    model.conclude(
        pt_a,
        pt_b,
        pt_g,
        pt_d,
        pt_e,
        pt_z,
        by="PG.IV.SidePoint",
        label=f"Area(DZG) : Area(ABDZ) = {p} : {q}",
    )

    return SidePointDivisionResult(
        model=model,
        pt_a=pt_a,
        pt_b=pt_b,
        pt_g=pt_g,
        pt_d=pt_d,
        pt_e=pt_e,
        pt_z=pt_z,
        ratio_p=p,
        ratio_q=q,
        gz_length=sp.simplify(gz_len),
        area_dzg=area_dzg,
        area_abdz=area_abdz,
        area_total=area_total,
    )


@dataclass(frozen=True)
class ParallelDivisionResult:
    """Exact model & invariants for dividing $\\triangle ABG$ by $[EZ] \\parallel [BG]$."""

    model: Model
    pt_a: spg.Point
    pt_b: spg.Point
    pt_g: spg.Point
    pt_d: spg.Point
    pt_k: spg.Point
    pt_e: spg.Point
    pt_z: spg.Point
    ratio_p: int
    ratio_q: int
    ae_quadrance: sp.Expr
    az_quadrance: sp.Expr
    ez_quadrance: sp.Expr
    area_aez: sp.Expr
    area_ebgz: sp.Expr
    area_total: sp.Expr


def construct_triangle_parallel_division(
    *,
    p: int = 1,
    q: int = 1,
    preset: str = "10-14-12",
) -> ParallelDivisionResult:
    """Divide $\\triangle ABG$ in ratio $p : q$ by $[EZ] \\parallel [BG]$ via Euclid VI.13 mean proportional.

    Supports two exact symbolic presets:

    - ``"10-14-12"`` (default): Fibonacci's exact numerical triangle on Boncompagni p. 119
      ($AB = 10$, $BG = 14$, $GA = 12$), where $p = q = 1$ yields $AE^2 = 50$, $AZ^2 = 72$, $EZ^2 = 98$.
    - ``"13-14-15"``: Heronian triangle $A=(5, 12)$, $B=(0, 0)$, $G=(14, 0)$.
    """
    if p <= 0 or q <= 0:
        raise ValueError("Ratio components p and q must be positive integers.")

    model = Model("division_parallel_base", logger=False, auto_intersect=False)

    pt_b = model.set_point(0, 0, classes=["given"], ID="B")
    pt_g = model.set_point(14, 0, classes=["given"], ID="G")
    if preset == "10-14-12":
        # Exact coordinates for AB = 10, BG = 14, GA = 12: x = 38/7, y = 24*sqrt(6)/7
        pt_a = model.set_point(
            sp.Rational(38, 7),
            sp.Rational(24, 7) * sp.sqrt(6),
            classes=["given"],
            ID="A",
        )
    elif preset == "13-14-15":
        pt_a = model.set_point(5, 12, classes=["given"], ID="A")
    else:
        raise ValueError(f"Unknown preset {preset!r}; expected '10-14-12' or '13-14-15'.")

    ln_bg = model.construct_line(pt_b, pt_g, classes=["carrier"], ID="lnBG")
    ln_ba = model.construct_line(pt_b, pt_a, classes=["carrier"], ID="lnBA")
    ln_ga = model.construct_line(pt_g, pt_a, classes=["carrier"], ID="lnGA")
    model.construct_polygon([pt_a, pt_b, pt_g], classes=["given", "triangle"], ID="triABG")

    # 1. Mark fractional segment on [AB] of length (p / (p + q)) * AB, then swing past A to D
    pt_f_frac = _divide_segment_in_ratio(
        model,
        pt_a,
        pt_b,
        p,
        p + q,
        pt_id="F1",
        classes=["guide"],
    )
    model[pt_f_frac].guide = True
    c_ad = model.construct_circle(pt_a, pt_f_frac, guide=True)
    pt_d = model.intersect(
        ln_ba,
        c_ad,
        beyond=(pt_b, pt_a),
        classes=["midpoint"],
        ID="D",
        by="I.3",
    )
    model.construct_segment(pt_a, pt_d, classes=["guide_ray"], ID="segAD")

    # 2. Euclid VI.13 semicircle on diameter [BD] and perpendicular at A to find mean proportional AK
    mid_bd = construct_midpoint(model, pt_b, pt_d, pt_id="O1", guide=True)
    semicirc = model.construct_circle(mid_bd, pt_b, classes=["semicircle_guide"], ID="circBD")

    with model.subconstruction("I.11_A", hide_guides=True) as sc_perp:
        # Symmetric points F1 and D around A already have equal distance from A!
        c_p1 = model.construct_circle(pt_f_frac, pt_d, guide=True)
        c_p2 = model.construct_circle(pt_d, pt_f_frac, guide=True)
        n1, n2 = model.intersect_all(c_p1, c_p2, guide=True)
        ln_perp_a = model.construct_line(n1, n2, guide=True)
        pt_k = model.intersect(
            semicirc,
            ln_perp_a,
            side_of=(pt_b, pt_a, 1),
            classes=["result", "mean_pt"],
            ID="K",
            by="VI.13",
        )
        sc_perp.keep(pt_k)

    model.construct_segment(pt_a, pt_k, classes=["bisector"], ID="segAK")

    # 3. Transfer mean proportional AK onto side [AB] via circle (A, K) -> point E, then [EZ] || [BG]
    c_ak = model.construct_circle(pt_a, pt_k, classes=["transfer_arc"], ID="circAK")
    pt_e = model.intersect(
        ln_ba,
        c_ak,
        between=(pt_a, pt_b),
        classes=["result", "division_pt"],
        ID="E",
        by="I.3",
    )
    ln_ez = construct_parallel_line(
        model,
        pt_b,
        pt_g,
        pt_e,
        line_id="lnEZ",
        classes=["parallel_guide"],
    )
    pt_z = model.intersect(
        ln_ga,
        ln_ez,
        classes=["result", "division_pt"],
        ID="Z",
        by="VI.2",
    )

    model.construct_segment(pt_e, pt_z, classes=["result", "cut_line", "golden"], ID="segEZ")
    model.construct_polygon([pt_a, pt_e, pt_z], classes=["share_p"], ID="polyAEZ")
    model.construct_polygon([pt_e, pt_b, pt_g, pt_z], classes=["share_q"], ID="polyEBGZ")

    # 4. Demonstrate (Euclid VI.13, VI.19 duplicate ratio of similar triangles)
    model.assert_perpendicular(ln_ba, (pt_a, pt_k), by="I.11")
    model.assert_equal((pt_a, pt_k), (pt_a, pt_e), by="I.3")
    model.assert_parallel(ln_bg, ln_ez, by="I.31")

    def _clean(expr: sp.Expr) -> sp.Expr:
        return sp.simplify(sp.radsimp(sqrtdenest(expr)))

    q_ab = _clean(quadrance(pt_a, pt_b))
    q_ae = _clean(quadrance(pt_a, pt_e))
    q_az = _clean(quadrance(pt_a, pt_z))
    q_ez = _clean(quadrance(pt_e, pt_z))
    q_bg = _clean(quadrance(pt_b, pt_g))

    if not zero_test(q_ae * (p + q) - q_ab * p):
        raise AssertionError("Mean proportional failed: Q(A, E) / Q(A, B) != p / (p + q)")
    if not zero_test(q_ez * (p + q) - q_bg * p):
        raise AssertionError("Similar base scaling failed: Q(E, Z) / Q(B, G) != p / (p + q)")

    area_total = _clean(sp.Abs(polygon_area2([pt_a, pt_b, pt_g])) / 2)
    area_aez = _clean(sp.Abs(polygon_area2([pt_a, pt_e, pt_z])) / 2)
    area_ebgz = _clean(sp.Abs(polygon_area2([pt_e, pt_b, pt_g, pt_z])) / 2)

    if not zero_test(area_aez * (p + q) - area_total * p):
        raise AssertionError("Area(AEZ) / Area(ABG) != p / (p + q)")

    model.conclude(
        pt_a,
        pt_b,
        pt_g,
        pt_d,
        pt_k,
        pt_e,
        pt_z,
        by="PG.IV.ParallelBase",
        label=f"AE^2 : AB^2 = {p} : {p + q} => Area(AEZ) : Area(EBGZ) = {p} : {q}",
    )

    return ParallelDivisionResult(
        model=model,
        pt_a=pt_a,
        pt_b=pt_b,
        pt_g=pt_g,
        pt_d=pt_d,
        pt_k=pt_k,
        pt_e=pt_e,
        pt_z=pt_z,
        ratio_p=p,
        ratio_q=q,
        ae_quadrance=q_ae,
        az_quadrance=q_az,
        ez_quadrance=q_ez,
        area_aez=area_aez,
        area_ebgz=area_ebgz,
        area_total=area_total,
    )


@dataclass(frozen=True)
class CentroidDivisionResult:
    """Exact model & invariants for Fibonacci's median concurrency & 3-consort centroid partition."""

    model: Model
    pt_a: spg.Point
    pt_b: spg.Point
    pt_g: spg.Point
    mid_e: spg.Point
    mid_z: spg.Point
    mid_t: spg.Point
    centroid_d: spg.Point
    consort_area: sp.Expr
    total_area: sp.Expr


def construct_triangle_medians_centroid() -> CentroidDivisionResult:
    """Construct Fibonacci's *Preparatoria* on medians & 3-consort centroid division (pp. 112–113, 120)."""
    model = Model("division_medians_centroid", logger=False, auto_intersect=False)

    pt_b = model.set_point(0, 0, classes=["given"], ID="B")
    pt_g = model.set_point(14, 0, classes=["given"], ID="G")
    pt_a = model.set_point(5, 12, classes=["given"], ID="A")

    model.construct_line(pt_b, pt_g, classes=["carrier"], ID="lnBG")
    model.construct_line(pt_a, pt_b, classes=["carrier"], ID="lnAB")
    model.construct_line(pt_g, pt_a, classes=["carrier"], ID="lnGA")
    model.construct_polygon([pt_a, pt_b, pt_g], classes=["given", "triangle"], ID="triABG")

    # Midpoints E of BG, Z of GA, T of AB (Boncompagni p. 113 labels: e on bg, z on ag, t on ab, centroid d)
    mid_e = construct_midpoint(model, pt_b, pt_g, pt_id="E", classes=["midpoint"])
    mid_z = construct_midpoint(model, pt_g, pt_a, pt_id="Z", classes=["midpoint"])
    mid_t = construct_midpoint(model, pt_a, pt_b, pt_id="T", classes=["midpoint"])

    med_ae = model.construct_line(pt_a, mid_e, classes=["bisector"], ID="lnAE")
    med_bz = model.construct_line(pt_b, mid_z, classes=["bisector"], ID="lnBZ")
    model.construct_line(pt_g, mid_t, classes=["bisector"], ID="lnGT")

    pt_d = model.intersect(med_ae, med_bz, classes=["result", "centroid", "golden"], ID="D", by="PG.IV.Prep")

    # Three equal consort triangles resting on the three sides AB, BG, GA (Boncompagni p. 120)
    model.construct_segment(pt_a, pt_d, classes=["result", "cut_line"], ID="segAD")
    model.construct_segment(pt_b, pt_d, classes=["result", "cut_line"], ID="segBD")
    model.construct_segment(pt_g, pt_d, classes=["result", "cut_line"], ID="segGD")
    model.construct_polygon([pt_d, pt_a, pt_b], classes=["share_p"], ID="polyDAB")
    model.construct_polygon([pt_d, pt_b, pt_g], classes=["share_q"], ID="polyDBG")
    model.construct_polygon([pt_d, pt_g, pt_a], classes=["pes_strip"], ID="polyDGA")

    # Verify concurrency of third median GT at D, 2:1 ratio (Q = 4:1), and 3 equal consort areas
    model.assert_collinear(pt_g, pt_d, mid_t, by="PG.IV.Prep")
    if not zero_test(quadrance(pt_a, pt_d) - 4 * quadrance(pt_d, mid_e)):
        raise AssertionError("Centroid 2:1 ratio failed on median AE.")
    if not zero_test(quadrance(pt_b, pt_d) - 4 * quadrance(pt_d, mid_z)):
        raise AssertionError("Centroid 2:1 ratio failed on median BZ.")
    if not zero_test(quadrance(pt_g, pt_d) - 4 * quadrance(pt_d, mid_t)):
        raise AssertionError("Centroid 2:1 ratio failed on median GT.")

    model.assert_area_equal([pt_d, pt_a, pt_b], [pt_d, pt_b, pt_g], by="I.38")
    model.assert_area_equal([pt_d, pt_b, pt_g], [pt_d, pt_g, pt_a], by="I.38")

    total_area = sp.Abs(polygon_area2([pt_a, pt_b, pt_g])) / 2
    consort_area = sp.Abs(polygon_area2([pt_d, pt_b, pt_g])) / 2

    model.conclude(
        pt_a,
        pt_b,
        pt_g,
        mid_e,
        mid_z,
        mid_t,
        pt_d,
        by="PG.IV.Centroid",
        label="AD : DE = 2 : 1 and Area(DAB) = Area(DBG) = Area(DGA) = 28",
    )

    return CentroidDivisionResult(
        model=model,
        pt_a=pt_a,
        pt_b=pt_b,
        pt_g=pt_g,
        mid_e=mid_e,
        mid_z=mid_z,
        mid_t=mid_t,
        centroid_d=pt_d,
        consort_area=consort_area,
        total_area=total_area,
    )


@dataclass(frozen=True)
class TrapezoidDivisionResult:
    """Exact symbolic result for dividing a trapezoid parallel to bases $a$ and $b$ in ratio $p : q$."""

    top_base_a: sp.Expr
    bottom_base_b: sp.Expr
    height: sp.Expr
    ratio_p: sp.Expr
    ratio_q: sp.Expr
    dividing_chord_c: sp.Expr
    upper_height: sp.Expr
    lower_height: sp.Expr
    upper_area: sp.Expr
    lower_area: sp.Expr


def trapezoid_parallel_division(
    top_base_a: int | sp.Expr = 7,
    bottom_base_b: int | sp.Expr = 17,
    height: int | sp.Expr = 10,
    *,
    p: int | sp.Expr = 1,
    q: int | sp.Expr = 1,
) -> TrapezoidDivisionResult:
    """Compute the exact parallel dividing line of a trapezoid (*Distinctio IV, Pars II*).

    For parallel bases $a$ (top) and $b$ (bottom), the parallel chord $c$ cutting off upper area :
    lower area $= p : q$ satisfies $c^2 = \\frac{q a^2 + p b^2}{p + q}$. On $(a, b) = (7, 17)$ with
    $p = q = 1$, $c = \\sqrt{(49 + 289)/2} = 13$, exhibiting the arithmetic progression of squares
    $(7^2, 13^2, 17^2)$ with *congruum* $120$ celebrated in Fibonacci's *Liber Quadratorum* (1225).
    """
    a_s = sp.sympify(top_base_a)
    b_s = sp.sympify(bottom_base_b)
    h_s = sp.sympify(height)
    p_s = sp.sympify(p)
    q_s = sp.sympify(q)

    c_sq = sp.simplify((q_s * a_s**2 + p_s * b_s**2) / (p_s + q_s))
    c_len = sp.simplify(sp.sqrt(c_sq))

    if zero_test(b_s - a_s):
        h_upper = sp.simplify(h_s * p_s / (p_s + q_s))
    else:
        h_upper = sp.simplify(h_s * (c_len - a_s) / (b_s - a_s))
    h_lower = sp.simplify(h_s - h_upper)

    area_upper = sp.simplify((a_s + c_len) * h_upper / 2)
    area_lower = sp.simplify((c_len + b_s) * h_lower / 2)

    if not zero_test(area_upper * q_s - area_lower * p_s):
        raise AssertionError("Trapezoid parallel division failed exact p : q area check.")

    return TrapezoidDivisionResult(
        top_base_a=a_s,
        bottom_base_b=b_s,
        height=h_s,
        ratio_p=p_s,
        ratio_q=q_s,
        dividing_chord_c=c_len,
        upper_height=h_upper,
        lower_height=h_lower,
        upper_area=area_upper,
        lower_area=area_lower,
    )
