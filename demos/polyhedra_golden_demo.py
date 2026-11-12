"""Runnable demonstration of *Practica Geometriae* Dist. VI–VIII, *Flos* (1225), and *Liber Abaci* Ch. 12."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.fibonacci import (  # noqa: E402
    PHI,
    construct_dodecahedron_golden_chord,
    construct_pentagon_decagon_in_circle,
    construct_sphere_polyhedra_section,
    fibonacci_rabbit_convergents,
    flos_congruum_squares,
    flos_sexagesimal_cubic,
    polyhedra_in_sphere,
    solve_pentagon_ptolemy_quartic,
    verify_cassini_identity,
    verify_hypsicles_xiv_ratio,
)


def main() -> None:
    console = Console()

    # 1. Five Regular Polyhedra in a Sphere of Diameter d = 6 (Distinctio VI, pp. 190–202)
    solids = polyhedra_in_sphere(6)
    section = construct_sphere_polyhedra_section()
    chord = construct_dodecahedron_golden_chord()
    xiv_ratio = verify_hypsicles_xiv_ratio(6)

    t_poly = Table(title="Distinctio VI — Five Regular Polyhedra in a Sphere of Diameter d = 6")
    t_poly.add_column("Polyhedron", style="cyan")
    t_poly.add_column("Exact Edge e", style="white")
    t_poly.add_column("Embadum e^2", style="gold1")
    t_poly.add_column("Face r_f^2", style="white")
    t_poly.add_column("Insphere r_in^2", style="white")
    t_poly.add_column("Volume", style="green")
    for key, s in solids.items():
        assert sp.simplify(section.quadrances[key] - s.edge_sq) == 0
        t_poly.add_row(
            s.name,
            str(s.edge),
            str(s.edge_sq),
            str(s.face_circumradius_sq),
            str(s.insphere_radius_sq),
            str(sp.simplify(s.volume)),
        )
    console.print(t_poly)
    console.print(
        f"[bold green]Golden Chord BG[/bold green] = {chord.golden_major}, "
        f"[bold green]Hypsicles Book XIV Ratio V_12 / V_20[/bold green] = {xiv_ratio}\n"
    )

    # 2. Pentagon & Decagon in Diameter 10 (Distinctio VIII, pp. 207–208) + Flos (1225)
    pent = construct_pentagon_decagon_in_circle()
    alg_side, alg_diag = solve_pentagon_ptolemy_quartic(10)
    cubic = flos_sexagesimal_cubic()
    cong_a, cong_x, cong_b = flos_congruum_squares()

    t_sub = Table(title="Distinctio VIII & Flos (1225) — Algebraic & Geometric Subtleties")
    t_sub.add_column("Problem", style="cyan")
    t_sub.add_column("Exact Symbolic Result", style="green")
    t_sub.add_row(
        "Decagon & Pentagon in d = 10 (Euclid XIII.9–10)",
        f"s_10 = {pent.decagon_side}, s_5 = {pent.pentagon_side} (Ptolemy quartic diag/side = {sp.simplify(alg_diag / alg_side)})",
    )
    t_sub.add_row(
        "Flos Congruum Challenge x^2 +/- 5 = square",
        f"(a, x, b) = ({cong_a}, {cong_x}, {cong_b}) => x^2 - 5 = {cong_a**2}, x^2 + 5 = {cong_b**2}",
    )
    t_sub.add_row(
        "Flos Cubic x^3 + 2x^2 + 10x = 20",
        f"1;22,7,42,33,4,40 = {cubic.rational_root}, |x_Fib - x_exact| = {float(cubic.abs_root_error.evalf()):.3e}",
    )
    console.print(t_sub)

    # 3. Liber Abaci Ch. 12 Rabbit Recurrence -> Golden Ratio phi
    verify_cassini_identity(15)
    t_rab = Table(title=f"Liber Abaci Ch. 12 — Twelve-Month Rabbit Convergents to phi = {PHI}")
    t_rab.add_column("Month", justify="right", style="cyan")
    t_rab.add_column("Pairs F_{m+2}", justify="right", style="white")
    t_rab.add_column("Ratio F_{m+2}/F_{m+1}", style="green")
    t_rab.add_column("Cassini Det", justify="right", style="gold1")
    t_rab.add_column("|Ratio - phi|", style="magenta")
    for row in fibonacci_rabbit_convergents(12):
        t_rab.add_row(
            str(row.month),
            str(row.pairs),
            f"{row.ratio_to_prev} ({float(row.ratio_to_prev):.8f})",
            f"{int(row.cassini_determinant):+d}",
            f"{float(row.phi_error_abs.evalf()):.3e}",
        )
    console.print(t_rab)


if __name__ == "__main__":
    main()
