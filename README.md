# Note CLI

Create and modify notes using [VSCode](https://code.visualstudio.com/) from the command line.

The [Markdown](https://www.markdownguide.org/cheat-sheet/) syntax is used for creating notes.

## Usage

### Open a note
This will also create a new note if it does not already exist.
``` bash
bin/note open "<note title>"
```

### Search for a note by keywords
``` bash
bin/note search "<note title>"
```

### Find a note by tag
Notes CLI supports tagging notes. Tags can be anywhere in the note
and use the format prefixed with a hashtag, e.g. `#Tag`.
``` bash
bin/note tag "<tag name>"
```
Note: you do not need to use the hashtag in the command to search for a tag.

## Maintainers
* Brian McVeigh
