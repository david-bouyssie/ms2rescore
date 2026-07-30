"""PyInstaller entrypoint for the MS²Rescore CLI.

On Windows, ``multiprocessing`` uses the "spawn" start method: child processes are created
by re-launching the frozen executable with internal arguments such as
``--multiprocessing-fork parent_pid=... pipe_handle=...``. Without
``multiprocessing.freeze_support()``, the child re-runs the CLI entrypoint, argparse sees
those internal arguments and aborts with "unrecognized arguments".

MS²Rescore's own GUI entrypoint (``ms2rescore/gui/__main__.py``) calls ``freeze_support()``
for exactly this reason, which is why the official GUI bundle works. The CLI entrypoint
(``ms2rescore/__main__.py``) does not, hence this thin wrapper, which mirrors the GUI
pattern: module-level import (so PyInstaller's static analysis picks up the dependency)
plus ``freeze_support()`` as the first statement of ``main()``.
"""

import multiprocessing

from ms2rescore.__main__ import main as cli_main


def main():
    """Entrypoint for the frozen MS²Rescore CLI."""
    multiprocessing.freeze_support()
    cli_main()


if __name__ == "__main__":
    main()
