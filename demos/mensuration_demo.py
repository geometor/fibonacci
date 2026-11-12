"""Runnable demonstration of *Practica Geometriae* Distinctio I & III: Pisan Metrology, Heron's Proof & Circle Bounds."""

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
    PisanLinearMeasure,
    construct_heron_incenter_proof,
    decompose_pisan_area,
    fibonacci_circle_bounds,
    heron_area_exact,
    multiply_pisan_lengths,
    verify_heron_polynomial_identity,
)


def main() -> None:
    console = Console()

    # 1. Pisan Surveyor's Metrology (Introductoria & Distinctio I, Boncompagni pp. 3–5)
    t_metro = Table(title="Distinctio I — Pisan Surveyor's Metrology (1 Stariorum = 66 Perticae)")
    t_metro.add_column("Width", style="cyan")
    t_metro.add_column("Length", style="cyan")
    t_metro.add_column("Superficial Perticae", style="green")
    t_metro.add_column("Stariora / Panora / Perticae / Pedes / Unciae", style="gold1")

    examples = [
        # Boncompagni p. 5: width = 7 perticae, length = 9 perticae, 2 pedes, 10 2/7 unciae -> 66 perticae = 1 stariorum
        (
            PisanLinearMeasure(perticae=7),
            PisanLinearMeasure(perticae=9, pedes=2, unciae=sp.Rational(72, 7)),
        ),
        (
            PisanLinearMeasure(perticae=12, pedes=3),
            PisanLinearMeasure(perticae=8, pedes=4, unciae=9),
        ),
        (
            PisanLinearMeasure(perticae=36),
            PisanLinearMeasure(perticae=44),
        ),
    ]
    for w, ln in examples:
        res = multiply_pisan_lengths(w, ln)
        t_metro.add_row(
            f"{w.perticae}p {w.pedes}ft {w.unciae}in",
            f"{ln.perticae}p {ln.pedes}ft {ln.unciae}in",
            str(res.total_perticae),
            f"{res.modiora} mod, {res.stariora} star, {res.panora} pan, "
            f"{res.perticae} pert, {res.pedes_superficiales} ped, {res.unciae_superficiales} unc",
        )
    console.print(t_metro)
    _ = decompose_pisan_area(66)

    # 2. Heron's Formula & Incenter Proof (Distinctio III, Boncompagni pp. 40–41)
    poly_res = verify_heron_polynomial_identity()
    heron_proof = construct_heron_incenter_proof()
    s22, exc22, sq22, area22 = heron_area_exact(13, 11, 20)

    t_heron = Table(title="Distinctio III — Heron's Formula & Geometric Incenter Proof")
    t_heron.add_column("Triangle / Check", style="cyan")
    t_heron.add_column("Semiperimeter s", style="white")
    t_heron.add_column("Excesses (s-a, s-b, s-c)", style="white")
    t_heron.add_column("Exact Area", style="green")
    t_heron.add_row(
        "Boncompagni p. 40 Numerical (13, 11, 20)",
        str(s22),
        str(exc22),
        f"sqrt({sq22}) = {area22}",
    )
    t_heron.add_row(
        "Geometric Incenter Model (13, 14, 15)",
        str(heron_proof.semiperimeter),
        str(heron_proof.excesses),
        f"r * s = {heron_proof.inradius} * {heron_proof.semiperimeter} = {heron_proof.area}",
    )
    t_heron.add_row(
        "Polynomial Identity Z[x,y,z] Residual",
        "-",
        "a=y+z, b=z+x, c=x+y",
        f"residual = {poly_res}",
    )
    console.print(t_heron)

    # 3. Fibonacci's 96-gon Circle Measurement (Distinctio III, Boncompagni pp. 88–91)
    cb = fibonacci_circle_bounds()
    t_pi = Table(title="Distinctio III — Fibonacci's 96-gon Circle Bounds vs. Archimedes")
    t_pi.add_column("Quantity", style="cyan")
    t_pi.add_column("Exact Rational", style="green")
    t_pi.add_column("Decimal (10 d.p.)", style="gold1")
    t_pi.add_row("Archimedes Lower (3 + 10/71)", str(cb.archimedes_lower), f"{float(cb.archimedes_lower):.10f}")
    t_pi.add_row("Fibonacci 96-gon Inscribed (1440 / 458 4/9)", str(cb.fibonacci_lower), f"{float(cb.fibonacci_lower):.10f}")
    t_pi.add_row("True pi", "pi", f"{float(sp.pi.evalf()):.10f}")
    t_pi.add_row("Fibonacci Mean Ratio (1440 / 458 1/3)", str(cb.fibonacci_pi), f"{float(cb.fibonacci_pi):.10f}")
    t_pi.add_row("Fibonacci 96-gon Circumscribed (1440 / 458 1/5)", str(cb.fibonacci_upper), f"{float(cb.fibonacci_upper):.10f}")
    t_pi.add_row("Archimedes Upper (864 / (275 - 1/11))", str(cb.archimedes_upper), f"{float(cb.archimedes_upper):.10f}")
    console.print(t_pi)


if __name__ == "__main__":
    main()
