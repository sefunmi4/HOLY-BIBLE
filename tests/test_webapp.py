from webapp import create_app
from webapp import notes as notes_module


def test_index_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Holy Bible App" in response.data


def test_notes_route(tmp_path, monkeypatch):
    notes_file = tmp_path / "notes.json"
    monkeypatch.setattr(notes_module, "NOTES_FILE", notes_file)

    app = create_app()
    client = app.test_client()

    response = client.post("/notes", data={"text": "My first note"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"My first note" in response.data
