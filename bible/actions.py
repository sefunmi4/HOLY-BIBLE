class TheActionsOfGod:
    """A minimal implementation of actions used in Genesis."""

    # TODO: expand this class with additional methods for later chapters

    @staticmethod
    def heavens():
        return "heavens"

    @staticmethod
    def planet(name="earth"):
        return {"name": name}

    @staticmethod
    def darkness():
        return "darkness"

    @staticmethod
    def said(command):
        if command == "Let there be light":
            return "light"
        if command == "Let there be a vault":
            return "vault"
        # TODO: handle more creation commands (e.g., "Let dry ground appear")
        return None

    @staticmethod
    def saw(thing):
        return f"{thing} is good"

    @staticmethod
    def separate(light, darkness):
        # TODO: implement logic for tracking separated elements
        return light, darkness

    @staticmethod
    def call(name, thing):
        """Associate a name with a thing, similar to God naming creations."""
        return {name: thing}

class TheSpiritOfGod:
    # TODO: add more spiritual interactions
    @staticmethod
    def hover(target):
        return f"hovering over {target}"
