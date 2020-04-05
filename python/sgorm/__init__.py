import os
import sys


def _resolve_paths():
    if not os.path.dirname(__file__) in sys.path:
        sys.path.insert(0, os.path.dirname(__file__))

    from .Connection import Connection, SgAuth


_resolve_paths()
del _resolve_paths
