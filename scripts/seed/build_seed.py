"""Generate data/*.json for the Sheikh Qāsim Nānautavī demo. Usage: python3 scripts/seed/build_seed.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import write_all
import base, teachers, students, companions, works  # noqa: F401  (order matters: base first)
out = os.path.join(os.path.dirname(__file__), "..", "..", "data")
print(write_all(out, "qasim-nanautavi"))
