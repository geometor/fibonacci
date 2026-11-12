"""Comprehensive exact symbolic, SVG, apparatus, and 4-track codex tests for geometor-fibonacci."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp

from geometor.fibonacci import (
    PHI,
    PISAN_AREA_PERTICAE,
    PisanLinearMeasure,
    __version__,
    construct_circle_archimedean_step,
    construct_dodecahedron_golden_chord,
    construct_heron_incenter_proof,
    construct_pentagon_decagon_in_circle,
    construct_pisan_pertica_grid,
    construct_quadrans_surveying,
    construct_sphere_polyhedra_section,
    construct_triangle_medians_centroid,
    construct_triangle_parallel_division,
    construct_triangle_side_point_division,
    decompose_pisan_area,
    fibonacci_circle_bounds,
    fibonacci_rabbit_convergents,
    flos_congruum_squares,
    flos_sexagesimal_cubic,
    heron_area_exact,
    multiply_pisan_lengths,
    polyhedra_in_sphere,
    solve_pentagon_ptolemy_quartic,
    trapezoid_parallel_division,
    verify_cassini_identity,
    verify_heron_polynomial_identity,
    verify_hypsicles_xiv_ratio,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCES_DIR = REPO_ROOT / "resources"
FIGURES_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"
CODEX_DIR = REPO_ROOT / "docsrc" / "practica_geometriae"


def _assert_zero_floats_in_model(model: object) -> None:
    """Assert that every geometric element inside ``model`` contains zero ``sp.Float`` atoms."""
    mapping = dict(model)  # type: ignore[arg-type]
    assert len(mapping) > 0
    for elem in mapping:
        if hasattr(elem, "atoms"):
            floats = elem.atoms(sp.Float)
            assert not floats, f"Found forbidden sp.Float {floats} in {elem!r}"
        elif hasattr(elem, "points"):
            for pt in elem.points:
                floats = pt.atoms(sp.Float)
                assert not floats, f"Found forbidden sp.Float {floats} in {pt!r}"


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_pisan_metrology_and_stariorum() -> None:
    assert PISAN_AREA_PERTICAE["pertica_superficialis"] == sp.Integer(1)
    assert PISAN_AREA_PERTICAE["pes_superficialis"] == sp.Rational(1, 6)
    assert PISAN_AREA_PERTICAE["denarius"] == sp.Rational(1, 36)
    assert PISAN_AREA_PERTICAE["panorum"] == sp.Rational(11, 2)
    assert PISAN_AREA_PERTICAE["stariorum"] == sp.Integer(66)

    # Boncompagni Vol. II, p. 5: frontage 7 perticae * depth 9p 2ft 10 2/7in = 66 perticae = 1 stariorum
    width = PisanLinearMeasure(perticae=7)
    depth = PisanLinearMeasure(perticae=9, pedes=2, unciae=sp.Rational(72, 7))
    prod = multiply_pisan_lengths(width, depth)
    assert prod.total_perticae == sp.Integer(66)
    assert prod.stariora == 1
    assert prod.panora == 0
    assert prod.perticae == 0
    assert prod.pedes_superficiales == 0
    assert prod.unciae_superficiales == 0

    decomp = decompose_pisan_area(66)
    assert decomp.stariora == 1
    assert decomp.total_denarii == 66 * 36


def test_heron_formula_and_incenter_proof() -> None:
    assert verify_heron_polynomial_identity() == 0

    s14, exc14, sq14, area14 = heron_area_exact(13, 14, 15)
    assert s14 == 21
    assert exc14 == (8, 7, 6)
    assert sq14 == 7056
    assert area14 == 84

    s22, _exc22, sq22, area22 = heron_area_exact(13, 11, 20)
    assert s22 == 22
    assert sq22 == 4356
    assert area22 == 66

    proof = construct_heron_incenter_proof()
    assert proof.incenter_t.x == sp.Integer(6)
    assert proof.incenter_t.y == sp.Integer(4)
    assert proof.inradius == sp.Integer(4)
    assert proof.semiperimeter == sp.Integer(21)
    assert proof.area == sp.Integer(84)
    _assert_zero_floats_in_model(proof.model)


def test_fibonacci_96gon_circle_bounds() -> None:
    cb = fibonacci_circle_bounds()
    assert cb.fibonacci_lower == sp.Rational(6480, 2063)
    assert cb.fibonacci_upper == sp.Rational(7200, 2291)
    assert cb.fibonacci_pi == sp.Rational(864, 275)
    assert cb.archimedes_upper == sp.Rational(22, 7)
    assert cb.archimedes_lower == sp.Rational(223, 71)

    assert cb.archimedes_lower < cb.fibonacci_lower
    assert float(cb.fibonacci_lower) < float(sp.pi.evalf()) < float(cb.fibonacci_pi)
    assert cb.fibonacci_pi < cb.fibonacci_upper < cb.archimedes_upper

    # Boncompagni Vol. II, p. 90: 864 / (275 - 1/11) == 22/7
    assert sp.Rational(864, 1) / (sp.Rational(275, 1) - sp.Rational(1, 11)) == sp.Rational(22, 7)


def test_distinctio_iv_divisions() -> None:
    # 1. Side-point bisection on (13, 14, 15) with BD = 5, DG = 9 -> GZ = 35/3 = 11 2/3
    side = construct_triangle_side_point_division(p=1, q=1, d_offset_from_b=5)
    assert side.gz_length == sp.Rational(35, 3)
    assert side.area_dzg == sp.Integer(42)
    assert side.area_abdz == sp.Integer(42)
    assert side.area_total == sp.Integer(84)
    _assert_zero_floats_in_model(side.model)

    # 1:2 division from same point D
    side_third = construct_triangle_side_point_division(p=1, q=2, d_offset_from_b=5)
    assert side_third.area_dzg == sp.Integer(28)
    assert side_third.area_abdz == sp.Integer(56)

    # 2. Parallel to base on (10, 14, 12) -> AE^2 = 50, AZ^2 = 72, EZ^2 = 98 (Boncompagni p. 119)
    par = construct_triangle_parallel_division(p=1, q=1, preset="10-14-12")
    assert par.ae_quadrance == sp.Integer(50)
    assert par.az_quadrance == sp.Integer(72)
    assert par.ez_quadrance == sp.Integer(98)
    assert sp.simplify(par.area_aez - par.area_ebgz) == 0
    _assert_zero_floats_in_model(par.model)

    # 3. Concurrency of medians & 3-consort centroid partition
    cent = construct_triangle_medians_centroid()
    assert cent.centroid_d.x == sp.Rational(19, 3)
    assert cent.centroid_d.y == sp.Integer(4)
    assert cent.consort_area == sp.Integer(28)
    assert cent.total_area == sp.Integer(84)
    _assert_zero_floats_in_model(cent.model)

    # 4. Trapezoid RMS chord (7^2 + 17^2 = 2 * 13^2)
    trap = trapezoid_parallel_division(top_base_a=7, bottom_base_b=17, height=10, p=1, q=1)
    assert trap.dividing_chord_c == sp.Integer(13)
    assert sp.simplify(trap.upper_area - trap.lower_area) == 0


def test_polyhedra_in_sphere_and_hypsicles_xiv() -> None:
    solids = polyhedra_in_sphere(6)
    section = construct_sphere_polyhedra_section()
    _assert_zero_floats_in_model(section.model)

    assert solids["tetrahedron"].edge_sq == 24
    assert solids["cube"].edge_sq == 12
    assert solids["octahedron"].edge_sq == 18
    assert solids["octahedron"].volume == 36
    assert sp.simplify(solids["dodecahedron"].edge - (sp.sqrt(15) - sp.sqrt(3))) == 0
    assert sp.simplify(solids["dodecahedron"].edge_sq - (18 - 6 * sp.sqrt(5))) == 0
    assert sp.simplify(solids["dodecahedron"].volume - (30 * sp.sqrt(3) + 6 * sp.sqrt(15))) == 0
    assert sp.simplify(solids["icosahedron"].edge_sq - (18 - sp.Rational(18, 5) * sp.sqrt(5))) == 0
    assert sp.simplify(solids["icosahedron"].volume - 18 * sp.sqrt(10 + 2 * sp.sqrt(5))) == 0

    for key, metric in solids.items():
        assert sp.simplify(section.quadrances[key] - metric.edge_sq) == 0

    xiv = verify_hypsicles_xiv_ratio(6)
    assert sp.simplify(xiv**2 - (5 + sp.sqrt(5)) / 6) == 0

    chord = construct_dodecahedron_golden_chord()
    assert sp.simplify(chord.golden_major - (sp.sqrt(15) - sp.sqrt(3))) == 0
    _assert_zero_floats_in_model(chord.model)


def test_pentagon_decagon_flos_and_rabbits() -> None:
    pent = construct_pentagon_decagon_in_circle()
    _assert_zero_floats_in_model(pent.model)
    assert sp.simplify(pent.decagon_side - 5 * (sp.sqrt(5) - 1) / 2) == 0
    assert sp.simplify(pent.pentagon_side_sq - (sp.Rational(125, 2) - sp.Rational(25, 2) * sp.sqrt(5))) == 0

    alg_side, alg_diag = solve_pentagon_ptolemy_quartic(10)
    assert sp.simplify(alg_side - pent.pentagon_side) == 0
    assert sp.simplify(alg_diag / alg_side - PHI) == 0

    cong_a, cong_x, cong_b = flos_congruum_squares()
    assert (cong_a, cong_x, cong_b) == (
        sp.Rational(31, 12),
        sp.Rational(41, 12),
        sp.Rational(49, 12),
    )
    assert cong_x**2 - 5 == cong_a**2
    assert cong_x**2 + 5 == cong_b**2

    cubic = flos_sexagesimal_cubic()
    assert cubic.rational_root == sp.Rational(1_596_577_777, 1_166_400_000)
    assert float(cubic.abs_root_error.evalf()) < 4e-11

    verify_cassini_identity(15)
    rows = fibonacci_rabbit_convergents(12)
    assert [r.pairs for r in rows] == [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert rows[-1].ratio_to_prev == sp.Rational(377, 233)


def test_remaining_models_zero_float() -> None:
    grid_model = construct_pisan_pertica_grid()
    circle_model = construct_circle_archimedean_step()
    quad_model = construct_quadrans_surveying()
    for m in (grid_model, circle_model, quad_model):
        _assert_zero_floats_in_model(m)


@pytest.mark.parametrize(
    "svg_name",
    [
        "pisan_pertica_grid",
        "heron_incenter_proof",
        "circle_96gon_bounds",
        "division_side_point",
        "division_parallel_base",
        "division_medians_centroid",
        "euclid_xiii_sphere_polyhedra",
        "dodecahedron_golden_chord",
        "quadrans_surveying",
        "pentagon_decagon_circle",
    ],
)
def test_interactive_euclid_graphic_svgs(svg_name: str) -> None:
    svg_path = FIGURES_DIR / f"{svg_name}.svg"
    assert svg_path.is_file(), f"Missing SVG figure {svg_path}"
    raw = svg_path.read_text(encoding="utf-8")
    root = ET.fromstring(raw)
    assert "euclid-graphic" in root.attrib.get("class", "")
    assert root.attrib.get("data-graphic-id") == svg_name
    assert 'id="geom-tick-1"' in raw
    assert 'id="highlights"' in raw
    assert "data-ref=" in raw


def test_apparatus_json_and_codex_four_track_parity() -> None:
    for fname in (
        "sources_manifest.json",
        "concordance.json",
        "persons.json",
        "citations.json",
        "glossary.json",
    ):
        fpath = RESOURCES_DIR / fname
        assert fpath.is_file(), f"Missing {fname}"
        data = json.loads(fpath.read_text(encoding="utf-8"))
        assert len(data) > 0

    svg_refs_by_id: dict[str, set[str]] = {}
    for svg_file in FIGURES_DIR.glob("*.svg"):
        root = ET.fromstring(svg_file.read_text(encoding="utf-8"))
        refs = {
            el.attrib["data-ref"]
            for el in root.iter()
            if "data-ref" in el.attrib
        }
        svg_refs_by_id[svg_file.stem] = refs

    g_role_re = re.compile(r":g:`[^`]*<([^:>]+):([^>]+)>`")

    for unit_num in range(1, 6):
        unit_dir = CODEX_DIR / f"unit-{unit_num}"
        assert unit_dir.is_dir()
        for track in ("en", "la", "summary", "notes"):
            rst_path = unit_dir / f"unit-{unit_num}-{track}.rst"
            assert rst_path.is_file(), f"Missing track {rst_path}"
            txt = rst_path.read_text(encoding="utf-8")
            assert ":layout: book" in txt
            assert f".. _unit-{unit_num}-{track}:" in txt
            assert "py_file" not in txt

            for graphic_id, elem_ref in g_role_re.findall(txt):
                assert graphic_id in svg_refs_by_id, f"Unknown SVG id {graphic_id} in {rst_path}"
                assert elem_ref in svg_refs_by_id[graphic_id], (
                    f"Missing data-ref {elem_ref!r} in {graphic_id}.svg (referenced in {rst_path.name})"
                )
