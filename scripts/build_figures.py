"""Generate all 10 interactive `.euclid-graphic` SVG plates for the Fibonacci Book Codex."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from geometor.fibonacci import (  # noqa: E402
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
    export_svg,
)

FIGURES_DIR = ROOT / "docsrc" / "_static" / "figures"


def build_all_figures(out_dir: Path = FIGURES_DIR) -> list[Path]:
    """Construct all exact symbolic models and export standalone + interactive SVGs."""
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # 1. Unit 1: Pisan Pertica 6x6 Denarius Grid
    m_pertica = construct_pisan_pertica_grid()
    written.append(
        export_svg(
            m_pertica,
            out_dir / "pisan_pertica_grid.svg",
            graphic_id="pisan_pertica_grid",
            title="Distinctio I — Pisan Pertica Superficialis (6 Pedes, 36 Denarii)",
            width=620,
            height=540,
            bbox=(-0.8, 6.8, -0.8, 6.8),
        )
    )

    # 2. Unit 2: Heron's Formula Incenter Proof
    heron_res = construct_heron_incenter_proof()
    written.append(
        export_svg(
            heron_res.model,
            out_dir / "heron_incenter_proof.svg",
            graphic_id="heron_incenter_proof",
            title="Distinctio III — Fibonacci's Geometric Incenter Proof of Heron's Formula",
            width=720,
            height=450,
            bbox=(-1.8, 22.8, -2.0, 13.8),
            highlight_point_ids=["T", "L"],
        )
    )

    # 3. Unit 2: Circle Measurement (Archimedean 6 -> 12 -> 96 Bisection)
    m_circle = construct_circle_archimedean_step()
    written.append(
        export_svg(
            m_circle,
            out_dir / "circle_96gon_bounds.svg",
            graphic_id="circle_96gon_bounds",
            title="Distinctio III — Circle Measurement (1440 : 458 1/3 = 864 : 275)",
            width=680,
            height=520,
            bbox=(-18.0, 19.5, -17.5, 17.5),
            highlight_point_ids=["F", "Y"],
        )
    )

    # 4. Unit 3: Division of a Triangle from a Point D on Side BG
    side_res = construct_triangle_side_point_division(p=1, q=1, d_offset_from_b=5)
    written.append(
        export_svg(
            side_res.model,
            out_dir / "division_side_point.svg",
            graphic_id="division_side_point",
            title="Distinctio IV — Dividing Triangle ABG from Point D on Side BG",
            width=680,
            height=460,
            bbox=(-1.5, 15.8, -1.8, 13.6),
            highlight_point_ids=["D", "Z"],
        )
    )

    # 5. Unit 3: Division of a Triangle Parallel to the Base via Mean Proportional
    par_res = construct_triangle_parallel_division(p=1, q=1, preset="10-14-12")
    written.append(
        export_svg(
            par_res.model,
            out_dir / "division_parallel_base.svg",
            graphic_id="division_parallel_base",
            title="Distinctio IV — Dividing Triangle ABG Parallel to Base BG via Semicircle Mean Proportional",
            width=700,
            height=500,
            bbox=(-2.2, 15.8, -1.8, 13.8),
            highlight_point_ids=["K", "E", "Z"],
        )
    )

    # 6. Unit 3: Medians & Three-Consort Centroid Division
    cent_res = construct_triangle_medians_centroid()
    written.append(
        export_svg(
            cent_res.model,
            out_dir / "division_medians_centroid.svg",
            graphic_id="division_medians_centroid",
            title="Distinctio IV — Concurrency of Medians and Three-Consort Centroid Partition",
            width=680,
            height=460,
            bbox=(-1.5, 15.8, -1.8, 13.6),
            highlight_point_ids=["D"],
        )
    )

    # 7. Unit 4: All Five Regular Polyhedron Edges in Sphere Diameter AI = 6
    sph_res = construct_sphere_polyhedra_section()
    written.append(
        export_svg(
            sph_res.model,
            out_dir / "euclid_xiii_sphere_polyhedra.svg",
            graphic_id="euclid_xiii_sphere_polyhedra",
            title="Distinctio VI & Euclid XIII.18 — Five Regular Polyhedra in Sphere of Diameter 6",
            width=680,
            height=520,
            bbox=(-3.9, 3.9, -3.6, 3.6),
            highlight_point_ids=["B", "C", "N", "M"],
        )
    )

    # 8. Unit 4: Extreme and Mean Ratio Division of Pentagon Chord BE = 2*sqrt(3)
    gold_res = construct_dodecahedron_golden_chord()
    written.append(
        export_svg(
            gold_res.model,
            out_dir / "dodecahedron_golden_chord.svg",
            graphic_id="dodecahedron_golden_chord",
            title="Distinctio VI — Modus Dividendi Lineam Media et Extrema Proportione",
            width=680,
            height=480,
            bbox=(-1.1, 5.4, -2.0, 3.2),
            highlight_point_ids=["G", "A"],
        )
    )

    # 9. Unit 5: Optical Quadrans Shadow Square (Distinctio VII)
    m_quad = construct_quadrans_surveying()
    written.append(
        export_svg(
            m_quad,
            out_dir / "quadrans_surveying.svg",
            graphic_id="quadrans_surveying",
            title="Distinctio VII — Optical Quadrans (Umbra Recta & Umbra Versa)",
            width=620,
            height=540,
            bbox=(-1.8, 13.8, -1.8, 13.8),
            highlight_point_ids=["D", "P", "C"],
        )
    )

    # 10. Unit 5: Regular Pentagon & Decagon in a Circle of Diameter 10 (Distinctio VIII)
    pent_res = construct_pentagon_decagon_in_circle()
    written.append(
        export_svg(
            pent_res.model,
            out_dir / "pentagon_decagon_circle.svg",
            graphic_id="pentagon_decagon_circle",
            title="Distinctio VIII — Regular Pentagon & Decagon in Circle of Diameter 10",
            width=680,
            height=540,
            bbox=(-6.2, 8.6, -6.0, 6.2),
            highlight_point_ids=["K", "D", "Q1"],
        )
    )

    return written


if __name__ == "__main__":
    paths = build_all_figures()
    for p in paths:
        print(f"Wrote {p.relative_to(ROOT)} ({p.stat().st_size:,} bytes)")
