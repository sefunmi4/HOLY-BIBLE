from flask import Flask, render_template
from bible.actions import TheActionsOfGod


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def index():
        # Using the actions module to demonstrate dynamic content
        verse = TheActionsOfGod.said("Let there be light")
        return render_template("index.html", verse=verse)

    return app
