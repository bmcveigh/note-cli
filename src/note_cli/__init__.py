from sys import argv

from src.note_cli.note_manager import NoteManager

operation = argv[1]

writer = NoteManager()

if operation == "open":
    writer.open_note()
elif operation == "open-dir":
    writer.open_note_dir()
elif operation == "search":
    writer.search_for_notes()
elif operation == "tag":
    writer.search_for_tags()
elif operation == "todo":
    writer.search_for_todos()
else:
    print(f"Unrecognized command: {operation}!")
