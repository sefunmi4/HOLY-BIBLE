import json
import os
from pathlib import Path
from typing import List, Dict


NOTES_FILE = Path(
    os.getenv("NOTES_FILE", Path(__file__).resolve().parent / "notes.json")
)


def load_notes() -> List[Dict[str, str]]:
    """Load notes from the JSON file."""
    if NOTES_FILE.exists():
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_note(text: str) -> None:
    """Append a note to the JSON file."""
    notes = load_notes()
    note = {"id": len(notes) + 1, "text": text}
    notes.append(note)
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)


def get_all_notes() -> List[Dict[str, str]]:
    return load_notes()
