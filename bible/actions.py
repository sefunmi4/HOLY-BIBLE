import logging


logger = logging.getLogger(__name__)


class TheActionsOfGod:
    """A minimal implementation of actions used in Genesis."""

    # TODO: expand this class with additional methods for later chapters

    @staticmethod
    def heavens():
        logger.info("Creating the heavens")
        return "heavens"

    @staticmethod
    def planet(name="earth"):
        logger.info("Creating planet %s", name)
        return {"name": name}

    @staticmethod
    def darkness():
        logger.info("Creating darkness")
        return "darkness"

    @staticmethod
    def said(command):
        logger.info("God said: %s", command)
        if command == "Let there be light":
            logger.info(" -> resulted in light")
            return "light"
        if command == "Let there be a vault":
            logger.info(" -> resulted in vault")
            return "vault"
        # TODO: handle more creation commands (e.g., "Let dry ground appear")

        logger.warning("Unknown command: %s", command)
        return None

    @staticmethod
    def saw(thing):
        logger.info("God saw %s", thing)
        return f"{thing} is good"

    @staticmethod
    def separate(light, darkness):
        logger.info("Separating %s from %s", light, darkness)
        # TODO: implement logic for tracking separated elements
        return light, darkness

    @staticmethod
    def call(name, thing):
        """Associate a name with a thing, similar to God naming creations."""
        logger.info("Calling %s %s", name, thing)
        return {name: thing}


class TheSpiritOfGod:
    # TODO: add more spiritual interactions
    @staticmethod
    def hover(target):
        logger.info("Spirit hovering over %s", target)
        return f"hovering over {target}"
