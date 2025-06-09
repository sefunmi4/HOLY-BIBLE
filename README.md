# HOLY-BIBLE

A project exploring a **full‑stack book experience** for the Holy Bible. The goal is to use code and notebooks to create interactive retellings of biblical passages.

Comments quote passages from the HOLY BIBLE (NIV version) and code translates those passages into interactive stories and small games.

## Why?
Yuval Noah Harari mentioned that what makes people special is the stories we tell and the different ways we do it. Like scribes writing on paper, code is a new form of storytelling that allows us to interact with and experience the stories we choose to tell.

I want to know what it is like to be a scribe, practice coding and bible studies, and use code as a new form of record‑keeping.

If you are interested in any aspect of this project, feel free to message me on GitHub, send a feature request, bug issue, or clone the repo and send a pull request.

## Getting Started
1. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Install the project in editable mode:
   ```bash
   pip install -e .
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
   Then open `old_testament/genesis/Genesis.ipynb`.
4. Run the web application:
   ```bash
   flask --app webapp run
   ```
   Then open `http://localhost:5000/notes` to record notebook notes.

The notebook imports helpers from the `bible` package to model passages programmatically.

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on setting up your environment, running tests, and submitting pull requests.

## Series of Book Experiences:

| OLD TESTAMENT  | OLD TESTAMENT  |
|---------------|---------------|
| Genesis       | Ecclesiastes   |
| Exodus        | Song of Songs  |
| Leviticus     | Isaiah         |
| Numbers       | Jeremiah       |
| Deuteronomy   | Lamentations   |
| Joshua        | Ezekiel        |
| Judges        | Daniel         |
| Ruth          | Hosea          |
| 1 Samuel      | Joel           |
| 2 Samuel      | Amos           |
| 1 Kings       | Obadiah        |
| 2 Kings       | Jonah          |
| 1 Chronicles  | Micah          |
| 2 Chronicles  | Nahum          |
| Ezra          | Habakkuk       |
| Nehemiah      | Zephaniah      |
| Esther        | Haggai         |
| Job          | Zechariah       |
| Psalms        | Malachi        |
| Proverbs      |               |

| NEW TESTAMENT    | NEW TESTAMENT  |
|-----------------|---------------|
| Matthew         | 1 Timothy      |
| Mark            | 2 Timothy      |
| Luke            | Titus          |
| John            | Philemon       |
| Acts            | Hebrews        |
| Romans          | James          |
| 1 Corinthians   | 1 Peter        |
| 2 Corinthians   | 2 Peter        |
| Galatians       | 1 John         |
| Ephesians       | 2 John         |
| Philippians     | 3 John         |
| Colossians      | Jude           |
| 1 Thessalonians | Revelation     |
| 2 Thessalonians |                |

## TODO
- Expand the Genesis notebook with additional verses and refactor repeated logic into helper functions.
- Flesh out `bible.actions` with more creation commands and side effects.
- Define `PHYSICS` and `INFORMATION` classes per `Blueprints.txt`.
- Add more unit tests to improve coverage.
- Polish documentation for a public launch.
