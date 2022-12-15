"""
Write and open notes via the command line.
"""

import glob
import logging
import os
import subprocess
import sys

__author__ = "Brian McVeigh"
__copyright__ = "Brian McVeigh"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


class NoteManager:
    def __init__(self):
        self.note_cli_base_path = f"{os.getenv('HOME')}/.note-cli"
        self.note_cli_notes_path = f"{self.note_cli_base_path}/notes"

        if len(sys.argv) >= 3:
            self.note_title = sys.argv[2]
        else:
            self.note_title = "Untitled"

        # Recursively create the notes path if it does not exist.
        if not os.path.exists(self.note_cli_notes_path):
            print("Creating notes-cli notes path.")
            os.makedirs(self.note_cli_notes_path)

    def open_note(self):
        """Opens a note. Creates the note if it does not exist."""

        if len(sys.argv) <= 1:
            print("Missing note title. Cannot continue!")
            sys.exit()

        file_path = f"{self.note_cli_notes_path}/{self.note_title}.md"
        # If the note path does not exist, create it.
        if not os.path.exists(file_path):
            print(f"Creating note: {self.note_title}")
            f = open(file_path, "w")
            f.write(f"# {self.note_title}\n")
            f.close()
        else:
            # Let us know if the note was found as well.
            print(f"Note found, opening: {file_path}")

        subprocess.run(['code', file_path])

    def search_for_notes(self):
        """Find a list of notes matching a pattern."""

        os.chdir(self.note_cli_notes_path)
        # TODO: make this case insensitive.
        for file in glob.glob(f"*{self.note_title}*.md"):
            print(file)

    def search_for_tags(self):
        """Find a list of notes matching a pattern."""

        os.chdir(self.note_cli_notes_path)
        # TODO: make this case insensitive.
        for file in glob.glob("*.md"):
            f = open(file, "r")
            content = f.read()
            if f"#{sys.argv[2]}" in content:
                print(file)
            f.close()

    def search_for_todos(self):
        """Find a list of notes containing todos in Markdown format."""

        os.chdir(self.note_cli_notes_path)
        for file in glob.glob("*.md"):
            f = open(file, "r")
            content = f.read()
            if f"- [ ]" in content:
                print(file)
            f.close()
