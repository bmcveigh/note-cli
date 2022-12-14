from sys import argv

# python3 -m src.note_cli.create_note
from src.note_cli.note_writer import NoteWriter

operation = argv[1]

writer = NoteWriter()

if operation == "open":
    writer.open_note()
elif operation == "search":
    writer.search_for_notes()
else:
    print(f"Unrecognized command: {operation}!")
