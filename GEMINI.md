# GEOMETOR • `fibonacci`

Scholarly four-track Digital Scriptorium Book Codex (`:layout: book`) and exact `SymPy` / `geometor.model` constructive verification package for **Leonardo Pisano (Fibonacci): *Practica Geometriae* (1220)**, with foundational bridges from ***Flos* (1225)** and ***Liber Abaci* (1202/1228)**.

---

## 1. Purpose & Textual Provenance

- **Primary Source**: Baldassarre Boncompagni, *Scritti di Leonardo Pisano, matematico del secolo decimoterzo*, Vol. II: *Leonardi Pisani Practica Geometriae ed Opuscoli* (Rome, 1862; Vatican Cod. Urb. Lat. 292) and Vol. I: *Il Liber Abbaci* (Rome, 1857) — **100% Public Domain**.
- **Strict Copyright & Provenance Mandate**: All English translations in `docsrc/practica_geometriae/` are authored originally from Boncompagni's Latin folios. Never incorporate prose from copyrighted modern translations (e.g., Barnabas Hughes 2008 or Laurence Sigler 2002).
- **Strict Content / Code Separation**: Zero `py_file` directives in the historical codex; all executable symbolic constructions live in `src/geometor/fibonacci/`, `scripts/build_figures.py`, `demos/`, and `tests/`.

---

## 2. Repository Architecture

```text
fibonacci/
├── src/geometor/fibonacci/
│   ├── __init__.py            # Public API & version (0.1.0)
│   ├── __main__.py            # Rich CLI summary table
│   ├── mensuration.py         # Pisan pertica/stariorum, Heron incenter proof, 96-gon pi bounds
│   ├── divisions.py           # Distinctio IV (Euclid's On Divisions): side point, parallel, centroid, trapezoid
│   ├── polyhedra_golden.py    # Distinctio VI-VIII, Flos cubic/congruum, Liber Abaci Ch. 12 -> phi
│   ├── render.py              # Theme-adaptive .euclid-graphic SVG exporter (3-vertex midpoint paths)
│   └── sphinx_ext.py          # Runtime 'la' ("Latin (1220 / Boncompagni 1862)") track & local intersphinx
├── scripts/
│   └── build_figures.py       # Deterministically generates all 10 interactive SVGs
├── demos/
│   ├── mensuration_demo.py
│   ├── divisions_demo.py
│   └── polyhedra_golden_demo.py
├── resources/
│   ├── sources_manifest.json  # Public-domain source & folio provenance
│   ├── concordance.json       # 18-locus cross-canon concordance
│   ├── persons.json           # 21 biographical entries (:person:)
│   ├── citations.json         # 22 bibliographic entries (:cite:)
│   └── glossary.json          # 17 Pisan metrological & scholastic terms (:term:)
├── docsrc/
│   ├── conf.py
│   ├── _static/figures/       # 10 interactive .euclid-graphic SVGs
│   └── practica_geometriae/   # 5 units x 4 tracks (-en, -la, -summary, -notes) + apparatus indices
└── tests/
    └── test_fibonacci.py      # Exact algebraic, zero-Float, SVG XML, and 4-track parity test suite
```

---

## 3. Architectural Mandates & Verification Gates

1. **100% Exact Symbolic Algebra**:
   - Always instantiate `Model(..., logger=False, auto_intersect=False)` with explicit `model.intersect(...)`.
   - Zero `float` / `sp.Float` coordinates in `Model`, and never bypass `Model.__setitem__`.
2. **Offline Sandbox Commands (Python 3.13)**:
   ```bash
   pytest
   ruff check src scripts demos tests
   publish build
   ```
