from bible.actions import TheActionsOfGod, TheSpiritOfGod


def test_heavens():
    assert TheActionsOfGod.heavens() == "heavens"


def test_planet_default():
    assert TheActionsOfGod.planet() == {"name": "earth"}


def test_planet_custom():
    assert TheActionsOfGod.planet("mars") == {"name": "mars"}


def test_darkness():
    assert TheActionsOfGod.darkness() == "darkness"


def test_said_light():
    assert TheActionsOfGod.said("Let there be light") == "light"

def test_said_vault():
    assert TheActionsOfGod.said("Let there be a vault") == "vault"


def test_said_unknown():
    assert TheActionsOfGod.said("Let there be cake") is None


def test_saw():
    assert TheActionsOfGod.saw("light") == "light is good"


def test_separate():
    light, darkness = TheActionsOfGod.separate("light", "darkness")
    assert light == "light"
    assert darkness == "darkness"


def test_call():
    assert TheActionsOfGod.call("day", "light") == {"day": "light"}


def test_spirit_hover():
    assert TheSpiritOfGod.hover("waters") == "hovering over waters"