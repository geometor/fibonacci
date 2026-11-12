"""Sphinx configuration for GEOMETOR Fibonacci."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "divine" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.fibonacci as module  # noqa: E402
from geometor.fibonacci.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_latin_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "fibonacci"
repo_name = "fibonacci"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.fibonacci.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.fibonacci.sphinx_ext")  # noqa: F405

register_latin_book_track()
configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

project = "GEOMETOR • fibonacci"
author = "Leonardo Pisano (Fibonacci)"
copyright = "1220 / 1225 (Boncompagni 1857–1862 Public Domain) • Digital Codex & Translations GEOMETOR"

html_theme = "foundation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = None
autoapi_add_toctree_entry = False
napoleon_use_ivar = True
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]
