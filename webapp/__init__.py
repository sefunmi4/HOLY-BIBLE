from flask import Flask, render_template, request, redirect, url_for
from bible.actions import TheActionsOfGod
from .notes import get_all_notes, save_note


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def index():
        # Using the actions module to demonstrate dynamic content
        verse = TheActionsOfGod.said("Let there be light")
        return render_template("index.html", verse=verse)

    @app.route("/notes", methods=["GET", "POST"])
    def notes():
        if request.method == "POST":
            text = request.form.get("text", "").strip()
            if text:
                save_note(text)
            return redirect(url_for("notes"))

        notes_list = get_all_notes()
        return render_template("notes.html", notes=notes_list)

    return app
