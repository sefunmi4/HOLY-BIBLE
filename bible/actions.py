class TheActionsOfGod:
    """A minimal implementation of actions used in Genesis."""

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
        return None

    @staticmethod
    def saw(thing):
        return f"{thing} is good"

    @staticmethod
    def separate(light, darkness):
        return light, darkness

class TheSpiritOfGod:
    @staticmethod
    def hover(target):
        return f"hovering over {target}"
