from sys import argv

from src.note_cli.note_writer import NoteWriter

operation = argv[1]

writer = NoteWriter()

if operation == "open":
    writer.open_note()
elif operation == "search":
    writer.search_for_notes()
elif operation == "tag":
    writer.search_for_tags()
else:
    print(f"Unrecognized command: {operation}!")
