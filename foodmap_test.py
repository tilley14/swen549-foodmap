import pytest


@pytest.fixture
def app():
    import foodmap
    foodmap.app.testing = True
    return foodmap.app.test_client()