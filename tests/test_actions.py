from bible.actions import TheActionsOfGod

def test_light_creation():
    light = TheActionsOfGod.said("Let there be light")
    assert light == "light"

def test_separation():
    light, darkness = TheActionsOfGod.separate("light", "darkness")
    assert light == "light"
    assert darkness == "darkness"
