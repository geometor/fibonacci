"""Runnable demonstration of *Practica Geometriae* Distinctio IV (*De divisione camporum*)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.fibonacci import (  # noqa: E402
    construct_triangle_medians_centroid,
    construct_triangle_parallel_division,
    construct_triangle_side_point_division,
    trapezoid_parallel_division,
)


def main() -> None:
    console = Console()

    # 1. Dividing Triangle ABG from a Point D on Side BG (Boncompagni p. 112)
    side_bisect = construct_triangle_side_point_division(p=1, q=1, d_offset_from_b=5)
    side_third = construct_triangle_side_point_division(p=1, q=2, d_offset_from_b=5)

    t_side = Table(title="Distinctio IV — Dividing Triangle (13, 14, 15) from Point D on Side BG (BD = 5)")
    t_side.add_column("Target Ratio p : q", style="cyan")
    t_side.add_column("Base Point E", style="white")
    t_side.add_column("Cut Point Z on AG", style="white")
    t_side.add_column("Exact GZ", style="gold1")
    t_side.add_column("Share Areas (DZG : ABDZ)", style="green")
    for res in (side_bisect, side_third):
        t_side.add_row(
            f"{res.ratio_p} : {res.ratio_q}",
            str(res.pt_e),
            str(res.pt_z),
            str(res.gz_length),
            f"{res.area_dzg} : {res.area_abdz} (sum = {res.area_total})",
        )
    console.print(t_side)

    # 2. Dividing Triangle Parallel to Base via Euclid VI.13 Mean Proportional (Boncompagni p. 119)
    par_101412 = construct_triangle_parallel_division(p=1, q=1, preset="10-14-12")
    par_131415 = construct_triangle_parallel_division(p=1, q=2, preset="13-14-15")

    t_par = Table(title="Distinctio IV — Dividing Triangle Parallel to Base BG via Semicircle Mean Proportional")
    t_par.add_column("Triangle & Ratio", style="cyan")
    t_par.add_column("AE^2", style="gold1")
    t_par.add_column("AZ^2", style="gold1")
    t_par.add_column("EZ^2", style="gold1")
    t_par.add_column("Exact Areas (AEZ : EBGZ)", style="green")
    t_par.add_row(
        "(10, 14, 12), 1 : 1 (Boncompagni p. 119)",
        str(par_101412.ae_quadrance),
        str(par_101412.az_quadrance),
        str(par_101412.ez_quadrance),
        f"{par_101412.area_aez} : {par_101412.area_ebgz}",
    )
    t_par.add_row(
        "(13, 14, 15), 1 : 2",
        str(par_131415.ae_quadrance),
        str(par_131415.az_quadrance),
        str(par_131415.ez_quadrance),
        f"{par_131415.area_aez} : {par_131415.area_ebgz}",
    )
    console.print(t_par)

    # 3. Medians Concurrency & Three-Consort Centroid Partition (Boncompagni pp. 112–113, 120)
    cent = construct_triangle_medians_centroid()
    # 4. Trapezoid Parallel Bisection & Three Squares in Arithmetic Progression (7^2, 13^2, 17^2)
    trap = trapezoid_parallel_division(top_base_a=7, bottom_base_b=17, height=10, p=1, q=1)

    t_more = Table(title="Distinctio IV — Three-Consort Centroid & Trapezoid Root-Mean-Square Cut")
    t_more.add_column("Construction", style="cyan")
    t_more.add_column("Exact Invariants", style="green")
    t_more.add_row(
        "Three-Consort Centroid D = X(2) on (13, 14, 15)",
        f"D = {cent.centroid_d}, Area(DAB) = Area(DBG) = Area(DGA) = {cent.consort_area} (Total = {cent.total_area})",
    )
    t_more.add_row(
        "Trapezoid Parallel Bisection (a=7, b=17, h=10)",
        f"Chord c = {trap.dividing_chord_c} (7^2 + 17^2 = 2 * 13^2 = 338), Areas = {trap.upper_area} : {trap.lower_area}",
    )
    console.print(t_more)


if __name__ == "__main__":
    main()
