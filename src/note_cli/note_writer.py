"""
Write and open notes via the command line.
"""

import argparse
import logging
import os
import subprocess
import sys

__author__ = "Brian McVeigh"
__copyright__ = "Brian McVeigh"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

class NoteWriter:
    def __init__(self):
        self.note_cli_base_path = "~/.note-cli"
        self.note_cli_notes_path = f"{self.note_cli_base_path}/notes"
        self.note_title = sys.argv[2]

        # Recursively create the notes path if it does not exist.
        if not os.path.exists(self.note_cli_notes_path):
            print("Creating notes-cli notes path.")
            os.makedirs(self.note_cli_notes_path)

    def open_note(self):
        """Opens a note. Creates the note if it does not exist."""
        if len(sys.argv) <= 1:
            print("Missing note title. Cannot continue!")
            sys.exit()

        file_path = f"{self.note_cli_notes_path}/{sys.argv[1]}.md"
        # If the note path does not exist, create it.
        if not os.path.exists(file_path):
            print(f"Creating note: {self.note_title}")
            f = open(file_path, "w")
            f.write(f"# {self.note_title}\n")
            f.close
        else:
            # Let us know if the note was found as well.
            print(f"Note found, opening: {self.note_title}")

        subprocess.run(['code', file_path])
