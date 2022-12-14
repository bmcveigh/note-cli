"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = note_cli.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import subprocess
import sys

__author__ = "Brian McVeigh"
__copyright__ = "Brian McVeigh"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

if len(sys.argv) <= 1:
    print("Missing note title. Cannot continue!")
    sys.exit()

print(f"Creating note: {sys.argv[1]}")
subprocess.run(['code'])
