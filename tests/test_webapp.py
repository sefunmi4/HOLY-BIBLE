from webapp import create_app


def test_index_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Holy Bible App" in response.data
