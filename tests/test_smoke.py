import importlib.util
from pathlib import Path

import numpy as np

import mdolib

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_truss():
    # exercises/tenbartruss is not a package, so load the file directly
    path = REPO_ROOT / "exercises" / "tenbartruss" / "truss.py"
    spec = importlib.util.spec_from_file_location("truss", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.truss


def test_mdolib_version():
    assert mdolib.__version__ == "0.1.0"


def test_truss_runs():
    truss = _load_truss()
    mass, stress = truss(np.ones(10))
    assert isinstance(mass, float)
    assert mass > 0
    assert stress.shape == (10,)
