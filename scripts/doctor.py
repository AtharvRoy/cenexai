#!/usr/bin/env python3
"""Cenex AI environment diagnostics.

Checks common local setup prerequisites and explains what to do next.
"""

from __future__ import annotations

import importlib
import platform
import socket
import sys
from pathlib import Path

REQUIRED_PACKAGES = ("fastapi", "pydantic", "uvicorn")


def _check_python() -> tuple[bool, str]:
    ok = sys.version_info >= (3, 10)
    ver = platform.python_version()
    return ok, f"Python version: {ver} (required: >= 3.10)"


def _check_repo_files() -> tuple[bool, str]:
    required = [Path("requirements.txt"), Path("app/main.py"), Path("tests")]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        return False, f"Missing expected project paths: {', '.join(missing)}"
    return True, "Required project files found"


def _check_packages() -> tuple[bool, str]:
    missing = []
    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg)
        except Exception:
            missing.append(pkg)
    if missing:
        return (
            False,
            "Missing packages: "
            + ", ".join(missing)
            + " (run: python -m pip install -r requirements.txt)",
        )
    return True, "Required Python packages are importable"


def _check_network(host: str = "pypi.org", port: int = 443) -> tuple[bool, str]:
    try:
        with socket.create_connection((host, port), timeout=3):
            return True, f"Network check: able to reach {host}:{port}"
    except OSError as exc:
        return False, f"Network check failed for {host}:{port} ({exc})"


def main() -> int:
    checks = [
        ("python", _check_python),
        ("repo", _check_repo_files),
        ("packages", _check_packages),
        ("network", _check_network),
    ]

    failed = False
    for name, fn in checks:
        ok, msg = fn()
        marker = "OK" if ok else "FAIL"
        print(f"[{marker}] {name}: {msg}")
        failed = failed or (not ok)

    if failed:
        print("\nNext steps:")
        print("1) Create/activate a virtual environment")
        print("2) Install dependencies: python -m pip install -r requirements.txt")
        print("3) Re-run tests: python -m unittest discover -s tests -p 'test_*.py'")
        return 1

    print("\nEnvironment looks ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
