"""Publication-grade interactive `.euclid-graphic` SVG renderer for GEOMETOR Fibonacci.

Generates crisp pixel-space SVGs directly from :class:`~geometor.model.Model`
instances while preserving exact SymPy coordinates in metadata attributes and
``<title>`` tooltips. Outputs conform simultaneously to:

1. **Standalone SVG viewing** (GitHub ``README.rst``, browsers, ``prefers-color-scheme``
   dark/light palettes via an embedded ``<style>`` sheet), and
2. **PHOTON Publish interactive Book Codices** (``svg.euclid-graphic``, ``#elements``,
   ``#graphics``, ``#highlights``, ``#points``, ``#labels``, ``#geom-tick-1..3``
   markers, 3-vertex ``<path>`` segments, ``data-ref``, and ``data-aliases``).
"""

from __future__ import annotations

import html
import math
import re
from collections.abc import Sequence
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.sections import Section

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --carrier: #475569;
    --circle-main: #0284c7;
    --circle-guide: #64748b;
    --bisector: #0d9488;
    --parallel: #6366f1;
    --golden: #d97706;
    --tetra: #e11d48;
    --octa: #0284c7;
    --cube: #059669;
    --icosa: #7c3aed;
    --grid: #94a3b8;
    --share-p: #f59e0b;
    --share-q: #0ea5e9;
    --pes-strip: #10b981;
    --pt-given: #0f172a;
    --pt-result: #0369a1;
    --pt-mid: #0f766e;
    --pt-golden: #d97706;
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --carrier: #94a3b8;
      --circle-main: #38bdf8;
      --circle-guide: #94a3b8;
      --bisector: #2dd4bf;
      --parallel: #818cf8;
      --golden: #fbbf24;
      --tetra: #fb7185;
      --octa: #38bdf8;
      --cube: #34d399;
      --icosa: #c084fc;
      --grid: #64748b;
      --share-p: #fbbf24;
      --share-q: #38bdf8;
      --pes-strip: #34d399;
      --pt-given: #e2e8f0;
      --pt-result: #38bdf8;
      --pt-mid: #2dd4bf;
      --pt-golden: #fbbf24;
    }
  }
  .euclid-graphic .svg-bg { fill: var(--svg-bg); }
  .euclid-graphic .geom-circle { fill: none; stroke: var(--circle-main); stroke-width: 2.1; opacity: 0.9; }
  .euclid-graphic .geom-circle.incircle-curve { stroke: var(--golden); stroke-width: 2.35; }
  .euclid-graphic .geom-circle.guide-circle { stroke: var(--circle-guide); stroke-width: 1.35; stroke-dasharray: 5 4; opacity: 0.68; }
  .euclid-graphic .geom-circle.transfer-circle { stroke: var(--golden); stroke-width: 1.45; stroke-dasharray: 6 4; opacity: 0.78; }
  .euclid-graphic .geom-line { fill: none; stroke: var(--carrier); stroke-width: 1.45; stroke-linecap: round; opacity: 0.72; }
  .euclid-graphic .geom-line.carrier-line { stroke: var(--carrier); stroke-width: 1.85; opacity: 0.88; }
  .euclid-graphic .geom-line.bisector-line { stroke: var(--bisector); stroke-width: 1.55; stroke-dasharray: 6 3.5; opacity: 0.85; }
  .euclid-graphic .geom-line.parallel-line { stroke: var(--parallel); stroke-width: 1.65; stroke-dasharray: 5 3.5; opacity: 0.88; }
  .euclid-graphic .geom-line.tangent-line { stroke: var(--icosa); stroke-width: 1.75; opacity: 0.88; }
  .euclid-graphic .geom-segment { fill: none; stroke: var(--carrier); stroke-width: 2.1; stroke-linecap: round; }
  .euclid-graphic .geom-segment.grid-seg { stroke: var(--grid); stroke-width: 1.05; opacity: 0.48; }
  .euclid-graphic .geom-segment.bisector-seg { stroke: var(--bisector); stroke-width: 1.9; stroke-dasharray: 5 3; }
  .euclid-graphic .geom-segment.inradius-seg { stroke: var(--golden); stroke-width: 2.2; }
  .euclid-graphic .geom-segment.cut-seg { stroke: var(--golden); stroke-width: 3.0; }
  .euclid-graphic .geom-segment.golden-seg { stroke: var(--golden); stroke-width: 3.2; opacity: 0.95; }
  .euclid-graphic .geom-segment.tetra-seg { stroke: var(--tetra); stroke-width: 2.75; }
  .euclid-graphic .geom-segment.octa-seg { stroke: var(--octa); stroke-width: 2.75; }
  .euclid-graphic .geom-segment.cube-seg { stroke: var(--cube); stroke-width: 2.75; }
  .euclid-graphic .geom-segment.icosa-seg { stroke: var(--icosa); stroke-width: 2.75; }
  .euclid-graphic .geom-polygon { fill: var(--share-q); fill-opacity: 0.05; stroke: var(--carrier); stroke-width: 2.0; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.share-p-poly { fill: var(--share-p); fill-opacity: 0.13; stroke: var(--golden); stroke-width: 1.8; }
  .euclid-graphic .geom-polygon.share-q-poly { fill: var(--share-q); fill-opacity: 0.08; stroke: var(--circle-main); stroke-width: 1.6; }
  .euclid-graphic .geom-polygon.pes-strip-poly { fill: var(--pes-strip); fill-opacity: 0.14; stroke: var(--cube); stroke-width: 1.7; }
  .euclid-graphic .geom-polygon.denarius-poly { fill: var(--share-p); fill-opacity: 0.28; stroke: var(--golden); stroke-width: 2.2; }
  .euclid-graphic .geom-point { fill: var(--pt-given); stroke: var(--svg-bg); stroke-width: 1.5; }
  .euclid-graphic .geom-point.result-point { fill: var(--pt-result); }
  .euclid-graphic .geom-point.mid-point { fill: var(--pt-mid); }
  .euclid-graphic .geom-point.golden-point { fill: var(--pt-golden); stroke-width: 1.8; }
  .euclid-graphic .geom-label {
    fill: var(--ink);
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: var(--label-halo);
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 10px; font-weight: 600; }
""".strip()


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an infinite algebraic line $a x + b y + c = 0$ to a math bounding box."""
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None
    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split an alphanumeric point ID into ``(base, subscript)`` for ``<tspan>`` display."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _circle_css_classes(classes: set[str]) -> str:
    out = ["geom-circle"]
    if "incircle" in classes:
        out.append("incircle-curve")
    if "semicircle_guide" in classes:
        out.append("guide-circle")
    if "transfer_arc" in classes:
        out.append("transfer-circle")
    return " ".join(out)


def _line_css_classes(classes: set[str]) -> str:
    out = ["geom-line"]
    if "carrier" in classes:
        out.append("carrier-line")
    if "bisector" in classes:
        out.append("bisector-line")
    if "parallel_guide" in classes:
        out.append("parallel-line")
    if "tangent" in classes:
        out.append("tangent-line")
    return " ".join(out)


def _segment_css_classes(classes: set[str]) -> str:
    out = ["geom-segment"]
    if "grid" in classes:
        out.append("grid-seg")
    if "bisector" in classes or "guide_ray" in classes:
        out.append("bisector-seg")
    if "inradius" in classes:
        out.append("inradius-seg")
    if "cut_line" in classes:
        out.append("cut-seg")
    if "golden" in classes or "dodecahedron_edge" in classes:
        out.append("golden-seg")
    if "tetrahedron_edge" in classes:
        out.append("tetra-seg")
    if "octahedron_edge" in classes or "circum_side" in classes:
        out.append("octa-seg")
    if "cube_edge" in classes or "inscribed_side" in classes or "inscribed_12" in classes:
        out.append("cube-seg")
    if "icosahedron_edge" in classes or "chord_inscribed" in classes:
        out.append("icosa-seg")
    return " ".join(out)


def _polygon_css_classes(classes: set[str]) -> str:
    out = ["geom-polygon"]
    if "share_p" in classes:
        out.append("share-p-poly")
    if "share_q" in classes:
        out.append("share-q-poly")
    if "pes_strip" in classes:
        out.append("pes-strip-poly")
    if "denarius_sq" in classes:
        out.append("denarius-poly")
    return " ".join(out)


def _point_css_and_radius(classes: set[str]) -> tuple[str, float]:
    out = ["geom-point"]
    radius = 3.9
    if "given" in classes:
        out.append("given-point")
        radius = 4.2
    if "midpoint" in classes or "foot" in classes:
        out.append("mid-point")
        radius = 3.8
    if "result" in classes or "division_pt" in classes or "mean_pt" in classes:
        out.append("result-point")
        radius = 4.4
    if "golden" in classes or "incenter" in classes or "centroid" in classes or "consort_pt" in classes:
        out.append("golden-point")
        radius = 5.0
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """Compute pixel distance from ``(px, py)`` to segment ``(x1, y1)-(x2, y2)``."""
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    return math.hypot(px - proj_x, py - proj_y)


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "g1",
    title: str = "Fibonacci Practica Geometriae Construction",
    width: int = 680,
    height: int = 440,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> str:
    """Render a :class:`~geometor.model.Model` into a complete interactive `.euclid-graphic` SVG string."""
    visible_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    visible_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    visible_segments = [
        seg
        for seg in model
        if isinstance(seg, spg.Segment) and (include_guides or not model[seg].guide)
    ]
    visible_polygons = [
        poly
        for poly in model
        if isinstance(poly, spg.Polygon) and (include_guides or not model[poly].guide)
    ]
    visible_sections = [
        sec
        for sec in model
        if isinstance(sec, Section) and (include_guides or not model[sec].guide)
    ]
    visible_circles = [
        curve
        for curve in model
        if isinstance(curve, spg.Circle) and (include_guides or not model[curve].guide)
    ]

    frame_pts = list(focus_points) if focus_points else visible_points
    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif frame_pts or visible_circles:
        xs = [float(p.x.evalf()) for p in frame_pts]
        ys = [float(p.y.evalf()) for p in frame_pts]
        if focus_points is None:
            for curve in visible_circles:
                ccx = float(curve.center.x.evalf())
                ccy = float(curve.center.y.evalf())
                cr = float(curve.radius.evalf())
                xs.extend((ccx - cr, ccx + cr))
                ys.extend((ccy - cr, ccy + cr))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        pad_x = 0.12 * span_x
        pad_y = 0.14 * span_y
        xmin_m -= pad_x
        xmax_m += pad_x
        ymin_m -= pad_y
        ymax_m += pad_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -1.0, 5.0, -1.0, 3.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point, tuple[float, float]] = {
        pt: to_svg(float(pt.x.evalf()), float(pt.y.evalf())) for pt in visible_points
    }

    # 1. Circles
    circle_elems: list[str] = []
    for curve in visible_circles:
        el = model[curve]
        ccx_s, ccy_s = to_svg(float(curve.center.x.evalf()), float(curve.center.y.evalf()))
        r_px = float(curve.radius.evalf()) * scale
        on_curve_ids = [
            model[pt].ID
            for pt in visible_points
            if model[pt].ID and curve.contains(pt)
        ]
        cid = model[curve.center].ID if curve.center in model and model[curve.center].ID else ""
        if cid and on_curve_ids:
            primary_c_ref = f"( {cid} {on_curve_ids[0]} )"
        else:
            primary_c_ref = el.ID
        c_aliases: list[str] = []
        if el.ID and el.ID != primary_c_ref:
            c_aliases.append(el.ID)
        if cid:
            for pid in on_curve_ids:
                cand2 = f"( {cid} {pid} )"
                if cand2 != primary_c_ref and cand2 not in c_aliases:
                    c_aliases.append(cand2)
        if len(on_curve_ids) >= 3:
            cand3 = f"( {on_curve_ids[0]} {on_curve_ids[1]} {on_curve_ids[2]} )"
            if cand3 != primary_c_ref and cand3 not in c_aliases:
                c_aliases.append(cand3)
        c_alias_attr = f' data-aliases="{html.escape(" | ".join(c_aliases))}"' if c_aliases else ""
        c_ref_attr = f' data-ref="{html.escape(primary_c_ref)}"' if primary_c_ref else ""
        css_cls = _circle_css_classes(el.classes)
        eq_c_str = str(curve.equation())
        circle_elems.append(
            f'      <circle class="{css_cls}" '
            f'cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" r="{_fmt(r_px)}"'
            f'{c_ref_attr}{c_alias_attr} fill="none">'
            f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title></circle>"
        )

    # 2. Polygons
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        p_aliases: list[str] = []
        if el.ID and el.ID != poly_ref:
            p_aliases.append(el.ID)
        if len(vert_ids) >= 3:
            rev_ref = f"< {' '.join(reversed(vert_ids))} >"
            if rev_ref != poly_ref:
                p_aliases.append(rev_ref)
            for rot in range(1, len(vert_ids)):
                cyc = vert_ids[rot:] + vert_ids[:rot]
                cyc_ref = f"< {' '.join(cyc)} >"
                if cyc_ref != poly_ref and cyc_ref not in p_aliases:
                    p_aliases.append(cyc_ref)
        p_alias_attr = f' data-aliases="{html.escape(" | ".join(p_aliases))}"' if p_aliases else ""
        css_cls = _polygon_css_classes(el.classes)
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}"{p_alias_attr} fill="none" />'
        )

    # 3. Lines (3-vertex <path>)
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []
    for ln in visible_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(el.classes)
        incident_ids: list[str] = []
        for pt in visible_points:
            pid = model[pt].ID
            if not pid:
                continue
            px, py = pt_svg_coords[pt]
            if _point_to_segment_dist(px, py, sx1, sy1, sx2, sy2) < 0.85 and ln.contains(pt):
                incident_ids.append(pid)

        primary_ref = (
            f"[ {incident_ids[0]} {incident_ids[-1]} ]" if len(incident_ids) >= 2 else el.ID
        )
        aliases: list[str] = []
        if el.ID and el.ID != primary_ref:
            aliases.append(el.ID)
        for i in range(len(incident_ids)):
            for j in range(len(incident_ids)):
                if i == j:
                    continue
                for bracket_l, bracket_r in (("[", "]"), ("/", "/")):
                    cand = f"{bracket_l} {incident_ids[i]} {incident_ids[j]} {bracket_r}"
                    if cand != primary_ref and cand not in aliases:
                        aliases.append(cand)
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        eq_str = str(ln.equation())
        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # 4. Segments (3-vertex <path> with canonical `/ P Q /` data-ref)
    segment_elems: list[str] = []
    for seg in visible_segments:
        el = model[seg]
        p1, p2 = seg.p1, seg.p2
        sx1, sy1 = to_svg(float(p1.x.evalf()), float(p1.y.evalf()))
        sx2, sy2 = to_svg(float(p2.x.evalf()), float(p2.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        id1 = model[p1].ID if p1 in model and model[p1].ID else ""
        id2 = model[p2].ID if p2 in model and model[p2].ID else ""
        primary_s_ref = f"/ {id1} {id2} /" if (id1 and id2) else el.ID
        s_aliases: list[str] = []
        if el.ID and el.ID != primary_s_ref:
            s_aliases.append(el.ID)
        if id1 and id2:
            for cand in (f"/ {id2} {id1} /", f"[ {id1} {id2} ]", f"[ {id2} {id1} ]"):
                if cand != primary_s_ref and cand not in s_aliases:
                    s_aliases.append(cand)
        s_alias_attr = f' data-aliases="{html.escape(" | ".join(s_aliases))}"' if s_aliases else ""
        s_ref_attr = f' data-ref="{html.escape(primary_s_ref)}"' if primary_s_ref else ""
        css_cls = _segment_css_classes(el.classes)
        seg_len_str = str(sp.simplify(seg.length))
        segment_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{s_ref_attr}{s_alias_attr} fill="none">'
            f"<title>{html.escape(primary_s_ref)}: length = {html.escape(seg_len_str)}</title></path>"
        )

    # 5. Sections
    section_elems: list[str] = []
    for sec in visible_sections:
        if len(sec.points) >= 3:
            el = model[sec]
            p_start, p_end = sec.points[0], sec.points[-1]
            sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
            sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
            smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
            sec_ids = [model[p].ID for p in sec.points if p in model and model[p].ID]
            sec_ref = f"/ {' '.join(sec_ids)} /" if sec_ids else el.ID
            section_elems.append(
                f'      <path class="geom-segment golden-seg" '
                f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
                f'data-ref="{html.escape(sec_ref)}" fill="none" />'
            )

    # 6. Points & non-overlapping labels
    def _pt_z_key(pt: spg.Point) -> int:
        cls = model[pt].classes
        if "golden" in cls or "incenter" in cls or "centroid" in cls:
            return 40
        if "result" in cls or "division_pt" in cls:
            return 30
        if "given" in cls:
            return 20
        return 10

    sorted_pts = sorted(visible_points, key=_pt_z_key)
    highlight_ids = set(highlight_point_ids or ())
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in sorted_pts]

    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.28 * math.pi,
        -0.72 * math.pi,
        0.28 * math.pi,
        0.72 * math.pi,
        0.0,
        math.pi,
    ]

    for pt in sorted_pts:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue

        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(el.classes)
        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"

        if pid in highlight_ids:
            point_elems.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
                f'r="{_fmt(radius + 4.2)}" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.6" />'
            )

        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(radius)}"'
            f'{ref_attr} data-latex-x="{html.escape(x_latex)}" data-latex-y="{html.escape(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not show_labels or not pid:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 9.0 * len(base_txt) + 6.2 * len(sub_txt) + 4.0
        est_h = 14.0
        dist_r = radius + 12.0

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )

            score = 0.0
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0
            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 12.0:
                    score -= (12.0 - d_line) * 16.0
            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0
            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.0

            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)

        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f"{ref_attr}>{inner_txt}</text>"
        )

    defs_block = [
        "  <defs>",
        '    <marker id="geom-tick-1" viewBox="-4 -8 8 16" markerWidth="8" markerHeight="16" orient="auto">',
        '      <line x1="0" y1="-5" x2="0" y2="5" stroke="currentColor" stroke-width="1.5" />',
        "    </marker>",
        '    <marker id="geom-tick-2" viewBox="-6 -8 12 16" markerWidth="12" markerHeight="16" orient="auto">',
        '      <line x1="-2" y1="-5" x2="-2" y2="5" stroke="currentColor" stroke-width="1.5" />',
        '      <line x1="2" y1="-5" x2="2" y2="5" stroke="currentColor" stroke-width="1.5" />',
        "    </marker>",
        '    <marker id="geom-tick-3" viewBox="-8 -8 16 16" markerWidth="16" markerHeight="16" orient="auto">',
        '      <line x1="-4" y1="-5" x2="-4" y2="5" stroke="currentColor" stroke-width="1.5" />',
        '      <line x1="0" y1="-5" x2="0" y2="5" stroke="currentColor" stroke-width="1.5" />',
        '      <line x1="4" y1="-5" x2="4" y2="5" stroke="currentColor" stroke-width="1.5" />',
        "    </marker>",
        "  </defs>",
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        *defs_block,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" fill="none" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *polygon_elems,
        *circle_elems,
        *line_elems,
        *segment_elems,
        *section_elems,
        "    </g>",
        '    <g id="highlights"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "g1",
    title: str = "Fibonacci Practica Geometriae Construction",
    width: int = 680,
    height: int = 440,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> Path:
    """Write an interactive `.euclid-graphic` SVG rendering of ``model`` to ``output_path``."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        focus_points=focus_points,
        include_guides=include_guides,
        show_labels=show_labels,
        label_overrides=label_overrides,
        highlight_point_ids=highlight_point_ids,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()
