"""Rich CLI overview for ``geometor-fibonacci``."""

from __future__ import annotations

import sympy as sp
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from geometor.fibonacci import (
    PHI,
    __version__,
    construct_heron_incenter_proof,
    construct_pentagon_decagon_in_circle,
    construct_triangle_parallel_division,
    construct_triangle_side_point_division,
    fibonacci_circle_bounds,
    fibonacci_rabbit_convergents,
    flos_sexagesimal_cubic,
    polyhedra_in_sphere,
    verify_hypsicles_xiv_ratio,
)


def main() -> None:
    """Print an exact symbolic summary of Fibonacci's *Practica Geometriae* (1220) constructions."""
    console = Console()
    console.print(
        Panel.fit(
            f"[bold gold1]GEOMETOR Fibonacci[/bold gold1] v{__version__}\n"
            "[italic]Leonardo Pisano: Practica Geometriae (1220), Liber Abaci (1202/1228) & Flos (1225)[/italic]",
            border_style="gold1",
        )
    )

    heron = construct_heron_incenter_proof()
    bounds = fibonacci_circle_bounds()
    side_div = construct_triangle_side_point_division(p=1, q=1, d_offset_from_b=5)
    par_div = construct_triangle_parallel_division(p=1, q=1, preset="10-14-12")
    pent = construct_pentagon_decagon_in_circle()
    cubic = flos_sexagesimal_cubic()
    rabbits = fibonacci_rabbit_convergents(12)

    summary = Table(title="Key Exact Symbolic Results (Boncompagni 1857–1862)", show_lines=True)
    summary.add_column("Locus", style="cyan", no_wrap=True)
    summary.add_column("Exact Symbolic Invariant", style="green")
    summary.add_row(
        "Dist. III — Heron Incenter Proof (13, 14, 15)",
        f"T = {heron.incenter_t}, r = {heron.inradius}, s = {heron.semiperimeter}, Area = {heron.area}",
    )
    summary.add_row(
        "Dist. III — 96-gon Circle Bounds",
        f"{bounds.fibonacci_lower} < pi < {bounds.fibonacci_upper}, pi_Fib = {bounds.fibonacci_pi} (~{float(bounds.fibonacci_pi):.7f})",
    )
    summary.add_row(
        "Dist. IV — Side-Point Division (BD = 5)",
        f"GZ = {side_div.gz_length}, Area(DZG) = {side_div.area_dzg}, Area(ABDZ) = {side_div.area_abdz}",
    )
    summary.add_row(
        "Dist. IV — Parallel Cut on (10, 14, 12)",
        f"AE^2 = {par_div.ae_quadrance}, AZ^2 = {par_div.az_quadrance}, EZ^2 = {par_div.ez_quadrance}",
    )
    summary.add_row(
        "Dist. VI — Hypsicles XIV Volume Ratio",
        f"V_12 / V_20 = e_6 / e_20 = {verify_hypsicles_xiv_ratio(6)}",
    )
    summary.add_row(
        "Dist. VIII — Pentagon & Decagon (d = 10)",
        f"s_10 = {pent.decagon_side}, s_5^2 = {pent.pentagon_side_sq}",
    )
    summary.add_row(
        "Flos (1225) — Cubic x^3 + 2x^2 + 10x = 20",
        f"1;22,7,42,33,4,40 = {cubic.rational_root} (|err| ~ {float(cubic.abs_root_error.evalf()):.2e})",
    )
    summary.add_row(
        "Liber Abaci Ch. 12 — Month 12 Rabbits",
        f"F_14 / F_13 = {rabbits[-1].ratio_to_prev} -> phi = {PHI} (|err| ~ {float(rabbits[-1].phi_error_abs.evalf()):.2e})",
    )
    console.print(summary)

    solids_table = Table(title="Five Regular Polyhedra in a Sphere of Diameter d = 6 (Dist. VI)")
    solids_table.add_column("Polyhedron", style="gold1")
    solids_table.add_column("Edge e")
    solids_table.add_column("Edge^2 (Embadum)")
    solids_table.add_column("Face r_f^2")
    solids_table.add_column("Volume")
    for solid in polyhedra_in_sphere(6).values():
        solids_table.add_row(
            solid.name,
            str(solid.edge),
            str(solid.edge_sq),
            str(solid.face_circumradius_sq),
            str(sp.simplify(solid.volume)),
        )
    console.print(solids_table)


if __name__ == "__main__":
    main()
