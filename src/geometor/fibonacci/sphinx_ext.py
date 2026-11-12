"""Runtime Sphinx & photon-platform/publish integration for GEOMETOR Fibonacci.

Registers the ``la`` ("Latin (1220 / Boncompagni 1862)") companion track in
``photon_platform.publish.book`` at build time (without modifying any sibling
repository) alongside ``en``, ``summary``, and ``notes``, and binds offline-safe
local intersphinx inventories across the GEOMETOR canon.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

LATIN_TRACK_LABEL = "Latin (1220 / Boncompagni 1862)"

SISTER_REPOS: tuple[str, ...] = (
    "euclid",
    "elements",
    "heron",
    "archimedes",
    "pacioli",
    "divine",
    "phyllotaxis",
    "pappus",
    "etc",
    "wildberger",
    "proclus",
    "hilbert",
    "hoenen",
    "aquinas",
)


def register_latin_book_track() -> None:
    """Customize ``photon_platform.publish.book`` so ``<stem>-la`` renders with the Boncompagni 1862 label."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    la_pattern = (r"^(.+)[._-]la$", "la", LATIN_TRACK_LABEL)
    replaced = False
    for idx, (pat, key, _lbl) in enumerate(book._TRACK_SUFFIX_PATTERNS):
        if key == "la":
            book._TRACK_SUFFIX_PATTERNS[idx] = (pat, "la", LATIN_TRACK_LABEL)
            replaced = True
    if not replaced:
        book._TRACK_SUFFIX_PATTERNS.append(la_pattern)

    book._AUX_TRACK_BASENAMES.add("la")
    la_aux_re = re.compile(r"^.+[._-]la$")
    if not any(p.pattern == la_aux_re.pattern for p in book._AUX_TRACK_PATTERNS):
        book._AUX_TRACK_PATTERNS.append(la_aux_re)

    if getattr(book.detect_companion_tracks, "_fibonacci_la_patched", False):
        return

    orig_detect = book.detect_companion_tracks

    def _detect_with_boncompagni_latin(env: Any, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = book._extract_unit_stem(basename, doc_dir)
        if basename == "la" and doc_dir:
            stem = os.path.basename(doc_dir)

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        la_candidates = [_qual(f"{stem}.la"), _qual(f"{stem}_la"), _qual(f"{stem}-la"), _qual("la")]
        la_doc = next((c for c in la_candidates if c in found_docs), None)

        probe_page = pagename
        if la_doc and pagename == la_doc:
            en_cand = next(
                (c for c in (_qual(f"{stem}-en"), _qual(f"{stem}_en"), _qual(f"{stem}.en")) if c in found_docs),
                None,
            )
            if en_cand:
                probe_page = en_cand

        tracks = orig_detect(env, probe_page)
        if not la_doc:
            return tracks

        updated: list[dict[str, Any]] = []
        inserted_la = False
        la_entry = {
            "key": "la",
            "label": LATIN_TRACK_LABEL,
            "docname": la_doc,
            "active": la_doc == pagename,
        }
        for tr in tracks:
            if tr.get("docname") == la_doc or tr.get("key") == "la":
                continue
            item = dict(tr)
            item["active"] = item.get("docname") == pagename
            updated.append(item)
            if item.get("key") == "en" and not inserted_la:
                updated.append(la_entry)
                inserted_la = True

        if not inserted_la:
            updated.insert(0, la_entry)

        return updated if len(updated) >= 2 else []

    _detect_with_boncompagni_latin._fibonacci_la_patched = True  # type: ignore[attr-defined]
    book.detect_companion_tracks = _detect_with_boncompagni_latin


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any],
    project_root: Path,
) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR repositories and drop offline-unreachable targets."""
    geometor_dir = project_root.parent
    for sister in SISTER_REPOS:
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            intersphinx_mapping[sister] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: Any) -> dict[str, Any]:
    """Sphinx extension entry point."""
    register_latin_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
