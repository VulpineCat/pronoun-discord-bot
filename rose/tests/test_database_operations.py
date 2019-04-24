import pytest
import rose.tasks.db_setup as db

@pytest.fixture()
def setup():
    db.setup(":memory")

#def test_request_user_not_available():
