import pytest
import rose.tasks.db_setup as db
import rose.database.user_controller as user

@pytest.fixture()
def uc():
    db.setup(":memory:")
    uc = user.UserController(":memory:")
    cur = uc._connection.cursor()
    cur.execute('''
    CREATE TABLE users(
        id INTEGER, 
        steam TEXT, 
        switch TEXT, 
        ds TEXT, 
        playstation TEXT, 
        uplay TEXT, 
        origin TEXT, 
        xbox TEXT, 
        epic TEXT, 
        twitter TEXT, 
        telegram TEXT, 
        facebook TEXT, 
        tumblr TEXT, 
        mastodon TEXT, 
        youtube TEXT, 
        twitch TEXT, 
        deviantart TEXT, 
        etsy TEXT, 
        furaffinity TEXT)
    ''')
    uc._connection.commit()

    yield uc
    uc._connection.close()


def test_request_user_not_available(uc):
    with pytest.raises(TypeError):
        uc.read_user(1)

def test_create_user(uc):
    uc.create_user(14)
    user = uc.read_user(14)
    user['id'] == 14

def test_update_user(uc):
    uc.create_user(14)
    changeset = uc.empty_changeset
    changeset['twitter'] = 'real_praxis'
    uc.update_user(14, changeset)